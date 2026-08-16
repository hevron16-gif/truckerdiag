# TruckerDiag

PWA + FastAPI for Chinese truck diagnostics (Howo, Shacman, Weichai).

## Structure

| Path | Description |
|------|-------------|
| `web/` | PWA frontend (vanilla HTML/JS) |
| `api/` | FastAPI backend (xAI Grok 4.6) |

## Backend

```bash
cd api
pip install -r requirements.txt
copy .env.example .env
# впишите XAI_API_KEY в .env
python main.py
```

API: http://localhost:8000  
Health: http://localhost:8000/health

Эндпоинты:

- `POST /diagnose` — диагностика по коду ошибки
- `POST /diagnose-photo` — OCR фото сканера + диагностика каждого кода
- `GET /health`

## Frontend

```bash
cd web
python -m http.server 5500
```

Open http://localhost:5500

## Env

| Variable | Description |
|----------|-------------|
| `XAI_API_KEY` | xAI / SpaceXAI API key ([console.x.ai](https://console.x.ai)) |
| `XAI_MODEL` | optional, default `grok-4.6` |
| `XAI_BASE_URL` | optional, default `https://api.x.ai/v1` |

Ключ не коммитить: `.env` уже в `.gitignore`.
