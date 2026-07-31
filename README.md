# TruckerDiag

PWA + FastAPI for Chinese truck diagnostics (Howo, Shacman, Yutong).

## Structure

| Path | Description |
|------|-------------|
| `web/` | PWA frontend (vanilla HTML/JS) |
| `api/` | FastAPI backend (Kimi/Moonshot) |

## Backend

```bash
cd api
pip install -r requirements.txt
set MOONSHOT_API_KEY=your_key
python main.py
```

API: http://localhost:8000  
Health: http://localhost:8000/health

## Frontend

```bash
cd web
python -m http.server 5500
```

Open http://localhost:5500

## Env

| Variable | Description |
|----------|-------------|
| `MOONSHOT_API_KEY` or `KIMI_API_KEY` | Moonshot/Kimi API key |
