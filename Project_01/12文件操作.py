from os import write
from pathlib import Path #路径库和类
path = Path("文件名.格式")#实例化函数

contents = path.read_text()#读取文件到内存中是字符串形式

#以下是常见的文件操作方法
print(contents[:10])#切片读取 前十个
contents =contents.replace("5","x")#replace方法：把5替换成x

print(contents)

#查询字符串
if "5" in contents:
    print("yes")
else:
    print("no")

#按行拆分以列表形式储存 多行读取内容
contents = path.read_text().splitlines()
print(contents)

#在不同目录下读取文件
path = Path("./目录名/文件名.格式")#相对路径
path = Path("d:/目录名/文件名.txt")#绝对路径
path = Path(r"d:\目录名\文件名.txt")#r 表示让反斜线不是转义字符



#文件开闭
f = open("文件路径，打开模式")
f.read()/f.write()/f.readlines()/f.writelines()
f.close()#关闭文件对象 释放资源

#文件的打开模式：
r #只读模式 仅读取文件内容
w #写入模式 原内容会被删除 如果文件不存在，会自动创建新文件
a #追加模式 可在文件最后添加新内容 如果文件不存在，会自动创建新文件

    #如果要让文件即可读又可写：
r+ #打开文件用于读写，新内容插行在文件最前面
w+ #打开文件用于读写，文件原有内容被删除
a+ #打开文件用于读写，新内容插行在文件最后面

#常见函数
read() #读取文件内容 返回字符串
write(字符串参数)#写入文件内容
readlines() #返回字符串列表
writelines(字符串列表)

f = open("a.txt","r")
print(f.read())
print(f.readlines())#返回结果是列表形式


f = open("a.txt","w")/f = open("a.txt","a")
print(write())
print(writelines())#写入的参数要是列表形式
f.close()