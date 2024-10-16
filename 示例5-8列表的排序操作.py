lst=[4,56,78,40,56,89]
print('原列表:',lst)

#排序，默认升序
lst.sort()#排序是在原列表的基础上进行的，不会产生新的列表对象
print('升序:',lst)

#排序，降序
lst.sort(reverse=True)
print('降序:',lst)

print('--------------------------------------')
#其实英文也可以排序
lst2=['banana','apple','Cat','Orange']
print('原列表:',lst2)
#升序排序，先排大写，再排小写（大写的ASCII码值比小写的要大）
lst2.sort()
print(lst2)
#降序排序，先排小写，再排大写
lst2.sort(reverse=True)
print('降序:',lst2)
#忽略大小写经行比较
lst2.sort(key=str.lower)
print(lst2)