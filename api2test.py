import requests

url = "https://openai.api2d.net/v1/chat/completions"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer fk188609-96dTUaP7eav6Sfd9Ax16B34T9CP7aCVp'
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "你好！给我讲个笑话。"}]
}

response = requests.post(url, headers=headers, json=data)

print("Status Code", response.status_code)
print("JSON Response ", response.json())
