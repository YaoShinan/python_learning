lst=['hello','world','python']
print('原列表',lst,id(lst))#id()为取值操作，可取出变量的内存地址
#增加元素的操作
lst.append('sql')
print('增加元素之后:',lst,id(lst))#可见增加元素之后lst变量的地址并没有改变，这说明这是一个可变数据类型
#使用insert(index x)在指定的index位置上插入元素x
lst.insert(1,100)
print('在下标为1的位置插入100之后:',lst)
#列表元素的删除操作
lst.remove('world')
print('删除。元素之后的列表:',lst,id(lst))
#使用pop(index)根据索引将元素取出，然后再删除
print(lst.pop(1))
print(lst)
#清除列表中所有的元素clear()
#lst.clear()
#print(lst,id(lst))#可见从头至尾序列lst的地址都未曾变过

#列表的反向
lst.reverse()
print(lst)

#列表的拷贝，将产生一个新的列表对象
new_lst=lst.copy()
print(new_lst,id(new_lst))

#列表元素的修改操作
lst[1]='mysql'
print(lst)