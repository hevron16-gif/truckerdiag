import os
import json
import base64
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import httpx

app = FastAPI(title="TruckerDiag AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ОТКЛЮЧАЕМ ПРОКСИ для Kimi API (proxy, не proxies!)
http_client = httpx.Client(proxy=None, timeout=60.0)

client = OpenAI(
    api_key=os.environ.get("MOONSHOT_API_KEY") or os.environ.get("KIMI_API_KEY") or "",
    base_url="https://api.moonshot.ai/v1",
    http_client=http_client,
)

SERVICE_MANUAL = """HOWO A7 СЕРВИСНАЯ КНИГА
=====================================
P1011 - Ошибка дозирующего клапана ТНВД
На моделях Howo A7 с двигателем WD615:
• Причина 1 (83%): Засор сетки на обратке топлива. Номинал давления: 2.5 бар.
  OEM запчасть: VG1540090006
• Причина 2 (12%): Износ редукционного клапана ТНВД
  OEM запчасть: VG1092040306
• Причина 3 (5%): Обрыв проводки датчика давления
  Проверка: мультиметром, сопротивление 2.5 кОм ± 0.2

P0087 - Низкое давление топлива в рампе
• Причина 1 (70%): Засор топливного фильтра
• Причина 2 (20%): Неисправность ТНВД
• Причина 3 (10%): Утечка на обратке

U0155 - Потеря связи с приборной панелью
• Проверить разъём X201 (20-pin) под панелью приборов
• Сопротивление CAN-шины: 60 Ом между CAN-H и CAN-L
"""

SYSTEM_PROMPT = f"""Ты — эксперт-диагност китайских грузовиков Howo.
У тебя есть доступ к сервисной книге.
Отвечай СТРОГО в формате JSON.

Сервисная книга:
{SERVICE_MANUAL}

Формат ответа:
{{
  "error_description": "описание ошибки",
  "top_causes": [
    {{"cause": "причина", "probability": 83, "oem_part": "номер запчасти"}}
  ],
  "check_steps": ["шаг 1", "шаг 2"],
  "severity": "can_drive|limited|tow",
  "estimated_time_min": 45
}}
"""


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


@app.post("/diagnose", response_model=DiagnoseResponse)
async def diagnose(req: DiagnoseRequest):
    user_prompt = f"""
Модель: {req.vehicle_model}
Двигатель: {req.engine}
Год: {req.year}
Код ошибки: {req.error_code}
Доп. данные: {json.dumps(req.freeze_frame or {}, ensure_ascii=False)}
"""
    try:
        response = client.chat.completions.create(
            model="kimi-k3",
            reasoning_effort="max",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
        )
        result = json.loads(response.choices[0].message.content)
        return DiagnoseResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/diagnose-photo")
async def diagnose_photo(photo: UploadFile = File(...), vehicle_model: str = "Howo A7", engine: str = "WD615", year: int = 2019):
    """Принимает фото экрана сканера, распознаёт коды ошибок, диагностирует"""
    try:
        contents = await photo.read()

        if len(contents) > 5 * 1024 * 1024:
            raise HTTPException(status_code=400, detail="Файл слишком большой (макс 5MB)")

        img_base64 = base64.b64encode(contents).decode("utf-8")

        vision_response = client.chat.completions.create(
            model="kimi-k3",
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"}
                    },
                    {
                        "type": "text",
                        "text": f"""На фото экран диагностического сканера грузовика {vehicle_model} ({engine}, {year}).
                        1. Распознай ВСЕ коды ошибок (включая китайские иероглифы, если есть).
                        2. Определи модель техники, если видно на экране.
                        3. Верни ТОЛЬКО JSON: {{"error_codes": ["P1011"], "vehicle_model": "Howo A7", "notes": "доп. наблюдения"}}"""
                    }
                ]
            }],
            response_format={"type": "json_object"},
        )

        ocr_result = json.loads(vision_response.choices[0].message.content)
        error_codes = ocr_result.get("error_codes", [])

        if not error_codes:
            return {"error": "Коды ошибок не распознаны", "ocr_raw": ocr_result}

        diagnoses = []
        for code in error_codes:
            user_prompt = f"""
Модель: {ocr_result.get('vehicle_model', vehicle_model)}
Двигатель: {engine}
Год: {year}
Код ошибки: {code}
Доп. данные: {json.dumps(ocr_result.get('notes', ''), ensure_ascii=False)}
"""
            diag_response = client.chat.completions.create(
                model="kimi-k3",
                reasoning_effort="max",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ],
                response_format={"type": "json_object"},
            )
            diagnoses.append(json.loads(diag_response.choices[0].message.content))

        return {
            "ocr_result": ocr_result,
            "diagnoses": diagnoses
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка обработки: {str(e)}")


@app.get("/health")
async def health():
    return {"status": "ok", "api": "kimi-k3", "ocr": "enabled"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
