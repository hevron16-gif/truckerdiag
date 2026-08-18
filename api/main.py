import os
import re
import json
import hmac
import base64
import traceback
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from openai import OpenAI
import httpx

from knowledge import format_entry, format_service_manual, images_for, known_codes, lookup
from comments_store import add_comment, approve_comment, delete_comment, list_all, list_approved

load_dotenv(Path(__file__).resolve().parent / ".env")
load_dotenv()

XAI_BASE_URL = os.environ.get("XAI_BASE_URL", "https://api.x.ai/v1")
XAI_MODEL = os.environ.get("XAI_MODEL", "grok-4.6")
XAI_API_KEY = os.environ.get("XAI_API_KEY", "").strip()
DEBUG = os.environ.get("DEBUG", "").strip().lower() in {"1", "true", "yes"}
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "changeme").strip()
SERVE_WEB = os.environ.get("SERVE_WEB", "1").strip().lower() not in {"0", "false", "no"}
WEB_DIR = Path(__file__).resolve().parent.parent / "web"


def _cors_origins() -> list[str]:
    raw = os.environ.get("CORS_ORIGINS", "*").strip()
    if not raw or raw == "*":
        return ["*"]
    return [part.strip() for part in raw.split(",") if part.strip()]

PROMPT_PATH = Path(__file__).resolve().parent / "prompt.txt"

app = FastAPI(title="TruckerDiag AI")

