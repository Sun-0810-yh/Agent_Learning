from fastapi import FastAPI
from pydantic.v1 import JsonTypeError

app = FastAPI()#创建一个 FastAPI 应用实例，并把这个实例保存到 app 变量中。

@app.get("/health")#它把“GET + /health”这个 HTTP 请求注册到 health() 函数。
                    #一个 API 路由 = HTTP 方法 + 路径。 FastAPI 匹配路由的时候，不只看路径，还看 HTTP 方法。
def health():
    return{"status": "ok"}

#访问浏览器请求的完整链路：
# 你运行 uvicorn
#       ↓
# Uvicorn 启动服务器
#       ↓
# 等待 HTTP 请求
#       ↓
# 浏览器发送 GET /health
#       ↓
# Uvicorn 接收请求
#       ↓
# FastAPI 根据路由匹配
#       ↓
# 找到 health()
#       ↓
# 执行 health()
#       ↓
# 得到 Python 字典
#       ↓
# FastAPI 把它转换成 JSON Response
#       ↓
# 返回浏览器

#HTTP方法：
# GET：请求服务器返回某些资源或数据。
# POST：向服务器提交数据，让服务器创建某个资源或者执行某个操作。

#GET参数：Query Parameter
#我要查询某一个用户:/users?user_id=100
@app.get("/users")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }
#访问：http://127.0.0.1:8000/users?user_id=100  这里?user_id=100就是Query Parameter

#Get参数：Path Parameter
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }
#访问：http://127.0.0.1:8000/users/100   这里/100就是Query Parameter

#Query Parameter与Path Parameter区别：
#? 后面的是 Query Parameter。 URL 路径里面 {} 对应的是 Path Parameter。

# POST发送的数据是放在HTTP Request Body请求体里面
# POST /users
# {
#     "name": "顺顺",
#     "age": 20
# }
# HTTP Request
# ┌──────────────────────┐
# │ Method: POST         │
# │ Path: /users         │
# ├──────────────────────┤
# │ Body:                │
# │ {                    │
# │   "name": "顺顺",     │
# │   "age": 20          │
# │ }                    │
# └──────────────────────┘

