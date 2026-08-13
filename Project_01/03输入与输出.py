# #获取键盘上输入的数据
# name = input("请输入您的姓名:")
# age = input("请输入您的年龄:")
# print(f"您的名字为{name},您的年龄为{age}")

#案例:
total = 10000
password = input("请输入您的密码")
print("密码正确")
num = int(input("请输入取款金额:"))#要数据类型转换
print(f"成功取款{num}元,您的余额为{total - num}")