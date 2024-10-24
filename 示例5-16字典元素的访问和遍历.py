d={'hello':10,'world':20,'python':30}
#访问字典中的元素
#1.使用d[key]
print(d['hello'])
#2.d.get()
print(d.get('hello'))

#那么这两种访问方式是否有区别呢，是有的：如果key不存在，那么d[key]会报错，而d.get(key)可以指定默认值
#print(d['java'])#KeyError: 'java'
print(d.get('java'))#None
print(d.get('java','不存在'))

for item in d.items():
    print(item)

#在使用for循环遍历时，分别使用key,value
for key,value in d.items():
    print(key,'--->',value)