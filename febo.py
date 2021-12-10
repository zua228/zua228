def func(n):
    if n<=2:
        return 1
    else:
        sum=func(n-1)+func(n-2)
        return sum
a=func(20)
print(a)


func2=lambda x:1 if x<2 else func2(x-1) +func2(x-2)
res=func2(10)
print(res)
