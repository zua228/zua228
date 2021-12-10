from functools import reduce
import pygame
def func1(a, b):
    return a if a > b else b

if __name__ == '__main__':
    list1 = []
    list2 = []
    while True:
        num = input('请输入数字:（输入0表示输入结束）')
        if int(num)==0:
            break
        list1.append(int(num))
        print(list1)
    while True:
        max_num = reduce(func1, list1)
        list1.remove(max_num)  # 不重复的情况下
        list2.append(max_num)
        if len(list1)==0:
            print(list2)
            break
