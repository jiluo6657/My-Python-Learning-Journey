import random
import string
while True:
    a=int(input("请输入密码长度"))
    if a<=0:
        print("密码长度有误，请重新输入")
    else:
        b=string.ascii_letters + string.digits
        d=[]
        for i in range(1,a+1):
          c=random.choice(b)
          d.append(c)
        e="".join(d)
        print("生成的密码是",e)
        break
