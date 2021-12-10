for num in range(100000):
    num0 = num
    sum = 0
    print(num)
    while num != 0:
        temp = num % 10
        sum += temp
        num = num // 10
        if num==0:
            break
    sum += num
    print('sum=',sum)
    if sum % 9 == 0:
        if num0 % 9 != 0:
            print('sum1',sum)
            print('各个位数相加和整除9的不一定能被整除')
        else:
            print('sum2',sum)
else:
    print('各个位数相加和整除9的一定能被整除')
