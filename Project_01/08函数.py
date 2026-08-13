# def 函数名（参数列表）:
#     函数体

def hello():
    print("Hello World!")
hello()

def max(a,b):
    if a > b:
        return a
    else:
        return b
a = 4
b = 5
print(max(a,b))


# !/usr/bin/python3

# 计算面积函数（函数实例）
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

# !/usr/bin/python3

# 定义函数
def printme(str):
    # 打印任何传入的字符串
    print(str)
    return

# 调用函数（函数可以随时多次调用）
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")


# !/usr/bin/python3

# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)


def change(a):
    a.append(4)

x = [1, 2, 3]
change(x)
print(x)


# 可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return

# 调用 printme 函数，不加参数会报错
printme("  ")❌->printme(" 你好 ")✔

# 关键字参数
# 可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return
# 调用printme函数
printme(str = "菜鸟教程")


#使用关键字参数可以改变参数传递的位置
# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return

# 调用printinfo函数
printinfo(age=50, name="runoob")#这里形参和实参的位置有变化 不影响结果

#默认值参数
def printinfo(name,age = 18):
    print("名字：", name)
    print("年龄：", age)
    return

printinfo(name = "runoob") #名字：runoob 年龄：18
printinfo(age = 20,name="runoob")#名字：runoob 年龄：20

#不定长参数  写在定义函数的参数值用于保存多余的参数值
#语法为：*args 以元组形式保存参数  **kwargs 以字典形式保存参数

# 可写函数说明 *参数名 用法：
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    # print(vartuple)
    #遍历元组后的结果为70 /n 60 /n 50
    for var in vartuple:
        print(var)
    return

# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)#结果：70 /n(60, 50)

#**参数名 用法：
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print(arg1)
    print(vardict)

# 调用printinfo 函数
printinfo(1, a=2, b=3)#结果为：# 1 /n{'a': 2, 'b': 3}

#声明函数时，参数中星号 * 可以单独出现，意思是从 * 后面的参数开始，必须使用关键字参数传递
def f(a,b,*,c):
    return a+b+c
print(f(1,2,c = 3))#f(1,2,3)报错

# “/”前的参数强制使用位置参数，不能变换顺序
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

#匿名函数lambda 语法：lambda a : a的表达式 ==等价于def 函数名(a) return : a的表达式
x = lambda a : a + 10
print(x(5))#15

#以下实例匿名函数设置两个参数：
sum = lambda a,b : a+b
print(sum(10,20))#30

# 我们可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数。
# 以下实例将匿名函数封装在 myfunc 函数中，通过传入不同的参数来创建不同的匿名函数：

def fun(n):
    return lambda a : a*n
doubler = fun(2)#a*2 2为n的传参
tripler = fun(3)
fourlrer = fun(4)

print(doubler(11))#11为a的传参
print(tripler(11))
print(fourlrer(21))#21*4

# 好处就是 可以批量制造不同功能的函数，并写在函数内部 不占用全局变量 可快速调用

# return语句的用法：函数内部负责计算，return负责把计算结果交给函数外部使用。
# 好处:封装结果，把函数内部计算出来的结果，交给调用这个函数的地方。
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total

#调用sum函数
total = sum(10, 20)
print("函数外 : ", total)

#函数递归：指的是函数调用自己本身，逻辑为向下递归 向上返回
def Foo(x):
    if (x==1):
        return 1
    else:
        return x+Foo(x-1)

print(Foo(4))

#程序内部的运行逻辑为：
Foo(4)
 ↓
4 + Foo(3)
        ↓
        3 + Foo(2)
                ↓
                2 + Foo(1)
                        ↓
                        1
                ↑
                2+1=3
        ↑
        3+3=6
↑
4+6=10
# 向下递归（不断调用自己）Foo(4)Foo(3)Foo(2)Foo(1)一直找到出口。
# 向上返回（逐层计算）Foo(1)=1 Foo(2)=3 Foo(3)=6 Foo(4)=10


#常用内置函数
### Python 常用内置函数总结

#### 1. 输入输出
|函数|作用|示例|
|-|-|-|
|`print()`|输出内容|`print("hello")`|
|`input()`|获取用户输入（返回字符串）|`name=input()`|

---

#### 2. 类型转换
|函数|作用|示例|
|-|-|-|
|`int()`|转整数|`int("10")`|
|`float()`|转浮点数|`float("3.14")`|
|`str()`|转字符串|`str(123)`|
|`bool()`|转布尔值|`bool(1)`|
|`list()`|转列表|`list("abc")`|
|`tuple()`|转元组|`tuple([1,2])`|
|`set()`|转集合|`set([1,1,2])`|
|`dict()`|创建字典|`dict(a=1)`|

---

#### 3. 查看对象信息
|函数|作用|
|-|-|
|`type()`|查看对象类型|
|`id()`|查看对象内存标识|
|`isinstance()`|判断对象是否属于某类型|

示例：

isinstance(10, int)

#### 4. 数学计算
|函数|作用|
|-|-|
|`abs()`|绝对值|
|`max()`|最大值|
|`min()`|最小值|
|`sum()`|求和|
|`round()`|四舍五入|

示例：

sum([1,2,3])   # 6

#### 5. 序列操作（列表、字符串常用）
|函数|作用|
|-|-|
|`len()`|获取长度|
|`sorted()`|排序，返回新列表|
|`reversed()`|反转|
|`enumerate()`|同时获取索引和值|
|`zip()`|合并多个序列|

示例：

```python
for i, v in enumerate(["a","b"]):
    print(i,v)
```

---

#### 6. 循环迭代
|函数|作用|
|-|-|
|`range()`|生成数字序列|
|`iter()`|创建迭代器|
|`next()`|获取迭代器下一个值|

示例：

```python
for i in range(5):
    print(i)
```

---

#### 7. 文件操作
|函数|作用|
|-|-|
|`open()`|打开文件|

推荐：

```python
with open("a.txt") as f:
    data=f.read()
```

---

#### 8. 字符编码
|函数|作用|
|-|-|
|`ord()`|字符转数字|
|`chr()`|数字转字符|

示例：

```python
ord('A')  # 65
chr(65)   # A
```

---

### 当前阶段优先掌握：

⭐⭐⭐⭐⭐
`print()`
`type()`
`len()`
`range()`
`enumerate()`
`sorted()`

⭐⭐⭐⭐
`input()`
`isinstance()`
`zip()`
`open()`

⭐⭐⭐
`sum()`
`max()`
`min()`
`id()`
`map()` / `filter()` / `lambda`

