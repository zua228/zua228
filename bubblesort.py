# bubble sort


def bubble_sort(x):
    for i in range(len(x), 0, -1):
        for j in range(i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x
# there can add a boolean judge，if a loop has not change, then break out then loop!


if __name__ == '__main__':
    x = [3, 1, 2, 4, 5]
    print(bubble_sort(x))
