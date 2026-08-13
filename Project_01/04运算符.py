#算数运算符: +加  -减  *乘 /除 //整除 %取余 **幂
print("10 + 4 = ",10 + 4)
print("10 - 4 = ",10 - 4)
print("10 * 4 = ",10 * 4)
print("10 / 4 = ",10 / 4)
print("10 // 4 = ",10 // 4)
print("10 % 4 = ",10 % 4)
print("10 ** 4 = ",10 ** 4)

#算数运算符优先级 ** ---> * / // % ---> + -   特定优先级加()
print("0.1 + 10 / 4 ** 2 = ",0.1+ 10/4 ** 2)

x = float(input("请输入x的值:"))#记得输入的所有数据都是字符串类型的 要转化成需要的数据类型
y = float(input("请输入y的值:"))
#0.9999999998 --->精度损失;由于计算机底层是基于 二进制 进行数据的存储与处理，二进制是无法准确的表示所有的小数，因此涉及到浮点数的运算，可能损失精度
print("x+y的结果是?:",x+y)
print("x+y的结果是?:",x-y)



#赋值运算符:  =   +=   -=   *=   /=   //=   %=   **=
num = 85
num += 10  #num = num + 10
print(num)  #95

num -= 10  #num = num - 10
print(num)  #85

num *= 10  #num = num * 10
print(num)  #850

num /= 10  #num = num / 10
print(num)  #85.0(除法是浮点数)

num //= 10 #num = num // 10
print(num)  #8.0

num %= 3  #num = num % 10
print(num)  #2.0

num **= 3 #num = num ** 10
print(num) #8.0



#比较运算符:   ==   !=   >   >=   <   <= ,返回bool值判断True or False表示表达式成立与不成立
print(100 == 100)#True
print(100 != 100)#False
print(100 > 100)#False
print(100 >= 100)#True
print(100 < 100)#False
print(100 <= 100)#True



#逻辑运算符:  and并且(需要同时成立结果才为True)  or或者(左右两边有一个成立,结果为True,有一个不为True则为False)   not非(取反操作,true为false)
num = int(input("请输入一个整数:"))
print(f"{num}在10-20之间吗?", num >= 10 and num <= 20)

num = int(input("请输入一个整数:"))
print(f"{num}<10或者>20吗?", num <= 10 or num >= 20)







