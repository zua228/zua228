arr = [8, 3, 1, 2, 9, 6, 7]
for i in range(len(arr)):
    for j in range(i,len(arr)):
         if arr[j]<arr[i]:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
    i+=1
print(arr)