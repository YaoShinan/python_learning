import random
lst=[item for item in range(1,11)]
print(lst)

lst=[item*item for item in range(1,11)]
print(lst)

lst=[random.randint(1,100) for _ in range(1,11)] #下划线也好，item也好，只是一个辅助循环的变量罢了，不必过于纠结，就像循环变量用i还是j都行
print(lst)

#从列表当中选择符合条件的元素组成新的列表
lst=[i for i in range(10) if i%2==0]
print(lst)