import requests

response = requests.get("网站地址")

print(response.status_code)#status_code表示HTTP响应状态码(requests库中的一个属性)
print(response.json())#是 requests 帮你把 HTTP 响应中的 JSON 数据解析成 Python 对象。

# #常见状态码
# 200 → 成功
# 404 → 找不到资源
# 500 → 服务器内部错误
# 401 → 没有认证/身份验证失败
# 403 → 没有权限

import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

print("状态码：", response.status_code)
print("URL：", response.url)
print("响应内容：", response.text)

data = response.json()

print(data)
print(type(data))

print(data["title"])
print(data["completed"])

"https://example.com/search?keyword=Python"
" ?keyword=Python " #表示查询参数

#?keyword=Python == 下面这种params写法
params = {
    "keyword": "Python"
}

response = requests.get(
    "https://httpbin.org/get",
    params=params
)

"?keyword=Python&page=2&limit=10"
"keyword = Python"
"page = 2"
"limit = 10"

#理解get请求:
import requests

params = {
    "userId": 1
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    params=params
)

print(response.url)
print(response.status_code)

data = response.json()

print(data)
print(type(data))
print(len(data))
print(data[0])

#理解post请求
import requests

data = {
    "name": "顺顺",
    "age": 20
}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

print("状态码：",response.status_code)
print("响应内容",response.text)
print("响应类型",type(response.json()))