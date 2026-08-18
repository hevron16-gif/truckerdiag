# Деплой на Render

Один Web Service: backend + фронт с того же хоста.

## Сервис

- **Type:** Web Service
- **Root Directory:** `api`
- **Runtime:** Python 3
- **Build:** `pip install -r requirements.txt`
- **Start:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Health Check:** `/health`

`PORT` Render задаёт сам — в переменные его писать не нужно.

## Переменные окружения

| Переменная | Обязательно | Значение |
|------------|-------------|----------|
| `XAI_API_KEY` | да | ключ с [console.x.ai](https://console.x.ai) |
| `XAI_MODEL` | нет | `grok-4.6` |
| `XAI_BASE_URL` | нет | `https://api.x.ai/v1` |
| `SERVE_WEB` | нет | `1` (отдавать PWA из `web/`) |
| `CORS_ORIGINS` | нет | `*` или ваши домены через запятую |
| `DEBUG` | нет | `0` в проде |
| `ADMIN_PASSWORD` | да для отзывов | свой пароль админки |

## Фронт

При `SERVE_WEB=1` сайт открывается по URL сервиса Render. API — тот же хост, отдельно ничего прописывать не нужно.

Если фронт на другом хосте — в `web/config.js` укажите:

```js
window.TRUCKERDIAG_API = "https://ВАШ-СЕРВИС.onrender.com";
```

Либо один раз откройте сайт с `?api=https://ВАШ-СЕРВИС.onrender.com` — адрес сохранится в браузере. Клик по адресу API в подвале тоже меняет его.
