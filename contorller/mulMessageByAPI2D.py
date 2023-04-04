import requests
from flask import Blueprint, render_template, request

mul_message_api2d = Blueprint('mul_mes_spi2d', __name__)
url = "https://openai.api2d.net/v1/chat/completions"
keys = 'fk188609-96dTUaP7eav6Sfd9Ax16B34T9CP7aCVp'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(keys)
    # <-- 把 fkxxxxx 替换成你自己的 Forward Key，注意前面的 Bearer 要保留，并且和 Key 中间有一个空格。
}


def get_response(incoming_msg):
    system_prompt = {"role": "system", "content": "You are a helpful assistant."}
    data = []
    if incoming_msg == 'clear':
        data.clear()
        data.append({"role": "assistant", "content": 'hello'})
    else:
        data.append({"role": "assistant", "content": incoming_msg})

    messages = [system_prompt]
    messages.extend(data)
    try:
        requests.post(url, headers=headers, json=data)
        response = requests.post(
            url,
            headers=headers,
            json={
                "model": "gpt-3.5-turbo",
                "messages": messages
            }
        ).json()
        content = response["choices"][0]["message"]["content"]
        return content
    except IndexError as e:
        print(e)
        return ""


@mul_message_api2d.route('/message/api2d')
def message_home():
    return render_template("message_index_api2d.html")


@mul_message_api2d.route('/message/api2d/chat', methods=["GET", "POST"])
def message_chat_api2d():
    user_text = request.args.get('msg')
    return str(get_response(user_text))


if __name__ == '__main__':
    print(get_response('你好'))
