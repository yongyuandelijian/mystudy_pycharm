'''
看视频看到一个while...else感觉很新奇，记录下
逻辑是，while中如果没有执行过break等跳出语句，那么就执行else语句，否则的话就不执行else中的内容
虽然目前没想到有啥用，但是怕别人用，记录下
'''
i=0
while i<5:
    i+=1
    if i==3:
        break # 实际测试发现continue并不算，如果跳出就不执行else语句，不跳出那么就执行语句
    print(i)
else:
    print("程序被推出去了")