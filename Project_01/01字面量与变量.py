print(100)
print(3.4)
print(True)
print(False)
print(None)
print("Hello world")
#True - 1   False - 0
print(True + 1)
print(False - 1)

# 变量的定义
# 变量名 = 变量值
#Python 是动态类型语言 一个变量可以储存不同数据类型 但是最好一个变量存储一个数据类型

num = 3.1415926
print(num)
num = num + 1
print(num)
num = "ok"
print(num)
num = True
print(num)
num = False
print(num)

base = 20.7
incr = 50
print("未来两个月的播放量为：", base + 2*incr)

#一次性定义多个语句
b,a = 20.7,50
print("未来两个月的播放量为：", b + 2*a)

#变量调换顺序
a = 10
b = 20

c = a
a = b
b = c

print(a)
print(b)

#案例
a,b,c = 100,200,300

d = a
a = c
c = b
b = d

print(a,b,c)