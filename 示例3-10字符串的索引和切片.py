s='helloworld'
print(s[0],s[-10])  #序号0和序号-10表示的是同一个字符
print('北京欢迎你'[4])       #获取字符串中索引为4
print('北京欢迎你'[-1])      #获取字符串中索引为-1
print('------------------------')
print(s[2:7])       #从2开始到7结束不包含7   正向递增
print(s[-8:-3])     #从-8开始到-3结束不包含-3    反向递减
print(s[:5])        #N默认从0开始
print(s[5:])        #M默认切到字符串结尾
