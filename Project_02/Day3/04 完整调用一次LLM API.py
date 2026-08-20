import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}"
}

def chat(user_input):
    messages = [
        {
            "role": "system",#system用来给模型设置行为规则、身份、任务目标、回答风格等
            "content": "你是一名 Python 教程助手。"
        },
        {
            "role": "user",#用户发送的问题
            "content": user_input
        },
    ]
    data = {
        "messages" : messages
    }

    response = requests.post(
        "你的LLM API地址",
        headers = headers,
        json = data
    )

    if response.status_code == 200:
        result = response.json()

        answer = result["choices"][0]["message"]["content"]

        return answer

    else:
        print("请求失败")
        print("状态码：", response.status_code)
        print("错误信息：", response.text)
        return None


user_input = input("今天想问点什么？：")

answer = chat(user_input)

if answer:
    print("AI:", answer)
