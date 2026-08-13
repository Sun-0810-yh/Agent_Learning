# # Git基础命令
# git init  #创建项目
# git status  #查看状态
# git add .  #把文件加入暂存区：
# git commit -m "day1: learn http and json" #创建一次版本记录

# #以后修改代码
# git add .
# git commit -m "day1: add api demo"

# .gitignore  # 仓库里哪些文件不受管理
#             # 在根目录下创建.gitignore文件 里面写不被管理的文件名 要是整个目录的话写法为:目录名/
#             # 尽量初始化的时候就创建好

# git reset --hard<comit ID>#把仓库强制回退某个版本提交
# git revert <comit ID>#生成一个反向提交，抵消掉某次的历史提交