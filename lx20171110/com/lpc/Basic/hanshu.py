# 函数类似于Java中的方法，或者类，实现一个特定的功能代码段，或者相当与数据库中的函数

help(abs)  # 查看函数的帮助，很好的功能
jdz=abs# 给函数起个别名
print(jdz(-1))

# 定义我的第一个函数,由于python的特性，不需要提前定义参数的类型，这个比sql还要方便一些
def myfunc(str,age):
    "开个小玩笑"  # 函数文档字符串
    str=str+'is a pig'
    age=age*2
    return str,age

def myfunc1(age,str='没名字'):  # 可以看到添加了默认值的参数必须要放在后面，放在没有默认值的参数前面会编译错误
    str=str+'is a pig'
    age=age*2
    return str,age
print("%s是一个半%d的人了"%myfunc1(28)) # 有默认值就可以不传入参数
print("%s是一个半%d的人了"%myfunc('小丁',28))
print("%s是一个半%d的人了"%myfunc(str='小丁',age=28)) # 当然如果记不住顺序可以使用参数名称进行匹配,结果一样的

# 可变参数的函数 通过* 标记变量，传入的时候使用元组即可
def kbfunc(cs1='小红',*cs2):  # 默认参数不能在必须参数之前，但是可以在可变参数之前
    print("不可变参数是：%s"%cs1,"可变参数是：",cs2)
    for kbcs in cs2:
        print("可变参数逐个输出：",kbcs)
    return

kbfunc('小丁','城市','西安','爱好','打游戏','装逼')  # 从输出的情况看，*自动将所有可变参数存储到一个元组内进行输出

# 当然上面的输出不是很合适，如果是字典的话，最好需要成对的输出，我们将上面的参数经过改进之后进行输出
other={'城市':'西安','爱好':'打游戏'}
def kbfunc2(name='小丁',**kbcs):
    print("%s目前的城市是%s,爱好是%s"%(name,other['城市'],other['爱好']))
    return

kbfunc2('小丁',other)