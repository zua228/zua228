# 十进制数转化为任意进制
def ten_to_any(num, x):
    str1 = ''
    while True:
        a = num % x
        b = num // x
        str1 = str1 + str(a)
        num = b
        if b == 0:
            return int(str1[::-1])

# a = ten_to_any(11, 3)
# print(a)
