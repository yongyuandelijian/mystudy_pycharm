# 打印99乘法表
wc=0
nc=0
for wc in range(9):
    wc+=1
    for nc in range(wc):
        nc+=1
        # bds="%d*%d=%d"%(wc,nc,wc*nc) 也可以拼接好放进去
        print("%d*%d=%d\t"%(nc,wc,wc*nc),end='')  # end=''使输出不换行
    if nc == wc: # 此处的换行要先让输出之后在换行
        print("外层是%d，内层是%d\n" % (wc, nc))