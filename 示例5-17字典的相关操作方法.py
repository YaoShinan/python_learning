d={1001:'lily',1002:'jack',1003:'mike'}
print(d)

#向字典中添加元素
d[1004]='mary'#直接使用赋值运算符向字典中添加元素
print(d)

#获取字典中所有的key
keys=d.keys()
print(keys)
print(list(keys))#dict_keys([1001, 1002, 1003, 1004])
print(tuple(keys))

#获取字典中所有的value
values=d.values()
print(values)#dict_values(['lily', 'jack', 'mike', 'mary'])
print(list(values))
print(tuple(values))

#如何将字典中的数据转成key-value的形式，以元组的方式进行展现
lst=list(d.items())
print(lst)
#可见list与dict其实是一对互逆的过程
d=dict(lst)
print(d)

#使用pop函数
print(d.pop(1001))
print(d)
#倘若我要删除一个不存在的值，阁下又当如何应对
print(d.pop(1008,'不存在'))

#随机删除
print(d.popitem())
print(d)
#清空字典中所有的元素
d.clear()
print(d)
#python当中一切皆对象，每一个对象都有一个布尔值
print(bool(d))#False，可见空字典的布尔值为False