import random

print('''
----------游戏开始----------
''')
n=0
while n<=10:
    n += 1  # 放在这里后面计算次数的时候比较方便，逻辑也比较清楚，建议放在这里
    sysNumber = random.randint(1, 10)
    num_input=input("请输入你猜的1到10内的整数\n") # 默认接收到的是字符串类型
    # print("输入的数字是：",num_input)
    # if not num_input.isdigit(): 不能判断是不是数字，我们判断是不是int
    num_input=int(num_input)
    if not isinstance(num_input,int):
        print("输入的必须是整数,还有%d次机会"%(10-n))
        continue
    elif num_input>10 or num_input<1:
        print("输入的数字必须介于1到10之间的整数，还有%d次机会"%(10-n))
        continue
    elif num_input>sysNumber:
        print("猜大了！小丁很生气，还有%d次机会"%(10-n))
        continue
    elif num_input<sysNumber:
        print("猜小了，小丁很生气,还有%d次机会"%(10-n))
        continue
    elif num_input==sysNumber:  # 按照节省资源的角度这个应该在最前面，如果匹配就会最开始识别到而结束程序
        print("恭喜你，猜对了，小丁很高兴！！！")
        break
    else:
        print("系统的数字是%d你猜测的数字是%d,不知道出什么问题，请联系小丁排查！"%(sysNumber,num_input))
    # n+=1 # 如果这个增加放在开始进来执行，那么10次是包含了=的数字的
    print("十次都猜不对，小丁很生气，拜拜！！！")

