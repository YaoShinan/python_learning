lst=['hello','world','python','php']
#for
for item in lst:
    print(item)

#for循环+range()函数+len函数，根据索引进行遍历
for i in range(0,len(lst)):
    print(i,'-->',lst[i])

#第三种遍历方式，使用enumerate（）函数
for index,item in enumerate(lst):
    print(index,item)#index是序号2，不是索引
#手动修改序号的起始值
for index,item in enumerate(lst,start=1):
    print(index,item)
#序列起始值start也可直接省略不写：
for index,item in enumerate(lst,2):
    print(index,item)