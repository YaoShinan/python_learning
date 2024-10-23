#创建字典方式1
d={10:'cat',20:'fog',30:'pet',20:'zoo'}
print(d)#key相同时，后者的value对前者的value进行了覆盖

#创建字典方式2——zip()函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo']
zipobj=zip(lst1,lst2)
print(zipobj)#<zip object at 0x0000024B0091B440>可见这是一个zip对象，无法直接查看其内容
'''
这是一种查看zip内容的方式
print(list(zipobj))#强转的结果为[(10, 'cat'), (20, 'dog'), (30, 'pet'), (40, 'zoo')]，可见这是一个元组
'''
d=dict(zipobj)
print(d)#结果正确：{10: 'cat', 20: 'dog', 30: 'pet', 40: 'zoo'}

#创建字典方式3
d=dict(cat=10,dog=20)#key=cat,value=10
print(d)

#那么哪些值（数据类型）是可以作为key的呢？
t=(10,20,30)
print({t:10})#元组t是key,10是value，可见元组是可以作为key的

lst=[10,20,30]
#print({lst:10})#TypeError: unhashable type: 'list'。可见列表类型变量lst是可变数据类型，不能作为key

#字典也属于序列，所以对于序列的一些基本操作也可对字典经行使用
print('max:',max(d))
print('min:',min(d))
print('len:',len(d))
#字典的删除
del d
print(d)#NameError: name 'd' is not defined