#项目要求：
# API 查询器 v1

# 运行效果：
# ====== API 查询器 ======
#
# 1. 查询 Todo
# 2. 创建 Todo
# 3. 退出


# 请选择：
# 选择 1：

# 请输入用户ID：1

# 请求成功！
# 请输入用户ID：1

# 请求成功！
# 状态码：200
#
# 找到 10 条 Todo

# 第一条：
# 标题：delectus aut autem
# 完成状态：False

# 选择 2：

# 请输入标题：学习Agent
# 请输入用户ID：1
#
# 创建成功！
# 状态码：201
# 服务器返回：
# {
#     ...
# }


# 这里我们使用：
# https://jsonplaceholder.typicode.com/todos

# 查询参数：
# params = {
#     "userId": 用户输入的ID
# }
# 然后：
# requests.get(...)


import requests

def search_todo():
    user_id = int(input("请输入用户ID:"))
    params = {
        "userId": user_id
    }

    response = requests.get("https://jsonplaceholder.typicode.com/todos",params = params)

    if response.status_code == 200:
        print("请求成功!")
        print("状态码:", response.status_code)
    else:
        print("请求失败")
        print("状态码:", response.status_code)
        return

    data = response.json()
    print(f"找到{len(data)}条Todo")

    print("第一条:")
    print("标题：",data[0]["title"])
    print("完成状态：",data[0]["completed"])

def send_todo():
    title = input("请输入标题：")
    user_id = int(input("请输入用户ID:"))

    data = {
        "title": title,
        "userId": user_id
    }

    response = requests.post("https://jsonplaceholder.typicode.com/todos",json = data)
    if response.status_code == 201:
        print("创建成功!")
        print("状态码:", response.status_code)
    else:
        print("创建失败")
        print("状态码:", response.status_code)
        return

    print("服务器返回：",data)


while True:
    print("====== API 查询器 ======")
    print("1.查询 Todo")
    print("2.创建 Todo")
    print("3.退出")

    choice = int(input("请选择："))

    if choice == 1:
        search_todo()
    elif choice == 2:
        send_todo()
    elif choice == 3:
        print("感谢使用，再见!")
        break
    else:
        print("输入无效,请重新输入")
