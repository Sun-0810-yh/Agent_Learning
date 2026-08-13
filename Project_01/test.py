# def Foo(x):
#     if (x==1):
#         return 1
#     else:
#         return x+Foo(x-1)
#
# print(Foo(4))
#
#
class Person:
    def __init__(self,name,relationship):
        self.name = name
        self.relationship = relationship
        self.wife = None
        self.husband = None
        self.lover = None

    def Marry(self,half):
        if self.relationship ==  "丈夫":
            self.wife = half
            half.husband = self
        elif self.relationship == "妻子":
            self.husband = half
            half.wife = self

        print(self.name,"与",half.name,"结婚了")

    def Cheating(self,girl):
        print(self.name,"出轨了",girl.name)

    def catch_3th(self,xiaosan):

        print(self.name,"找小三")
        print("找你们公司陈俊生的姘头")
        print("谁是",xiaosan.name)
        print("我是谁啊?你听好了")
        print("我是",self.relationship)

boy = Person("陈俊生","丈夫")
girl1 = Person("罗子君","妻子")
girl2 = Person("凌玲","小三")
girl3 = Person("薛甄珠","罗子君的妈妈，陈俊生的丈母娘")

boy.wife = girl1
boy.lover = girl2


boy.Marry(girl1)
boy.Cheating(girl2)
girl3.catch_3th(girl2)


# class Employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#
#     def print_info(self):
#         print(self.name,self.id)
#
#
# class FullTimeEmployee(Employee):
#     def __init__(self,name,id,monthly_salary):
#         super().__init__(name,id)
#         self.monthly_salary = monthly_salary
#
#     def calculate_monthly_pay(self):
#         return self.monthly_salary
#
#
# class PartTimeEmployee(Employee):
#     def __init__(self,name,id,daily_salary,work_days):
#         super().__init__(name,id)
#         self.daily_salary = daily_salary
#         self.work_days = work_days
#
#     def calculate_monthly_pay(self):
#         return self.daily_salary * self.work_days
#
# zhangsan = FullTimeEmployee("zhangsan",1,10000)
# lisi = PartTimeEmployee("lisi",2,300,30)
#
# zhangsan.print_info()
# lisi.print_info()
#
# print(zhangsan.calculate_monthly_pay())
# print(lisi.calculate_monthly_pay())
