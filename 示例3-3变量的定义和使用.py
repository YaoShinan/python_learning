luck_number=8  #创建一个整型变量luvk_number，并为其赋值为8

my_name='Jack'  #字符串类型的变量

print('luck_number的数据类型是:',type(luck_number))   #<class 'int'>
print(my_name,'的幸运数字是',luck_number)

#pyhton动态修改变量的数据类型，通过赋不同类型的值就可以直接修改
luck_number='今天是2024年7月21号'
print('luck_number的数据类型是',type(luck_number))    #<class 'str'>

#在python中允许多个变量指向同一个值
no=number=1024  #no与number都指向了1024这个整数值
print(no,number)
print(id(no))   #id()函数是用来查看对象的内存地址的
print(id(number))   #验证可知no与number的内存地址相同

'''
变量命名的规则
1，变量名必须是一个有效的标识符
2，变量名不能使用python中的保留字
3，慎用小写字母i和大写字母O（你就说i和1像不像吧，O和0像不像吧）
4，应选择有意义的单词作为变量名

相比之下常量就是在程序运行过程中值不允许改变的量
全部使用大写字母和下划线命名
'''