_origins = _cors_origins()
app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins,
    allow_credentials=_origins != ["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Без системного прокси (на Windows часто висит SOCKS 127.0.0.1:10808 —
# httpx его подхватывает даже при proxy=None, если trust_env=True).
http_client = httpx.Client(
    trust_env=False,
    timeout=httpx.Timeout(180.0, connect=15.0),
)

client = OpenAI(
    api_key=XAI_API_KEY or "missing-xai-api-key",
    base_url=XAI_BASE_URL,
    http_client=http_client,
)

JSON_SCHEMA_HINT = """
Формат ответа — один JSON-объект, без markdown и без текста вокруг:
{
  "error_description": "Подробное описание простым языком: что чувствует водитель, как проявляется, на каких режимах.",
  "top_causes": [
    {
      "cause": "причина",
      "probability": 45,
      "oem_part": "номер или пустая строка",
      "comment": "почему это часто встречается"
    }
  ],
  "check_steps": ["Шаг 1 — самый простой", "Шаг 2"],
  "severity": "can_drive|limited|tow",
  "estimated_time_min": 40,
  "practical_advice": "Можно ли ехать и какие ограничения"
}
"""

OEM_RULES = """
ЖЁСТКИЕ ПРАВИЛА:
1. Отвечай СТРОГО валидным JSON на русском. Никакого текста до/после, никаких ``` ограждений.
2. Ты опытный диагност Howo, Shacman, Sitrak и двигателей Weichai.
   WP* = Weichai, WD615 = Sinotruk Howo, ISM11 = Cummins на Shacman.
3. 4–6 причин, строго по полевой частоте. Самая частая — первая.
4. OEM только из сервисной базы для этой причины, иначе "". Не выдумывать номера.
5. Если кода нет в базе — честно напиши, что точных данных мало, oem_part всегда "".
6. Описание живое и практичное. check_steps — от простого к сложному.
7. probability — целые 0–100, сумма ≈ 100. severity только: can_drive, limited, tow.
"""


def _default_system_prompt() -> str:
    return (
        "Ты — опытный диагност китайских грузовиков Howo, Shacman, Sitrak и двигателей Weichai.\n"
        f"{OEM_RULES}\n"
        f"{JSON_SCHEMA_HINT}\n"
        "Сервисная база:\n"
        f"{format_service_manual()}\n"
    )


def load_system_prompt() -> str:
    if PROMPT_PATH.is_file():
        text = PROMPT_PATH.read_text(encoding="utf-8").strip()
        if "{{SERVICE_MANUAL}}" in text:
            return text.replace("{{SERVICE_MANUAL}}", format_service_manual())
        if text:
            return f"{text}\n\nСервисная база:\n{format_service_manual()}\n"
    return _default_system_prompt()


SYSTEM_PROMPT = load_system_prompt()


class DiagnoseRequest(BaseModel):
    vehicle_model: str
    engine: str
    year: int
    error_code: str
    freeze_frame: dict | None = None


class CommentIn(BaseModel):
    name: str
    text: str


class DiagnoseResponse(BaseModel):
    error_description: str
    top_causes: list[dict]
    check_steps: list[str]
    severity: str
    estimated_time_min: int
    practical_advice: str = ""
    images: list[dict] = []


def _require_api_key() -> None:
    if not XAI_API_KEY:
        raise HTTPException(
            status_code=503,
            detail="XAI_API_KEY не задан. Скопируйте api/.env.example в api/.env и укажите ключ.",
        )


def _strip_json_fences(raw: str) -> str:
    text = (raw or "").strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s*```$", "", text)
    return text.strip()


def _parse_json_content(raw: str) -> dict:
    text = _strip_json_fences(raw)
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, flags=re.DOTALL)
        if not match:
            raise
        data = json.loads(match.group(0))
    if not isinstance(data, dict):
        raise ValueError("Модель вернула не объект JSON")
    return data


def _sanitize_diagnosis(
    data: dict,
    error_code: str,
    *,
    engine: str | None = None,
    brand: str | None = None,
) -> dict:
    """Режем выдуманные OEM: оставляем номер, только если он есть в базе для этого кода."""
    entry = lookup(error_code, engine=engine, brand=brand)
    allowed: set[str] = set()
    if entry:
        for cause in entry.get("causes") or []:
            oem = (cause.get("oem_part") or "").strip()
            if oem:
                allowed.add(oem.upper())

    causes = data.get("top_causes") or []
    cleaned = []
    if isinstance(causes, list):
        for item in causes:
            if not isinstance(item, dict):
                continue
            oem = str(item.get("oem_part") or "").strip()
            if oem.upper() not in allowed:
                oem = ""
            cleaned.append(
                {
                    "cause": str(item.get("cause") or "").strip(),
                    "probability": int(item.get("probability") or 0),
                    "oem_part": oem,
                    "comment": str(item.get("comment") or "").strip(),
                }
            )
    data["top_causes"] = cleaned

    steps = data.get("check_steps") or []
    data["check_steps"] = [str(s) for s in steps] if isinstance(steps, list) else []

    severity = str(data.get("severity") or "limited").strip().lower().replace(" ", "")
    if "|" in severity:
        severity = severity.split("|", 1)[0]
    if severity not in {"can_drive", "limited", "tow"}:
        severity = "limited"
    data["severity"] = severity

    try:
        data["estimated_time_min"] = int(data.get("estimated_time_min") or 30)
    except (TypeError, ValueError):
        data["estimated_time_min"] = 30

    data["error_description"] = str(data.get("error_description") or "").strip() or "Нет описания"
    data["practical_advice"] = str(data.get("practical_advice") or "").strip()
    # Картинки только из базы, модель их не выбирает и не выдумывает.
    data["images"] = images_for(error_code, engine=engine, brand=brand)
    return data


def _chat_json(messages: list[dict], *, timeout: float | None = None) -> dict:
    _require_api_key()
    kwargs: dict = {
        "model": XAI_MODEL,
        "messages": messages,
        "response_format": {"type": "json_object"},
        "temperature": 0.2,
    }
    if timeout is not None:
        kwargs["timeout"] = timeout
    response = client.chat.completions.create(**kwargs)
    content = response.choices[0].message.content or ""
    return _parse_json_content(content)


def _run_diagnosis(
    *,
    vehicle_model: str,
    engine: str,
    year: int,
    error_code: str,
    extra: dict | str | None = None,
) -> dict:
    known = lookup(error_code, engine=engine, brand=vehicle_model)
    if known:
        kb_hint = (
            "Код есть в сервисной базе — опирайся на карточку. "
            "4–6 причин по полевой частоте, OEM только из базы, "
            "заполни comment и practical_advice.\n\n"
            f"Карточка кода:\n{format_entry(known)}"
        )
    else:
        kb_hint = (
            "Кода нет в сервисной базе. Честно напиши, что точных данных мало, "
            "дай общие рекомендации по системе, oem_part всегда пустой, 4–6 причин."
        )
    extra_json = json.dumps({} if extra is None else extra, ensure_ascii=False)
    user_prompt = f"""
Модель: {vehicle_model}
Двигатель: {engine}
Год: {year}
Код ошибки: {error_code}
Доп. данные: {extra_json}
{kb_hint}
Верни JSON по схеме.
"""
    raw = _chat_json(
        [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ]
    )
    return _sanitize_diagnosis(
        raw, error_code, engine=engine, brand=vehicle_model
    )


@app.post("/diagnose", response_model=DiagnoseResponse)
async def diagnose(req: DiagnoseRequest):
    try:
        result = _run_diagnosis(
            vehicle_model=req.vehicle_model,
            engine=req.engine,
            year=req.year,
            error_code=req.error_code,
            extra=req.freeze_frame,
        )
        return DiagnoseResponse(**result)
    except HTTPException:
        raise
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=str(e) if DEBUG else "Внутренняя ошибка сервера",
        )


def _image_media_type(photo: UploadFile) -> str:
    ctype = (photo.content_type or "").split(";")[0].strip().lower()
    if ctype in {"image/jpeg", "image/jpg", "image/png", "image/webp"}:
        return "image/jpeg" if ctype == "image/jpg" else ctype
    name = (photo.filename or "").lower()
    if name.endswith(".png"):
        return "image/png"
    if name.endswith(".webp"):
        return "image/webp"
    return "image/jpeg"


@app.post("/diagnose-photo")
async def diagnose_photo(
    photo: UploadFile = File(...),
    vehicle_model: str = Form("Howo A7"),
    engine: str = Form("WD615"),
    year: int = Form(2019),
):
    """Принимает фото экрана сканера, распознаёт коды ошибок, диагностирует."""
    try:
        contents = await photo.read()

        if len(contents) > 5 * 1024 * 1024:
            raise HTTPException(status_code=400, detail="Файл слишком большой (макс 5MB)")
        if not contents:
            raise HTTPException(status_code=400, detail="Пустой файл")

        media_type = _image_media_type(photo)
        img_base64 = base64.b64encode(contents).decode("utf-8")

        ocr_result = _chat_json(
            [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:{media_type};base64,{img_base64}"},
                        },
                        {
                            "type": "text",
                            "text": (
                                f"На фото экран диагностического сканера грузовика "
                                f"{vehicle_model} ({engine}, {year}).\n"
                                "1. Распознай ВСЕ коды ошибок (P/U/C/B и SPN/FMI, включая китайские подписи).\n"
                                "2. Определи модель техники, если видно на экране.\n"
                                "3. Верни ТОЛЬКО JSON: "
                                '{"error_codes": ["P1011"], "vehicle_model": "Howo A7", "notes": "доп. наблюдения"}'
                            ),
                        },
                    ],
                }
            ]
        )

        error_codes = ocr_result.get("error_codes") or []
        if isinstance(error_codes, str):
            error_codes = [error_codes]
        error_codes = [str(c).strip() for c in error_codes if str(c).strip()]

        if not error_codes:
            return {"error": "Коды ошибок не распознаны", "ocr_raw": ocr_result}

        diagnoses = []
        resolved_model = ocr_result.get("vehicle_model") or vehicle_model
        for code in error_codes:
            diagnoses.append(
                _run_diagnosis(
                    vehicle_model=resolved_model,
                    engine=engine,
                    year=year,
                    error_code=code,
                    extra=ocr_result.get("notes", ""),
                )
            )

        return {"ocr_result": ocr_result, "diagnoses": diagnoses}

    except HTTPException:
        raise
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=str(e) if DEBUG else "Ошибка обработки фото",
        )


def _client_ip(request: Request) -> str:
    forwarded = request.headers.get("x-forwarded-for", "")
    if forwarded:
        return forwarded.split(",")[0].strip()[:64]
    if request.client and request.client.host:
        return request.client.host[:64]
    return ""


@app.post("/api/comments")
async def create_comment(payload: CommentIn, request: Request):
    name = (payload.name or "").strip()
    text = (payload.text or "").strip()
    if not name or len(name) > 80:
        raise HTTPException(status_code=400, detail="Укажите имя (до 80 символов)")
    if not text or len(text) > 2000:
        raise HTTPException(status_code=400, detail="Укажите текст комментария (до 2000 символов)")
    add_comment(name=name, text=text, ip=_client_ip(request))
    return {"ok": True, "message": "Комментарий отправлен на модерацию"}


@app.get("/api/comments")
async def get_comments():
    return {"comments": list_approved()}


def _require_admin(request: Request) -> None:
    given = (
        request.headers.get("x-admin-password")
        or request.query_params.get("password")
        or ""
    ).strip()
    ok = (
        bool(ADMIN_PASSWORD)
        and len(given) == len(ADMIN_PASSWORD)
        and hmac.compare_digest(given, ADMIN_PASSWORD)
    )
    if not ok:
        raise HTTPException(status_code=401, detail="Неверный пароль")


@app.get("/api/admin/comments")
async def admin_list_comments(request: Request):
    _require_admin(request)
    return {"comments": list_all()}


@app.post("/api/admin/comments/{comment_id}/approve")
async def admin_approve_comment(comment_id: int, request: Request):
    _require_admin(request)
    if not approve_comment(comment_id):
        raise HTTPException(status_code=404, detail="Комментарий не найден")
    return {"ok": True}


@app.delete("/api/admin/comments/{comment_id}")
async def admin_delete_comment(comment_id: int, request: Request):
    _require_admin(request)
    if not delete_comment(comment_id):
        raise HTTPException(status_code=404, detail="Комментарий не найден")
    return {"ok": True}


@app.get("/parts-images")
async def parts_images(code: str):
    """Справочные фото узла по коду ошибки (без вызова модели)."""
    return {"code": code, "images": images_for(code)}


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "api": XAI_MODEL,
        "provider": "xai",
        "ocr": "enabled",
        "has_api_key": bool(XAI_API_KEY),
        "knowledge_codes": len(known_codes()),
    }


if SERVE_WEB and WEB_DIR.is_dir():
    app.mount("/", StaticFiles(directory=str(WEB_DIR), html=True), name="web")


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
