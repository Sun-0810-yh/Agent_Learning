# type() - - - > 获取字面量或者指定变量的数据类型
print(type(3.14))
print(type(3))
print(type("helloworld"))
print(type(True))
print(type(False))
print(type(None))

num = -10
print(type(num))

#通过  isinstance(数据,类型)  判断是否为指定值,返回bool值 True/False
print(isinstance(num,int))
print(isinstance(num,float))
print(isinstance(num,str))

#字符串
#字符串的三种定义
s1 = "python"#双引号定义方式(不能直接换行)
s2 = 'python'#单引号(不能直接换行)
s3 = """
Hello:
    欢迎大家进入python课程学习!
    记得一键三连哦~
"""#三引号定义多行字符串

print(s1)
print(s2)
print(s3)

print(isinstance(s1,str))
print(isinstance(s2,int))
print(isinstance(s3,float))

#转义字符  (通常用于字符标识符号冲突时)
#常见的转义字符  \'为单引号  \"为双引号 \n换行  \t缩进
s4 = 'It\'s very good'
print(s4)

mg3 = "Hello的意思是\"你好\""
print(mg3)

print("\t欢迎大家进入python课程学习!\n\t记得一键三连哦~")

#字符串的拼接
s1 = "人生苦短" "我用python"
print(s1)

msg1 ="人生苦短"
msg2 = "我用python"
print("宇涵说:" + msg1 + ","+msg2)#通过+号拼接 只能拼接字符串与字符串 非字符串类型要转成字符串类型

#案例:str(int数字)--->将int型转成字符串类型
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "Python java"
message = "大家好,我是"+ name +",今年"+ str(age) + "岁,学习的专业是" + pro +",爱好"+hobby
print(message)
#使用+号来连接字符串的会出现以下三个问题:1\拼接繁琐2\破坏字符串完整性3\类型转换

#字符串格式化
#方式一: %s 占位符
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "Python java"
message = "大家好,我是%s,今年%s岁,学习的专业是%s,爱好%s"%(name,age,pro,hobby)
print(message)

#方式二: f"...{变量/表达式}..."推荐方式
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "Python java"
print(f"大家好,我是{name},今年{age}岁,学习的专业是{pro},爱好{hobby}")