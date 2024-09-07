x=20    #直接赋值，直接将20赋值给左侧的变量x
y=10
x+=y
print(x)
x-=y
print(x)
x*=y
print(x)
x/=y
print(x)
x%=y
print(x)
x=8
x//=3
print(x)
x**=2
print(x)
#python支持链式赋值
a=b=c=d=100
print(a,b,c)
#pyhton支持系列解包赋值
a,b =10,20
print('a=',a,'b=',b)
#用系列解包赋值进行变量数值交换
a,b=b,a
print('a=',a,'b=',b)