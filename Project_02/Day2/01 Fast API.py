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

# Day 2 随记 ｜ FastAPI 基础

# 1. FastAPI 是什么
# Python 写 HTTP API 的框架。app 是应用对象，所有路由都挂在它上面。路由 = HTTP方法 + URL路径。

# python
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
# GET /health → health()

# 2. GET vs POST
# GET 取/查数据；POST 提交/新建。同路径不同方法 = 两个不同接口。
#
# python
@app.get("/users")            # 查
def get_users(): return {"users": []}

@app.post("/users")           # 建
def create_user(): return {"message": "创建成功"}

# 3. 路径参数 Path
# URL 路径里的动态值，写在 {} 里。GET /users/100 → user_id = 100

# python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# 4. 查询参数 Query
# ? 后面的参数，函数参数直接接收。GET /users?user_id=100 → user_id = 100。记忆：路径里的动态值=Path；?后面=Query。
#
# python
@app.get("/users")
def get_user(user_id: int):
    return {"user_id": user_id}

# 5. 请求体 Request Body
# POST 一般把数据放在 Body（JSON）里发给服务器。

# json
{"name": "顺顺", "age": 20}

# 6. Pydantic 定义 + 校验
# user: UserCreate 中 user 是参数名，UserCreate 是数据类型。FastAPI 自动把 JSON 校验后塞进 user，直接用 user.name / user.age 取。类型不对或缺字段 → 422。
#
# python
from pydantic import BaseModel
class UserCreate(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: UserCreate):
    return {"name": user.name, "age": user.age}

# 7. 返回 Response
# 直接 return 字典，FastAPI 自动转 JSON 响应。

# 8. /docs 调试
# 启动后访问 http://127.0.0.1:8000/docs，自动生成 Swagger 文档，能直接 Try it out 调接口。

# 9. 完整请求生命周期
# POST /chat → 路由匹配 → Pydantic 校验 → 业务函数 → return → JSON 响应。

# 10. Agent API 雏形
# 现在 reply 写死，以后接 LLM / Tool / RAG / Memory 就变成真正的 Agent。

# python
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def create_chat(chat: ChatRequest):
    return {"message": chat.message,
            "reply": "你好，我是你的AI助手"}
# 核心记法
# FastAPI → 路由(方法+路径) → GET/POST → Path/Query → Body → Pydantic 校验 → 业务逻辑 → Response → /docs 调试