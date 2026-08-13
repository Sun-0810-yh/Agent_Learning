#模块就是一堆类和函数组成的一个文件,例:tools.py

#导入模块
import tools # import 模块名称
from Scripts.pywin32_postinstall import uninstall

#调用模块里面的函数:
tools.fool1() # 模块名.函数名()

#当模块名比较长时 可以将模块起一个别名
import tools as t  #import 模块名称 as 别名

#从模块里导入指定/多个函数
from tools import fool1,fool2  # from 模块名 import 函数名1,函数名2,```

#如果要导入的模块不在同一个目录下
from 目录名.模块名 import fool1,fool2

#将模块里的方法 变量全部导入使用*
from tools import *

fool()#调用函数

from tools import fool1 as f1,fool2 as f2   #多个函数起别名

#__name__  自动读取模块名 特例：如果__name__ == __main__,那它就是主文件也就是当前执行的文件
print('模块名:',__name__) #tools
if __name__ == '__main__':
    #如果是主文件 就执行以下操作

#常用模块
os #操作系统
re #正则
math #数学
datetime #日期

#第三方库
爬虫：
requests
beautifulsoup
scrapy

网站后端：
Django
Flask

桌面软件：
PyQt
PySide
wxPython

# pip命令用来下载第三方库：命令行中输入:
pip install 第三方库的名字
pip uninstall 库name#删除第三方库

#
# 导入包
# 生成包