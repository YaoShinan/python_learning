row=eval(input('请输入菱形的层数:'))
while row%2==0:
    print('菱形的层数必须是奇数，请重新输入')
    row=eval('请输入菱形的个数:')
top_row=row//2+1
for i in range(1,top_row+1):
    for j in range(1,top_row-i+1):
        print(' ',end='')
    for k in range(1,2*i):
        if k==1 or k==2*i-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
bottom_row=row//2
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*bottom_row-2*i+2):
        if k==1 or k==2*bottom_row-2*i+1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
