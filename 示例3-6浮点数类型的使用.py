height=188.5
print(height)
print('height变量的类型为:',type(height))

x=10
y=10.0
print('x的数据类型是:',type(x))
print('y的数据类型是:',type(y))

z=1.99E1413
print('科学计数法:',z,'z的数据类型:',type(z))

print(0.1+0.2)  #不确定的尾数问题   0.30000000000000004
print(round(0.1+0.2,1))     #当然这个不确定尾数问题也不是没有解决方法，只要看不见不就可以了