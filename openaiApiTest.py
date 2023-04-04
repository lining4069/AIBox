# Python 请求示例
import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(completion.choices[0].message)
