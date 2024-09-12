sum=0
for i in range(1,101):
    if i%2==1:
        continue
    #累加求和的代码
    else:
        sum+=i
print('1-100之间的偶数和为:',sum)