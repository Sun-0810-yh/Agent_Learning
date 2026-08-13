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

