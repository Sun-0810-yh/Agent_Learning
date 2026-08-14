#类和方法
# 封装 防止全局变量的值影响
class 类名 :
    def __init__(self,形参):
        self.属性名 = 形参 #设置对象属性 值
    def 方法(self,形参):

对象名（变量） = 类名(形参)#实例化对象
#访问控制
对象.属性
对象.方法()

# 以下创建一个学生类，包含各种属性以及访问控制演示：
class Student:
    def __init__(self,a,b,c,d):
        self.name = a
        self.age = b
        self.heigh = c
        self.sex = d

    def listen(self):
        print("听课")

    def study(self):
        print("学习")

#实例化对象
stu1 = Student("张三",18,180,"男")
stu2 = Student("李四",20,175,"女")
stu3 = Student("王五",16,170,"男")

#调用属性及方法
print(stu1.name)
stu2.study()


#私有属性 __变量名
class 类名 :
    def __init__(self,x):
        self.__age = x
        #私有变量不能通过强制赋值修改 self.__age(10) ❌

    def set_age(self,new_age):
        self.__age = new_age#这样就修改x的形参为new_age了

    def get_age(self):
        return self.__age

#只能通过调用方法来修改和访问打印控制✔
对象a.set_age(20)#修改实参
print(对象a.get_age())#打印控制只能通过调用方法

#直接调用对象.属性和方法在私有变量中是无效的❌
对象a = 类名(10)
print(对象a.age)

#继承：子类继父类的属性和方法
class Student:
    def __init__(self,a,b,c,d):
        self.name = a
        self.age = b
        self.height = c
        self.sex = d

    def study(self):
        print("学习")

class BoyStudent(Student):
    #继承父类Student
    def __init__(self,a,b,c,d,e):
        # 假如子类需要添加新的属性 要先用super().__init__(属性名1，属性名2,...)调用父类初始化方法的属性
        super().__init__(a,b,c,d)
        self.weight = e

    def heavy(self):
        print("搬重物")

class GirlStudent(Student):
    def __init__(self,a,b,c,d,f):
        super().__init__(a,b,c,d)
        self.hair_long = f

    def paint(self):
        print("化妆")


Person = Student("张三",18,180,"男")
Boy = BoyStudent("张三",18,180,"男",65)
Girl = GirlStudent("Ailce",17,165,"女",2)

#调用属性及方法
print(Boy.name)
Boy.study()
Boy.heavy()

print(Girl.name)
Girl.paint()


# 案例2
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")

#Python 按照 class sample(speaker, student) 里面写的顺序，从左往右找
#这个查找顺序叫做MRO（Method Resolution Order，方法解析顺序）
test.speak()



#组合：一个对象的属性值是另一个对象
#多态：调用同一个方法 结果不同 。以下案例演示def myMethod()在不同子类下的结果是不同的
#方法重写
class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')

class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')
        #super().myMethod() 强制使用父类方法
        #该函数写法通常表示在子类内部调用父类方法，一般用于子类有特定方法时同时需要父类的方法

c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法 输出：“调用子类方法”
super(Child, c).myMethod()  # 在类的外部调用时 需要告诉函数传递位置和实例对象
                            #(Child, c)表示对C这个实例 从Child类的上边找方法 在继承链中往下找

#运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):#字符串类型的运算符重载
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        #这里告诉python的运算规则是哪两个数字相加
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)#Vector(7,8)

#常见的运算符重载
+       → __add__()
-       → __sub__()
*       → __mul__()
/       → __truediv__()

==      → __eq__()
<       → __lt__()
>       → __gt__()

len()   → __len__()
str()   → __str__()


#！装饰器语法
def 装饰器函数名(function):
    def 内部函数名():
        #在这里添加功能增强的代码 表示在原函数操作前使用
        function()#原函数
        #可以在这里添加更多的行为 表示在原函数操作后使用
    return 内部函数名#必须返回内部函数名

#在原函数调用时语法
@装饰器函数名
def function():
    pass

#本示例说明了装饰器的原理，装饰器参数以及装饰器返回值:
def outer(func):
    def x(*args,**kwargs):#装饰器参数处理 用于原函数传参的时候 装饰器内部函数也要传入值 不然会报错
        # 在执行原函数前出发
        print("准备开始")
        #多个原函数参数用*,**传入  args kwargs只是参数名 不是固定语法
        value = func(*args,**kwargs)# * 用于保存所有多余的位置参数, 保存形式为一个元组
                            # **,用于保存所有多余的关键字参数body = "你好"保存形式为一个字典
        # 在执行原函数前后出发
        print("准备结束")
        return value#装饰器返回值：必须返回保存值 否则x无法接收
    return x

@outer  #装饰器的原理（传入过程）：send_wechat = outer(send_wechat)
def send_wechat(to,body):
    print("微信",to,body)
    # 这里展示原函数需要返回值
    # 根据装饰器原理的逻辑来说：装饰器处理的过程是 在装饰器内部 定义一个容器接收返回值
    # 跳转上述步骤value = func(*args,**kwargs)
    # return value闭环传给函数x   x返回传给函数send_wechat 调用
    return 100


if __name__ == "__main__":
    send_wechat("Alice",body = "你好")


#反射就是让程序在运行过程中，自己“查看、获取、修改对象的信息”，而不需要提前把对象的属性或方法写死。
class Student:
    def __init__(self):
        self.name = "张三"
        self.age = 18

student = Student()

print(student.name)
print(student.age)

#如果以后属性名不是固定的，而是来自用户输入
#不用反射的程序代码：这样就很麻烦，而且属性越多，if 越多
attr = input("请输入要查看的属性：")

if attr == "name":
    print(student.name)
elif attr == "age":
    print(student.age)

#使用反射函数优化的代码：
class Student:
    def __init__(self):
        self.name = "张三"
        self.age = 18

student = Student()

attr = input("请输入要查看的属性：")

print(getattr(student, attr)) #getattr(对象名，"属性名")就是可以通过变量的形式让程序自己查看并获取

#常见的几个反射函数：
getattr()  # 动态获取属性/方法
setattr()  # 动态设置修改属性 setattr(student, "score", 90) == student.score = 90 90为设置的值 setattr()函数的语法
hasattr()  # 动态判断有没有某属性/方法
delattr()  # 动态删除属性


# 需求
#  ↓
# 需要什么数据？
#  ↓
# 数据在哪里？
#  ↓
# 怎么获取？
#  ↓
# 怎么处理？
#  ↓
# 怎么判断？
#  ↓
# 怎么返回？