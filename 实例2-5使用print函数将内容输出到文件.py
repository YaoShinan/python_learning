fp=open('note.txt','w') #打开文件 w->write
print('欢迎使用python',file=fp) #将'欢迎使用pyrhon'输出（写入）到note.txt文件中
fp.close() #关闭文件