arr = [8, 3, 1, 2, 9, 6, 7]
temp=[]
for j in range(0,len(arr)):
    for i in range(1, len(arr)):
        father = int((i - 1) / 2)
        while i != 0 and arr[i] < arr[father]:
            arr[i], arr[father] = arr[father], arr[i]
            i = father
            father = int((i - 1) / 2)
    temp.append(arr.pop(0))
print(temp)
#O(nlogn)