from pydantic import BaseModel
class UserCreate(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_uer(user: UserCreate):
    return{
        "name": user.name,
        "age": user.age
    }

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    ...


from fastapi import FastAPI
from pydantic import BaseModel

@app.get("/users")
def get_users():
    return{
        "users":[
            {"id":1,"name":"张三"},
            {"id": 2, "name": "李四"},
        ]
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }

class UserCreate(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: UserCreate):#创建一个叫 user 的参数，并且告诉 Python/FastAPI：这个参数应该是 UserCreate 类型
    return{
        "message": "创建成功",
        "name": user.name,
        "age": user.age
    }

#今天Day2的重点:搞懂：一个HTTP请求进入FastAPI后，到底是怎么找到 Python 函数、拿到数据、处理数据，再返回结果的。
#
# # Day 3｜FastAPI 基础笔记
#
# # 一、FastAPI 是什么？
#
# FastAPI 是一个用于开发 **Web API / HTTP 接口** 的 Python Web 框架。
#
# 最基本的结构：
#
# ```python
# from fastapi import FastAPI
#
# app = FastAPI()
# ```
#
# 这里：
#
# ```python
# app = FastAPI()
# ```
#
# 可以理解为：
#
# > 创建一个 FastAPI 应用对象，后面的路由、接口都注册到这个 `app` 上。
#
# ---
#
# # 二、路由 Route
#
# 路由就是：
#
# > **告诉服务器：收到某种 HTTP 请求以后，应该调用哪个 Python 函数。**
#
# 例如：
#
# ```python
# @app.get("/health")
# def health():
#     return {"status": "ok"}
# ```
#
# 表示：
#
# ```text
# GET /health
#     ↓
# health()
#     ↓
# {"status": "ok"}
# ```
#
# `@app.get("/health")` 不是普通的 Python 装饰器用法那么简单，它是在告诉 FastAPI：
#
# > 如果收到 `GET /health` 请求，就执行 `health()`。
#
# ---
#
# # 三、一个 API 路由由什么决定？
#
# 非常重要：
#
# > **HTTP 方法 + URL 路径 = 一个 API 路由**
#
# 例如：
#
# ```text
# GET  /users
# POST /users
# GET  /users/1
# ```
#
# 虽然前两个路径都是：
#
# ```text
# /users
# ```
#
# 但 HTTP 方法不同，所以是不同接口。
#
# ```python
# @app.get("/users")
# def get_users():
#     ...
#
#
# @app.post("/users")
# def create_user():
#     ...
# ```
#
# 可以理解为：
#
# ```text
# GET /users
#     ↓
# 查询
#
#
# POST /users
#     ↓
# 创建
# ```
#
# ---
#
# # 四、GET 和 POST
#
# ## GET
#
# 通常用于：
#
# > **获取 / 查询数据**
#
# 例如：
#
# ```text
# GET /users
# GET /users/1
# GET /todos
# ```
#
# ---
#
# ## POST
#
# 通常用于：
#
# > **提交数据、创建资源或者执行某个操作**
#
# 例如：
#
# ```text
# POST /users
# POST /chat
# POST /orders
# ```
#
# 以后我们的 Agent API 最常见的就是：
#
# ```text
# POST /chat
# ```
#
# ---
#
# # 五、Path Parameter 路径参数
#
# 例如：
#
# ```python
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {
#         "user_id": user_id
#     }
# ```
#
# 访问：
#
# ```text
# /users/100
# ```
#
# FastAPI 会自动得到：
#
# ```python
# user_id = 100
# ```
#
# 所以：
#
# ```text
# /users/{user_id}
#         ↑
#      动态参数
# ```
#
# 常用于：
#
# ```text
# /users/1
# /products/100
# /orders/2026
# ```
#
# 核心记忆：
#
# > **Path Parameter 是 URL 路径本身的一部分。**
#
# ---
#
# # 六、Query Parameter 查询参数
#
# 例如：
#
# ```text
# /users?user_id=100
# ```
#
# 代码：
#
# ```python
# @app.get("/users")
# def get_user(user_id: int):
#     return {
#         "user_id": user_id
#     }
# ```
#
# 这里：
#
# ```text
# ?user_id=100
# ```
#
# 就是 Query Parameter。
#
# 你 Day 2 已经见过它：
#
# ```python
# params = {
#     "userId": user_id
# }
#
# requests.get(url, params=params)
# ```
#
# 最终就是：
#
# ```text
# /todos?userId=1
# ```
#
# 核心记忆：
#
# > **`?` 后面的参数通常就是 Query Parameter。**
#
# ---
#
# # 七、Path 和 Query 的区别
#
# 一定要分清：
#
# ### Path Parameter
#
# ```text
# /users/100
# ```
#
# 代码：
#
# ```python
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
# ```
#
# ### Query Parameter
#
# ```text
# /users?user_id=100
# ```
#
# 代码：
#
# ```python
# @app.get("/users")
# def get_user(user_id: int):
# ```
#
# 简单记：
#
# ```text
# /users/100
#        ↑
#       Path
#
#
# /users?user_id=100
#         ↑
#        Query
# ```
#
# ---
#
# # 八、Request Body 请求体
#
# POST 请求经常需要向服务器提交数据。
#
# 例如：
#
# ```text
# POST /users
# ```
#
# 请求 Body：
#
# ```json
# {
#     "name": "顺顺",
#     "age": 20
# }
# ```
#
# 这里的：
#
# ```json
# {
#     "name": "顺顺",
#     "age": 20
# }
# ```
#
# 就是 **Request Body**。
#
# 可以理解为：
#
# ```text
# HTTP Request
# │
# ├── Method：POST
# ├── URL：/users
# │
# └── Body：
#     {
#         "name": "顺顺",
#         "age": 20
#     }
# ```
#
# ---
#
# # 九、Pydantic
#
# Pydantic 是 FastAPI 中非常重要的数据验证工具。
#
# 我们可以定义：
#
# ```python
# from pydantic import BaseModel
#
# class UserCreate(BaseModel):
#     name: str
#     age: int
# ```
#
# 这相当于定义了一份：
#
# > **Request Body 数据结构规范**
#
# 要求：
#
# ```text
# name → str
# age  → int
# ```
#
# 然后：
#
# ```python
# @app.post("/users")
# def create_user(user: UserCreate):
#     return {
#         "name": user.name,
#         "age": user.age
#     }
# ```
#
# 客户端发送：
#
# ```json
# {
#     "name": "顺顺",
#     "age": 20
# }
# ```
#
# FastAPI 会：
#
# ```text
# JSON
#  ↓
# Pydantic
#  ↓
# 验证数据
#  ↓
# UserCreate对象
#  ↓
# user
#  ↓
# create_user()
# ```
#
# 所以：
#
# ```python
# user: UserCreate
# ```
#
# 可以理解为：
#
# > 函数接收一个叫 `user` 的参数，这个参数应该符合 `UserCreate` 数据模型。
#
# ---
#
# # 十、Pydantic 的两个核心作用
#
# ### ① 定义数据结构
#
# ```python
# class UserCreate(BaseModel):
#     name: str
#     age: int
# ```
#
# 告诉 FastAPI：
#
# ```text
# 我需要：
# name
# age
# ```
#
# 以及它们的类型。
#
# ### ② 数据验证
#
# 如果发送：
#
# ```json
# {
#     "name": "顺顺",
#     "age": "hello"
# }
# ```
#
# 因为：
#
# ```python
# age: int
# ```
#
# 但是：
#
# ```text
# "hello" ❌
# ```
#
# 不能作为整数。
#
# 所以 FastAPI 返回：
#
# ```text
# 422
# ```
#
# 如果缺少必填字段：
#
# ```json
# {
#     "name": "顺顺"
# }
# ```
#
# 同样会：
#
# ```text
# 422
# ```
#
# 所以：
#
# > **Pydantic = 定义数据结构 + 验证数据**
#
# ---
#
# # 十一、Response 响应
#
# FastAPI 中直接：
#
# ```python
# return {
#     "message": "Hello FastAPI"
# }
# ```
#
# FastAPI 会把 Python 字典转换成 JSON 响应。
#
# 例如：
#
# ```python
# @app.get("/hello")
# def hello():
#     return {
#         "message": "Hello FastAPI"
#     }
# ```
#
# 客户端最终得到：
#
# ```json
# {
#     "message": "Hello FastAPI"
# }
# ```
#
# 所以可以理解：
#
# ```text
# Python dict
#     ↓
# FastAPI
#     ↓
# JSON Response
# ```
#
# ---
#
# # 十二、完整请求生命周期
#
# 这是今天最重要的总结。
#
# 例如：
#
# ```text
# POST /chat
# ```
#
# 客户端发送：
#
# ```json
# {
#     "message": "你好"
# }
# ```
#
# 整个过程：
#
# ```text
# 客户端
#   │
#   │ POST /chat
#   │ Request Body
#   ▼
# FastAPI
#   │
#   │ 路由匹配
#   ▼
# @app.post("/chat")
#   │
#   ▼
# Pydantic
#   │
#   │ 验证 message
#   ▼
# ChatRequest
#   │
#   ▼
# create_chat(chat)
#   │
#   ▼
# 业务逻辑
#   │
#   ▼
# return
#   │
#   ▼
# JSON Response
#   │
#   ▼
# 客户端
# ```
#
# 这条链路一定要记住。
#
# 因为以后 Agent：
#
# ```text
# 用户
#  ↓
# POST /chat
#  ↓
# FastAPI
#  ↓
# Pydantic
#  ↓
# Agent
#  ↓
# LLM
#  ↓
# Tool / RAG
#  ↓
# Agent
#  ↓
# Response
#  ↓
# 用户
# ```
#
# 本质上就是在今天这个基础上继续往里面添加东西。
#
# ---
#
# # 十三、Swagger / `/docs`
#
# 启动 FastAPI 后：
#
# ```text
# http://127.0.0.1:8000/docs
# ```
#
# 可以看到自动生成的 API 文档。
#
# FastAPI 根据你的：
#
# ```python
# @app.post("/chat")
# ```
#
# 以及：
#
# ```python
# class ChatRequest(BaseModel):
#     message: str
# ```
#
# 自动生成接口说明。
#
# 而且可以直接：
#
# ```text
# Try it out
#     ↓
# 输入 JSON
#     ↓
# Execute
#     ↓
# 查看 Response
# ```
#
# 所以 `/docs` 不只是“看文档”。
#
# 开发的时候它也是一个非常方便的：
#
# > **API 调试工具**
#
# ---
#
# # 十四、今天实际写出的 Agent 雏形
#
# 你最后写出的：
#
# ```python
# class ChatRequest(BaseModel):
#     message: str
#
#
# @app.post("/chat")
# def create_chat(chat: ChatRequest):
#     return {
#         "message": chat.message,
#         "reply": "你好，我是你的AI助手"
#     }
# ```
#
# 已经具备了一个 AI 应用 API 的基本形态：
#
# ```text
# POST /chat
#      ↓
# 接收用户消息
#      ↓
# Pydantic验证
#      ↓
# chat.message
#      ↓
# 处理
#      ↓
# 返回回答
# ```
#
# 现在的：
#
# ```python
# "reply": "你好，我是你的AI助手"
# ```
#
# 只是写死的。
#
# 以后我们会把这里换成：
#
# ```text
# chat.message
#       ↓
# LLM
#       ↓
# AI回答
# ```
#
# 再往后：
#
# ```text
# LLM
# ├── Tool
# ├── RAG
# ├── Memory
# └── Agent
# ```
#
# 这就是我们整个 Agent 学习路线逐步搭起来的东西。
#
# ---
#
# ## Day 3 必背/必理解
#
# 如果今天只留下 8 个知识点，我建议你记这几个：
#
# ```text
# 1. FastAPI
#    → Python Web API 框架
#
# 2. 路由
#    → HTTP方法 + URL路径 → Python函数
#
# 3. GET
#    → 通常用于查询数据
#
# 4. POST
#    → 通常用于提交/创建/执行操作
#
# 5. Path Parameter
#    → /users/{user_id}
#
# 6. Query Parameter
#    → /users?user_id=100
#
# 7. Request Body
#    → POST等请求中提交的JSON数据
#
# 8. Pydantic
#    → 定义数据结构 + 数据验证
# ```
#
# 最后把这张图记下来就行：
#
# ```text
#                  FastAPI
#                     │
#               ┌─────┴─────┐
#               │           │
#              GET         POST
#               │           │
#         Path / Query    Body
#                           │
#                       Pydantic
#                           │
#                        Python
#                           │
#                        Response
#                           │
#                          JSON
# ```
#
# **Day 2 完成。**
# 你现在已经从“会调用 API”走到了“会自己提供 API”，这是一个挺关键的台阶。