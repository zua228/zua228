# 将十进制数转化为二进制数
def ten_to_two(num):
    str1 = ''
    while True:
        a = num % 2
        b = num // 2
        str1 = str1 + str(a)
        num = b
        if b == 0:
            return int(str1[::-1])


c = ten_to_two(12)
print(c)
# print(type(c))
