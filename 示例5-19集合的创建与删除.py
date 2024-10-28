#{}直接创建集合
s={10,20,30,40}
print(s)
#集合只能存储不可变数据类型
#s={[10,20],[30,40]}#TypeError: unhashable type: 'list'

#使用set（）创建集合
s=set()#创建了一个空集合，空集合的布尔值是False
print(s)
#当时直接使用{}创建集合的时候创建的是集合还是字典呢？
s={}
print(s,type(s))#<class 'dict'>
s=set('helloworld')#集合内的元素是无序不重复的
print(s)

s2=set([10,20,30])
print(s2)

s3=set(range(1,10))
print(s3)
#集合是序列的一种，所以序列的大部分操作对于集合而言同样适用
print('max:',max(s3))
print('min:',min(s3))
print('len:',len(s3))

print('9在集合s3中存在吗?',(9 in s3))
print('9在集合s3中不存在吗?',(9 not in s3))

#集合的删除操作
del s3
#print(s3)#print('9在集合s3中存在吗?',(9 in s3))