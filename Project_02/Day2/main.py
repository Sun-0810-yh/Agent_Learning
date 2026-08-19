from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/health")
def health():
    return{"status": "ok","message":"服务运行正常"}

@app.get("/hello")
def hello():
    return{"message":"Hello FastAPI"}

@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "message": f"你说的是：{request.message}"
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

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def create_chat(chat: ChatRequest):
    return{
        "message": chat.message,
        "reply": "你好，我是你的AI助手"
    }