print('-------------老师写的打印倒立直角三角形--------------------')
for i in range(1,6):
    for j in range(1,7-i):
        print('*',end='')
    print()

print('-------------自己写的打印倒立的直角三角形------------------')
i,j=6,0
while i>0:
    i-=1
    while j<i:
        print('*',end='')
        j+=1
    print('')
    j=0

print('-------------自己写的等腰三角形---------------------')
r=eval(input('您想要多少层的等腰直角三角形?'))#总行数
for i in range(1,r+1):
    for j in range(1,2*r):
        if i<r:
            if j<=r-i:
                print(' ', end='')
            elif j<=r+i-1:
                print('*',end='')
        else:
            print('*',end='')
    print('')

print('----------------老师写的等腰三角形------------------------')

for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1,2*i):
        print('*',end='')
    print('')
