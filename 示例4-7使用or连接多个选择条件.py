score=eval(input('请输入您的成绩:'))
if score<0 or score>100:
    print('成绩非法')
else:
    print('您的成绩为:',score)