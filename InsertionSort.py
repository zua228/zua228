def InsertionSort(list: list) -> list:
    """
    简单插入排序，以第一个为基准，从二个开始，每选择一个，将其与前面的一个对比，如果比它小则交换位置，然后再将其与倒数第二个对比，直到集合没有元素
    """
    for i in range(1, len(list)):  # 选择元素i，遍历元素j
        for j in range(i, 1, -1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
    return list


if __name__ == '__main__':
    res = InsertionSort([1, 3, 2, 4, 5])
    print(res)
