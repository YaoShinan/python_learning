#三行四列长方形
for i in range(1,4):#外层循环行
    for j in range(1,5):#内层循环列
        print('*',end='')
    print('')#空的print语句，作用是换行

#输出直角三角形
print('---------------老师写的输出直角三角形--------------')
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()

print('---------------自己写的输出直角三角形--------------')
i,j=0,0
while i<5:
    i+=1
    while j<i:
        print('*',end='')
        j+=1
    print('')
    j=0
