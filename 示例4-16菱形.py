row=eval(input('请输入菱形的行数:'))
while row%2==0:
    print('菱形的行数必须是奇数，请重新输入')
    row=eval(input('请输入菱形的个数:'))
top_row=(row+1)//2
for i in range(1,top_row+1):
    for j in range(1,top_row-i+1):
        print(' ',end='')
    for k in range(1,2*i):
        print('*',end='')
    print('')
bottom_row=row//2
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*bottom_row-2*i+2):
        print('*',end='')
    print('')
