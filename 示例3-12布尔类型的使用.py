x=True
print(x)
print(type(x))
print(x+10) #1+10=11,true相当于1
print(False+10) #0+10=10.false相当于0
print('-------------------------------')
print(bool(18)) #测试一下整数18的布尔值
print(bool(0)) #测试一下整数0的布尔值
print(bool(0.0)) #测试一下浮点数0.0的布尔值
#总结：非0整数的布尔值都为True
print(bool('北京欢迎你'))    #True
print(bool('')) #False
#总结：所有非空字符串的布尔值都是True
print(bool(False))  #False
print(bool(None))   #False