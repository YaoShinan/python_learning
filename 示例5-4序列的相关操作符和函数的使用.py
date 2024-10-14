s='helloworld'
print('e在helloworld中存在吗?',('e' in s))#in的使用
print('v在helloworld中存在吗?',('v' in s))
#not in 的使用
print('e在helloworld中不存在吗?',('e' not in s))#in的使用
print('v在helloworld中不存在吗?',('v' not in s))

#序列相关的内置函数的使用
print('len(s):',len(s))
print('max(s):',max(s))#按照ASCII码值排序
print('min(s)',min(s))

#序列对象的方法，使用序列的名称，打点调用
print('s.index(o):',s.index('o'))#o在s中第一次出现的索引位置 4
#print('s.index(v):',s.index(v))#ValueError: substring not found
print('s.count(o)',s.count('o'))#统计o在s中出现的次数