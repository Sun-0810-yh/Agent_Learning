# # while 循环 : 打印10遍 "人生苦短, 我用Python~"
#
# i = 0
# while i < 10:
#     print("人生苦短, 我用Python~")
#     i += 1
# else:
#     print("循环正常结束")
#

#while案例 : 计算1-100之间所有偶数的累加之和

sum = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print(f"1-100之间的偶数的累加之和: {sum}")