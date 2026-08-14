from datetime import date

import json

bills = []

def add_bill(bill_type):
    print("当前账单类型：", bill_type)
    amount = float(input("请输入金额:"))
    category = input("请输入消费类型：")
    note = input("请输入备注：")

    bill = {
        "type" : bill_type,
        "amount" : amount,
        "category": category,
        "note" : note,
        "date" : str(date.today())
    }

    bills.append(bill)
    save_bills()
    print("添加成功！")


def save_bills():
    with open("bills.json","w",encoding="utf-8") as file:
        # ! json.dump(要保存的数据, 文件对象)
        json.dump(bills,file,ensure_ascii=False,indent=4)

def load_bills():
    try:
        with open("bills.json", "r",encoding="utf-8") as file:
            bills = json.load(file)
            return bills

    except FileNotFoundError:
        print("文件不存在,创建空文件")
        return []

bills = load_bills()

def show_bills():
    print("== == == 账单 == == ==")
    for bill in bills:

        bill_type = bill["type"]
        amount = bill["amount"]
        symbol = ""
        category = bill["category"]
        note = bill["note"]
        bill_date = bill["date"]

        if bill["type"] == "收入":
            symbol = "+"
        elif bill["type"] == "支出":
            symbol = "-"
        else:
            print("输入无效")

        print(f"{bill_type} {symbol}{amount:.2f} {category} {note} {bill_date}")

def show_balance():
    balance = 0
    for bill in bills :

        if bill["type"] == "收入":
            balance += bill["amount"]

        elif bill["type"] == "支出":
            balance -= bill["amount"]

        else:
            print("输入无效")

    print(f"您当前剩余：{balance:.2f}元")


def show_date():
    search_date = input("请输入日期：年-月-日")
    found = False
    print(f"====== {search_date} 账单 ======")

    for bill in bills:
        symbol = ""

        if bill["type"] == "收入":
            symbol = "+"
        elif bill["type"] == "支出":
            symbol = "-"
        else:
            print("输入无效")

        if bill["date"] == search_date:
            found = True

            bill_type = bill["type"]
            amount = bill["amount"]
            category = bill["category"]
            note = bill["note"]
            bill_date = bill["date"]

            print(f"{bill_type} {symbol}{amount:.2f} {category} {note} {bill_date}")

    if not found:
        print("未找到该日期的信息")



while True:
    print("====== 我的记账本 ======")

    print("1. 添加收入")
    print("2. 添加支出")
    print("3. 查看账单")
    print("4. 查看余额")
    print("5. 按日期查看")
    print("6. 退出")

    choice = int(input("请选择："))

    if choice == 1:
        add_bill("收入")

    elif choice == 2:
        add_bill("支出")

    elif choice == 3:
        show_bills()

    elif choice == 4:
        show_balance()

    elif choice == 5:
        show_date()

    elif choice == 6:
        print("感谢使用，再见")
        break
    else:
        print("错误请重新输入")








