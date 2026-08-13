import requests

response = requests.get("https://httpbin.org/get")

print(response.status_code)#status_code表示HTTP响应状态码(requests库中的一个属性)
print(response.json())#是 requests 帮你把 HTTP 响应中的 JSON 数据解析成 Python 对象。

# #常见状态码
# 200 → 成功
# 404 → 找不到资源
# 500 → 服务器内部错误
# 401 → 没有认证/身份验证失败
# 403 → 没有权限

import requests
response =  requests.get("https://httpbin.org/get")

print(response.status_code)
print(response.url)
print(response.json())