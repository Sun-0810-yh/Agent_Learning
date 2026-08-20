Day 3 随记 ｜ FastAPI + LLM API（调用链）
1. API Key 安全管理
Key 是访问 LLM 的凭证，不能硬编码（传 GitHub 会泄露）。用 .env 存，.gitignore 加 .env。load_dotenv() 把 .env 内容加载到环境变量，os.getenv() 从环境变量取值。

```python
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```
2. Authorization 认证头
HTTP 请求头携带 Key，格式 Bearer {api_key}。Authorization 是 HTTP 规范字段，Bearer 是认证方式，api_key 是你的变量。不同厂商认证方式可能不同，以文档为准。

python
headers = {"Authorization": f"Bearer {api_key}"}

3. messages 消息结构
LLM 聊天发的是 messages 列表，每条是 {role, content} 字典。system 设模型身份/规则/风格，user 是用户提问，assistant 是历史回答。第一次请求没历史对话就别伪造 assistant。

```python
messages = [
    {"role": "system", "content": "你是一名 Python 教程助手。"},
    {"role": "user", "content": "什么是 FastAPI？"}
]
```
4. 请求体 + requests.post
messages 放进 data 字典，json=data 自动转 JSON body，headers=headers 带认证。

```python
import requests
data = {"messages": messages}
response = requests.post("API地址", headers=headers, json=data)
```
5. 状态码判断
200 成功，401 Key 有问题，429 限流，500 服务器错误。失败时看 response.text 排查。

```python
if response.status_code == 200:
    result = response.json()
else:
    print("失败:", response.status_code, response.text)
```
6. Response 解析
response.json() 把 JSON 响应解析成 Python 字典。取值路径 choices[0].message.content 本质是按嵌套结构逐层取：dict→list→dict→dict→str。别死记路径，理解结构才是关键。

python
answer = result["choices"][0]["message"]["content"]

7. 封装 chat() 函数
把整个调用链封装成函数，return answer 把结果交还给调用处（不是 print 显示，是让外部能继续用）。print = 显示给看，return = 交给程序用。

```python
def chat(user_input):
    messages = [
        {"role": "system", "content": "你是一名 Python 教程助手。"},
        {"role": "user", "content": user_input}
    ]
    response = requests.post("API地址", headers=headers,
                             json={"messages": messages})
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    print("失败:", response.status_code)
    return None

answer = chat(input("想问什么？"))
if answer: print("AI:", answer)
```
8. 完整调用链（Day 3 核心）
用户输入 user_input
  → 构造 messages(system+user)
  → 构造 data
  → .env → load_dotenv → os.getenv → api_key
  → headers = Bearer {api_key}
  → requests.post(url, headers, json)
  → LLM 大模型处理
  → HTTP Response
  → response.json()
  → choices[0].message.content
  → return answer
  → 主程序接收并显示

以后 agent.run("你好") 看着一行，底层仍然是这条链：消息→模型调用→Response→解析→返回。框架只是帮你把重复工作封装了。