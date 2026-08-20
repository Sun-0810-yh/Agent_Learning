import requests
import os
from dotenv import load_dotenv

# 读取 .env
load_dotenv()

# 获取 API Key
api_key = os.getenv("OPENAI_API_KEY")

# 准备messages
messages = [
    {
        "role": "system",#system用来给模型设置行为规则、身份、任务目标、回答风格等
        "content": "你是一名 Python 教程助手。"
    },
    {
        "role": "user",#用户发送的问题
        "content": "什么是 FastAPI？"
    },
    {
        "role": "assistant",#ai回答的问题
        "content": "FastAPI 是一个基于 Python 的 Web 框架。"
    },
    {
        "role": "user",#写在一起让大模型理解上下文
        "content": "它和 Flask 有什么区别？"
    }
]

# 准备请求头
data = {"messages": messages}

# 发送 POST 请求
response = requests.post(
    "你的LLM API地址",
    headers = {
    #"Authorization"     → API / HTTP 规范规定的名字
    # "Bearer"          → 认证规范规定的格式
    # api_key           → 你自己定义的 Python 变量
    "Authorization": f"Bearer {api_key}"
    },
    json = data

)

# 打印服务器返回的数据
print(response.json())


