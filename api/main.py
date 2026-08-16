import os
import re
import json
import base64
import traceback
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import httpx

from knowledge import format_service_manual, lookup

load_dotenv(Path(__file__).resolve().parent / ".env")
load_dotenv()

XAI_BASE_URL = os.environ.get("XAI_BASE_URL", "https://api.x.ai/v1")
XAI_MODEL = os.environ.get("XAI_MODEL", "grok-4.6")
XAI_API_KEY = os.environ.get("XAI_API_KEY", "").strip()

PROMPT_PATH = Path(__file__).resolve().parent / "prompt.txt"

app = FastAPI(title="TruckerDiag AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
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


class DiagnoseResponse(BaseModel):
    error_description: str
    top_causes: list[dict]
    check_steps: list[str]
    severity: str
    estimated_time_min: int
    practical_advice: str = ""


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


def _sanitize_diagnosis(data: dict, error_code: str) -> dict:
    """Режем выдуманные OEM: оставляем номер, только если он есть в базе для этого кода."""
    entry = lookup(error_code)
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
    known = lookup(error_code)
    kb_hint = (
        "Код есть в сервисной базе — опирайся на неё. 4–6 причин по полевой частоте, "
        "OEM только из базы, заполни comment и practical_advice."
        if known
        else (
            "Кода нет в сервисной базе. Честно напиши, что точных данных мало, "
            "дай общие рекомендации по системе, oem_part всегда пустой, 4–6 причин."
        )
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
    return _sanitize_diagnosis(raw, error_code)


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
        raise HTTPException(status_code=500, detail=str(e))


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
        raise HTTPException(status_code=500, detail=f"Ошибка обработки: {str(e)}")


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "api": XAI_MODEL,
        "provider": "xai",
        "ocr": "enabled",
        "has_api_key": bool(XAI_API_KEY),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
