#aaa.py文件里 raise 表示抛出异常
from aaa import xxx
#捕获异常结构
try:
    #使用aaa中的xxx
except:#处理异常 后面可继续执行
    #及时处理错误

#aaa.py
def xxx():
    sex = input("请输入性别")
    if sex == "boy":
        print("boy")
    elif sex == "girl":
        print("girl")
    else:
        raise Exception("Invalid")#raise 表示抛出异常
        print("123456")#raise 后 不会被执行

#bbb.py
from aaa import xxx
import sys #python内置库
try:
    xxx()
except:
    print("出错了")
    #raise 继续提交异常
    sys.exit()#让出错的程序马上就停止 就不会执行后面的代码
print("捕获后的代码")


#异常各种类型
try:
    raise Exception("Invalid")
except Exception as e:

Exception #异常错误
ZeroDivisionError #除0错
FileNotFoundError #文件错
TypeError #类型错误
ValueError #值错误
KeyError #字典不存在
IndexError #索引错误

try:
    raise Exception("Invalid")
except ZeroDivisionError as e:#当这个错误被处理 后面的不会再进行处理
    print("除0错")
except Exception as e:#捕获所有异常


try:
    >>>
except Exception as e:
    print("有错误，执行这里处理")
else:#没有错误，执行这里
    print("没有错误，执行这里")
finally:#不管成功或失败，最终都执行这里
    print("不管成功或失败，最终都执行这里")