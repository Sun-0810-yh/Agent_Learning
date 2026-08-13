# """
# match 表达式：
#     case 值1：
#         操作1
#     case 值2 if 条件表达式：#满足条件且值为值2
#         操作2
#     case 值3 | 值4：#匹配值3或4
#         操作4
#     case _:#其他情况
#         默认操作
# """
# #match...case 模式匹配 ： 工作日程安排
# day = input("请输入今天星期几：")
#
# match day:
#     case "1":
#         print("周一：工作会议日")
#     case "2":
#         print("周二：学习培训日")
#     case "3":
#         print("周三：项目开发日")
#     case "4":
#         print("周四：代码审查日")
#     case "5":
#         print("周五：总结规划日")
#     case "6 "| "7":# | 表示或者的意思
#         print("周末：休息放松日")
#     case _ :# _ 表示匹配其他所有的情况
#         print("输入有误！！！")
#
# #案例：简易计算器
# num1 = float(input("请输入第一个数："))
# num2 = float(input("请输入第一个数："))
# oper = input("请输入运算符(+ - * /)：")
#
# match oper:
#     case "+":
#         print (f"{num1} + {num2} = {num1 + num2}")
#     case "-":
#         print (f"{num1} - {num2} = {num1 - num2}")
#     case "*":
#         print (f"{num1} * {num2} = {num1 * num2}")
#     case "/" if num2 != 0:#if条件成立才匹配case
#         print(f"{num1} / {num2} = {num1 / num2}")
#     case _:
#         print("输入有误！！！")
#
#练习：简单游戏指令
oper = input("请输入操作：")

match oper:
    case "上" | "w" | "W":
        print("角色向上移动")
    case "下" | "s" | "S":
        print("角色向下移动")
    case "左" | "a" | "A":
        print("角色向左移动")
    case "右" | "d" | "D":
        print("角色向右移动")
    case "跳" | " ":
        print("角色跳跃")
    case "攻击" | "j" | "J":
        print("角色发动攻击")
    case "退出" | "esc" | "ESC":
        print("角色退出游戏")
    case _:
        print("无操作")
