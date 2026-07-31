import base64
import json
import time
from PIL import Image
import io
import urllib.request
import ssl

API_KEY = "sk-yB7U6B4nglE9Zt6GyMGtf2NajvN06uYOTMB8GUfZHAbsego5"

# Сжимаем фото
with open("abs.jpg", "rb") as f:
    img = Image.open(f)
if img.width > 800:
    img = img.resize((800, int(img.height * 800 / img.width)), Image.LANCZOS)
if img.mode in ('RGBA', 'P'):
    img = img.convert('RGB')
buffer = io.BytesIO()
img.save(buffer, format="JPEG", quality=60, optimize=True)
compressed = buffer.getvalue()

print(f"Сжатый размер: {len(compressed)} bytes ({len(compressed)/1024:.1f} KB)")
img_base64 = base64.b64encode(compressed).decode("utf-8")
print(f"Base64: {len(img_base64)} chars")

payload = json.dumps({
    "model": "kimi-k3",
    "messages": [{
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"}},
            {"type": "text", "text": "На фото экран диагностического сканера. Распознай коды ошибок (SPN, FMI). Ответь кратко."}
        ]
    }]
}).encode("utf-8")

print("\nОтправка через urllib (без прокси)...")
start = time.time()

req = urllib.request.Request(
    "https://api.moonshot.ai/v1/chat/completions",
    data=payload,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    method="POST"
)

# ЯВНО отключаем прокси и SSL-проверку (для теста)
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

proxy_handler = urllib.request.ProxyHandler({})  # ПУСТОЙ прокси = отключён
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)

try:
    with urllib.request.urlopen(req, timeout=120, context=context) as response:
        elapsed = time.time() - start
        data = json.loads(response.read().decode("utf-8"))
        content = data["choices"][0]["message"]["content"]
        print(f"✅ Успех за {elapsed:.1f} сек!")
        print(f"\n📋 Распознано:\n{content[:500]}")
        
except Exception as e:
    print(f"❌ ОШИБКА: {type(e).__name__}: {e}")