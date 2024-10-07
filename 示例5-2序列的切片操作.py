s='helloworld'
#切片操作
s1=s[0:5:2]#索引从0开始到5结束。不包括5，步长为2
print(s1)
#省略了开始位置。start默认为0，省略了步长，step默认为1
print(s[:5:])
#省略结束位置，默认结束到结尾
print(s[0::1])
print(s[::])
#可只保留开始
print(s[5::])
print(s[5:])
#不可只保留步长
print(s[::2])#0h  2l  4o  6o  8l
print(s[:2])#0h  1e
#步长为负数
print(s[::-1])#逆序输出
print(s[-1:-11:-1])#17行代码完整版
print(s[::-2])