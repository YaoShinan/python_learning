answer=input('请问您喝酒了吗？')
if answer=='y':
    proof=eval(input('请输入您的酒精度数:'))
    if proof<20:
        print('构不成酒驾，祝您一路平安')
    elif proof<80:
        print('已构成酒驾，请不要开车')
    else:
        print('已构成醉驾，请千万不要开车')
else:
    print('你走吧，没你啥事')