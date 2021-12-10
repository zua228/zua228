#将二进制数转化为十进制数
def two_to_ten(num):
    total = 0
    num = str(num)
    i = 0
    while i < len(num):
        total += int(num[i]) * 2 ** (len(num) - i - 1)
        i += 1
    return total
# a = int(two_to_ten(1111))
# print(a)
# print(type(a))
