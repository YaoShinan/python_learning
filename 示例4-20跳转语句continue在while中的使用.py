s=0
i=1#1。初始化变量
while i<=100:#2.条件判断
    #3.语句块
    if i%2==1:#奇数
        i+=1
        continue#不再执行后面的代码了
    #累加求和的代码
    s+=i
    i+=1
print('1-100之间的偶数之和为:',s)