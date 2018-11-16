# 不能够rw也就是读取的时候写入
path = "F:\mutil.txt"   # 初步感觉可能是不支持一些特定的类型，比如sql，名称有汉字的就没有感觉到
path1 = "F:\lxxr.txt"
# 读取的方法
info0= open(path)
info1=open(path).read(20) # 字数是不含空格的字数，如果不传入字数，则是全部的内容  读取的方法
# 写入的方法
info2=open(path1,'w').write('我是一个测试文件！！！')  # 重复写入会覆盖之前的文件，所以名字一定要注意，返回的是文件的字符数

# 追加的方法
info3=open(path1,'a').write('追加的内容')  # 返回的是追加的长度,默认也是不会换行的
with open(path1,'a') as e:  # 这种方式会隐式的调用文件的close方法，不过看自己实际应用吧，file.close()好像也不错
    info4 =open(path1,'a')
    info4.write('\n使用with写入')
#  wirteline好像也不是换行写入,所以使用了\n来处理


# info5=open(path1,'r')  这里是不行的，换行没有成功
# info=open(path1).read()

# readline 和writeline
info6=open(path).readline(2)  # 默认取出第一行，如果传入数字，就会认为是要取的字符串个数
info7=open(path).readlines(300)  # 默认取出所有，并且\n换行符也会被输出，如果传入数字，如果字数不足一行的，输出一整行
info=open(path1).read()
print(info)
info0.close()


import  os
'''
try:
    # 文件重命名
    os.rename('F:\lxxr.txt',
              'F:\lpc20180521.txt')  # 该方法没有返回值，看到文件已经修改成功 ，如果没有old_name的文件，就会先创建在进行修改名称（但是当我第二遍执行的时候报错了，这个还有待确认）
    # 删除文件
    os.remove("F:\lpc20180521.txt")  # 删除文件找不到就会报错
    os.removedirs("F:\lx")  # 没猜错应该是删除文件夹，不存在就会报错
except Exception:
    print("文件没找到 ！！！")

# 对文件的内容进行迭代
txtpath='F:\mutil.txt'
sqlpath='E:\zt_cwglksrzl20180416.sql'
sqlinfo=open(sqlpath,'r',encoding='UTF-8')  # 当读取时乱码的时候或者不能读取的时候要对编码进行指定
str=sqlinfo.readline(20)  # 获取到一个字符串
print("要迭代的字符串是》》》",str)
# 将字符串写入文本
file=open("E:\lpc20180521.txt",'w',encoding='utf-8')
fileLength=file.write(str)
file.close()  # 当关闭之后内容才会真实的存储到文件中去，所以在写程序的时候要多注意
ddtxt=open("E:\lpc20180521.txt",'r',encoding='utf-8')
str1=ddtxt.read()
print("内容是%s"%str1)  # 这里应该会存在的问题，就是当程序刚执行了写入之后，实际文件内是没有存储到内容的，应该是需要等关闭的时候才能存储到
print("文件长度是%s,内容是%s"%(fileLength,ddtxt.name))

print(">>>>",str1)  # 当上面读取之后没有关闭，再次读取是空的
str2='hello'
a=0
while str2:  # 返回为空的时候布尔值就会自动为false
    print('读取的字符是》》》', str2)
    str2=ddtxt.read(1)+"\n"
    a=a+1
    if a>=5:
        break
ddtxt.close()

# 使用fileinput实现懒加载方式的迭代
import fileinput
txtpath='F:\mutil.txt'
sqlpath='E:\zt_cwglksrzl20180416.sql'
for line in fileinput.input(txtpath):  # 这个地方不能设置编码，不知道是如何操作sql之类的文件的
    print("使用了fileinput的input方法",line)

file=open(sqlpath,'r',encoding='utf-8')
for line in file:
    print("直接迭代文件对象",line)  # 这样看的话，上面的操作还是不如下面的操作方便

# StringIO函数  直接在内存中进行操作
from io import StringIO  # 新的导入格式

io_str=StringIO()
# 写入
io_str.write("使用StringIO写入的")
# str=io_str.read()# 没有读取到
str=io_str.getvalue() # 这个才可以
print(str)

# 当然也是可以通过while循环的形式来进行获取
io_str1=StringIO("hello\n 我是一个兵 \naaaaa111111")
print(io_str1.getvalue())
while io_str1:
    temp=io_str1.read(1)
    print(">>>>",temp)
    if temp=='':
        break
'''
'''
# 序列化和反序列化

# 使用pickle只能用于Python
import pickle
xiaoding=dict(name='小丁',age=18,lp='范冰冰')
txtpath='F:\小丁.txt'  # 感觉应该是\xiaoding和\x有关系，导致的不能运行
file=open(txtpath,'wb')
pickle.dump(xiaoding,file)  # 数据对象+文件对象
file.close()

# 反序列化在读取出来
filer=open(txtpath,'rb')
print(pickle.load(filer))
filer.close()
'''
