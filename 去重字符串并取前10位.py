def func():
    str1=input('请输入写字符，按回车结束输入')
    output=''
    set1=set()
    for i in str1:
        if i not in set1:
            output=output + i
        set1.add(i)
    print(output[0:10])
result=func()
