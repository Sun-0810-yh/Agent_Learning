# import requests
# url = "https://www.codefather.cn/course/1789189862986850306/section/1789190283176419330"
# headers = {"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"}
# r = requests.get(url, headers=headers)
# print(f"响应状态码：{r.status_code}")


import json

user = {
    "name": "顺顺",
    "age": 20,
    "skills": ["Python", "Agent"]
}

json_text = json.dumps(user, ensure_ascii=False)
data = json.loads(json_text)

print(data)
print(data["name"])
print(json_text)


#实例演示
import json
user = {
    "name" :"John",
    "age" :22,
    "city" : "New York",
    "skills": ["Python", "Agent"]
}

#json.dumps() 把 Python 对象序列化成 JSON 字符串
j = json.dumps(user)
print(j)

#json.loads把 JSON 字符串反序列化成 Python 对象字典的形式保存
p = json.loads(j)
print(p)
print(p["name"])

print(type(user))
print(type(j))
print(type(p))