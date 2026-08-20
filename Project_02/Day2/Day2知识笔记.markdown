# Day 2 随记 ｜ FastAPI 基础

**1. FastAPI 是什么**
Python 写 HTTP API 的框架。`app` 是应用对象，所有路由都挂在它上面。路由 = HTTP方法 + URL路径。
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
# GET /health → health()
```

**2. GET vs POST**
GET 取/查数据；POST 提交/新建。同路径不同方法 = 两个不同接口。
```python
@app.get("/users")            # 查
def get_users(): return {"users": []}

@app.post("/users")           # 建
def create_user(): return {"message": "创建成功"}
```

**3. 路径参数 Path**
URL 路径里的动态值，写在 `{}` 里。GET /users/100 → user_id = 100
```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

**4. 查询参数 Query**
`?` 后面的参数，函数参数直接接收。GET /users?user_id=100 → user_id = 100。记忆：路径里的动态值=Path；`?`后面=Query。
```python
@app.get("/users")
def get_user(user_id: int):
    return {"user_id": user_id}
```

**5. 请求体 Request Body**
POST 一般把数据放在 Body（JSON）里发给服务器。
```json
{"name": "顺顺", "age": 20}
```

**6. Pydantic 定义 + 校验**
`user: UserCreate` 中 user 是参数名，UserCreate 是数据类型。FastAPI 自动把 JSON 校验后塞进 user，直接用 user.name / user.age 取。类型不对或缺字段 → 422。
```python
from pydantic import BaseModel
class UserCreate(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: UserCreate):
    return {"name": user.name, "age": user.age}
```

**7. 返回 Response**
直接 return 字典，FastAPI 自动转 JSON 响应。

**8. /docs 调试**
启动后访问 `http://127.0.0.1:8000/docs`，自动生成 Swagger 文档，能直接 Try it out 调接口。

**9. 完整请求生命周期**
POST /chat → 路由匹配 → Pydantic 校验 → 业务函数 → return → JSON 响应。

**10. Agent API 雏形**
现在 reply 写死，以后接 LLM / Tool / RAG / Memory 就变成真正的 Agent。
```python
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def create_chat(chat: ChatRequest):
    return {"message": chat.message,
            "reply": "你好，我是你的AI助手"}
```

**核心记法**
FastAPI → 路由(方法+路径) → GET/POST → Path/Query → Body → Pydantic 校验 → 业务逻辑 → Response → /docs 调试