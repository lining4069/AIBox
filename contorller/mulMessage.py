from flask import Blueprint, render_template, request
import openai

mul_message = Blueprint('mul_message', __name__)

openai.api_key = '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'
systemPrompt = {"role": "system", "content": "You are a helpful assistant."}
data = []


def get_response(incoming_msg):
    if incoming_msg == "clear":
        data.clear()
        data.append({"role": "assistant", "content": 'hello'})
    else:
        data.append({"role": "assistant", "content": incoming_msg})

    messages = [systemPrompt]
    messages.extend(data)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        content = response["choices"][0]["message"]["content"]
        return content
    except openai.error.RateLimitError as e:
        print(e)
        return ""


@mul_message.route('/message/index')
def message_home():
    return render_template("message_index_api2d.html")


@mul_message.route('/message/chat')
def gpt_response():
    userText = request.args.get('msg')
    return str(get_response(userText))


if __name__ == '__main__':
    print(get_response('你好'))
