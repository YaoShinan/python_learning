t=(i for i in range(1,4))
print(t)
# t=tuple(t)
# print(t)
#遍历
# for i in t:
#     print(i)
#第二种遍历方法，不过这个不断next的过程类似于pop出栈，之后元组对应元素丢失
print(t.__next__())
print(t.__next__())
print(t.__next__())

t=tuple()
print(t)#可见元组已经为空
