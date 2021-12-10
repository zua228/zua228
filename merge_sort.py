def merge(a, b):
    _list = []
    l = r = 0
    while l < len(a) and r < len(b):
        if a[l] <= b[r]:
            _list.append(a[l])
            l += 1
        else:
            _list.append(b[r])
            r += 1
    if l == len(a):
        for item in b[r:]:
            _list.append(item)
    else:
        for _item in b[l:]:
            _list.append(_item)
    return _list


def merge_sort(list):
    if len(list) <= 1:
        return list
    pos = len(list) // 2
    left = merge_sort(list[:pos])
    right = merge_sort(list[pos:])
    return merge(left, right)


res = merge_sort([1, 3, 5, 6, 7, 2, 3, 2, 3, 4, 51, 2, 34])


def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = int( len(lists) / 2 )
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)
def Merge(left,right):
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])
    return result
print(MergeSort([1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45]))
