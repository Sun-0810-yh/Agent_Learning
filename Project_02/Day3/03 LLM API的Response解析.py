#假设我们向某个兼容 Chat Completions 格式的 API 发送请求，服务器可能返回类似这样的 JSON：
data = {
    "id": "chatcmpl-123",
    "object": "chat.completion",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "你好！我是一个 AI 助手。"
            },
            "finish_reason": "stop"
        }
    ]
}

print(data.keys())#dict_keys(['id', 'object', 'choices'])
data["choices"]       # 字典
data["choices"][0]    # 列表取第一个元素
data["choices"][0]["message"]       # 字典
data["choices"][0]["message"]["content"]  # 字典中的回答文本

#所以回答是：
answer = data["choices"][0]["message"]["content"]
