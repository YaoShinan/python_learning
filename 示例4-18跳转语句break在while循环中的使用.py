sum=0#存储累加和
i=1#1.初始化变量
while i<11:#2.条件判断
    #3.语句块
    sum+=i
    if sum>20:
        print('第',i,'轮时sum大于20')
        break
    i+=1#4.改变变量
print('sum=',sum)
print('----------------------------------')
i=0#统计登陆的次数
while i<3:
    user_name=input('请输入用户名:')
    pwd=input('请输入密码:')
    if user_name=='lily' and pwd=='123':
        print('正在登录系统，请稍后')
        break
    else:
        print('用户名或密码输入错误，您还有',2-i,'次机会')
    i+=1
else:print('账号已被锁定，您无权登录')