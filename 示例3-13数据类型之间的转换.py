x=10
y=3
z=x/y
print(z,type(z))    #隐式转换，通过运算隐式转换了结果的类型

#float类型转成int类型，只保留整数部分
print('float类型转成:',int(3.14))
print('float类型转成:',int(3.9))
print('float类型转成:',int(-3.14))
print('float类型转成:',int(-3.9))

#将int类型转成float类型
print('将int转成float类型:',float(10))
#将str转成int类型
print(int('100')+int('200'))
#字符串转成int或float时报错的情况
#print(int('18a'))   #ValueError: invalid literal for int() with base 10: '18a'
#print(int('3.14'))  #ValueError: invalid literal for int() with base 10: '3.14'   3.14本身不是整数
#print(float('34a.156')) #ValueError: could not convert string to float: '34a.156'

#chr(),ord()是一对操作相反的函数，一个是找到编号对应的字符，一个是找到字符对应的编号
print(ord('杨')) #杨在unicode中对应的整数值
print(chr(26472))#26472整数在unicode表中对应的字符是什么

#进制之间的转换操作，十进制与其他进制之间的转换
print('十进制转成十六进制:',hex(26472))
print('十进制转成八进制:',oct(26472))
print('十进制转成二进制:',bin(26472))