# 模拟登录的条件判断
ok_account = "123456"
ok_password = "123456"

account = input("请输入您的账号：")
password = input("请输入您的密码：")

if account == ok_account and password == ok_password:
    print("登陆成功")
    print("欢迎进入B站首页")
else:
    print("账号密码错误，请重新输入：")

#判断闰年
year  = int(input("请输入年份："))
if (year % 100 != 0 and year % 4 == 0) or (year % 400 ==0):
    print(f"{year}年是闰年")
else:
    print(f"{year}年是平年")

#练习1.
num = int(input("请输入数字："))

if num % 2 == 0 :
    print(f"{num}为偶数")
else:
    print(f"{num}为奇数")

age = int(input("请输入您的年龄："))

#2.
if age >= 18 :
    print("该用户已成年")
else:
    print("该用户未成年")

#3.
num = int(input("请输入数字："))
if num > 0 :
    print(f"{num}为正数")
elif num == 0:
    print(f"{num}为0")
else:
    print(f"{num}为负数")

#4.
score = int(input("请输入分数："))

if score >= 60:
    print("及格")
else:
    print("不及格")

#案例
username = input("请输入用户名：")
password = input("请输入密码：")

if username == "admin" and password == "666888":
    print("登录成功")
elif username == "root" and password == "547527":
    print("登录成功")
elif username == "zhangsan" and password == "123456":
    print("登录成功")
else:
    print("登录失败，请重新输入：")

#练习1.
score = int(input("请输入考试成绩："))
if score >= 85:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")

#2.
money = float(input("请输入总金额："))
if money >= 500:
    print(f"{money}元商品，8折，实际应付的金额为：{money * 0.8}元")
elif money >= 300:
    print(f"{money}元商品，9折，实际应付的金额为：{money * 0.9}元")
elif money >= 100:
    print("实际应付的金额为：", money * 0.95, "元")
else:
    print("实际应付的金额为：", money , "元")

#三角形类型判断
a = int(input("请输入第一条边长："))
b = int(input("请输入第二条边长："))
c = int(input("请输入第三条边长："))

if a + b > c and a + c > b and b + c > a:
    if a == b == c :
        print("该三条边构成等边三角形")
    elif a == b or a == c or b == c:
        print("该三条边构成等腰三角形")
    else:
        print("该三条边构成普通三角形")
else:
    print("该三条边不能构成三角形")

#练习1.
usage = int(input("请输入用电量："))

first_max = 2880
second_max = 4800

first_price = 0.4883
second_price = 0.5383
third_price = 0.7883

cost = 0.0

if usage <= first_max:
    cost = usage * first_price
elif usage <= second_max:
    first_cost = first_max * first_price
    second_cost = (usage - first_max)*second_price

    cost = first_cost + second_cost
else:
    first_cost = first_max * first_price
    second_cost = (second_max - first_max) * second_price
    third_cost = (usage - second_max) * third_price

    cost = first_cost + second_cost + third_cost

print(f"{usage}度的电费是: {cost}元")