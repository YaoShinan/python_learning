#使用小括号创建元组
tvv=('hello',[10,20,30],'python','world')
print(tvv)

#使用内置函数tuple()创建元组
tuu=tuple('helloworld')
print(tuu)

t=tuple([10,20,30,40])
print(t)
#元组是序列的一种，序列的大部分操作对于元组而言同样适用
print('10在元组t中是否存在:',(10 in t))
print('10在元组t中不存在:',(10 not in t))
print('最大值:',max(t))
print('最小值:',min(t))
print('len(t):',len(t))
print('t,index(10):',t.index(10))
print('t.count:',t.count(10))

#如果元组中只有一个元素
t=(10)
print(t,type(t))
#如果元组中只有一个元素，逗号不能省略
t=(10,)
print(t,type(t))

#元组的删除
del t
#print(t)   #NameError: name 't' is not defined