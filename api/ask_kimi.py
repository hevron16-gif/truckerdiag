import requests, json

prompt = open('prompt.txt','r',encoding='utf-8').read()

print('Отправка запроса в Kimi...')
resp = requests.post(
    'https://api.moonshot.ai/v1/chat/completions',
    headers={
        'Authorization': 'Bearer sk-yB7U6B4nglE9Zt6GyMGtf2NajvN06uYOTMB8GUfZHAbsego5',
        'Content-Type': 'application/json'
    },
    json={
        'model': 'kimi-k3',
        'messages': [{'role': 'user', 'content': prompt}]
    },
    proxies={'http': None, 'https': None},
    timeout=180
)

print(f'Статус: {resp.status_code}')
content = resp.json()['choices'][0]['message']['content']
open('response.txt','w',encoding='utf-8').write(content)
print(f'Ответ сохранен в response.txt ({len(content)} символов)')
