# set  集合  特点，无序，不重复，如果重复对象传入只保存一份，
# 应用场景，比如记录爬虫访问记录，有重复的就直接不用添加，如果用列表就还需要判断是不是存在，比如前面的购物车链接添加购物清单的时候
# 具体方法看源码即可
# se={"112","323"}  # create
# print(type(se))

# ret =se.pop()  # 这个的移除是随机的，所以不太实用，但是会将移除的结果返回到变量中
# se.discard("112") # 如果移除的元素存在，则移除，不存在则不处理，也不会报错

# list=["112,223"]
# print(list[0].__str__())
# se.add(list[0].__str__())
# se.add(list[1].__str__())
# print(se)

'''
# 练习题
old_dict={
    "1":"223",
    "2":"44",
    "3":"562"
}

new_dict={
    "1":"52",
    "2":"5",
    "5":"92"
}

# 找出在old存在，new不存在的key，进行删除 思路，利用set的diffrent方法找不同key然后利用key去删除
old_keys=old_dict.keys()
new_keys=new_dict.keys()
# print(old_keys,"\t",new_keys)
old_set=set(old_keys)
new_set=set(new_keys)
cy=old_set.difference(new_set)
for i in cy:
    print("要删除的key是",i)
    del(old_dict[i])
    print(old_dict)

# 找出都存在的进行更新，intersection获取交叉的key进行更新
jc=old_set.intersection(new_set)
for i in jc:
    print("现在要更新的key是：",i)
    old_dict[i]=new_dict[i]
    print(old_dict)
# 找出old中不存在，但是new中存在的进行新增
xz=new_set.difference(old_dict)
for i in xz:
    old_dict[i]=new_dict.get(i)
    print(old_dict)
'''

'''
list1=[1,2,4]
list2=[1,3,5]

# s1={"1",list1}
# s2={"2",list2}
# s1.difference(s2)

# 上面声明就会直接报错但是可以这样
set1=set(list1)
print(set1)

# s1={"1","2"}
# s1.add(list1)
'''

# 普通参数，严格按照顺序和类型将实际参数赋值给形式参数
# 默认参数，必须放在参数列表最后
# 指定参数，将实际参数赋值给指定的形式参数

'''
# 函数的动态参数这里，总觉得不是很明确，传入之后如何引用
# 测试说明，传入的参数都当做一个元组来进行处理，
def dtcs(*wew):  # 这里的参数名称不是固定的为args,其他形式也没有报错
    print(type(wew),wew)




list=[1111,"2323",2323]

# 当然这里有个地方要进行说明当我们这种的形式传入，会将传入的列表当做元组的一个元素传入<class 'tuple'> ([1111, '2323', 2323],)
dtcs(list)
# 当以星号附带传入，就是将列表中的元素取出放到元组中 <class 'tuple'> (1111, '2323', 2323),
# 如果传入一个字符串，会将字符串每个字符取出来传入 ,传入str="lipeng" 结果<class 'tuple'> ('l','i','p','e','n','g')
dtcs(*list)


# 当然还有两个星号的动态参数，类型是字典，主要是用来传入多个字典形式的，必须指定键值对比如n1=23
def dtcs2(**kwargs):
    print(type(kwargs),kwargs)

# dtcs2(age=18,name="xiaoding")

# 当然，和上面一样，如果我们希望以键值本身的形式传入<class 'dict'> {'age': 18, 'name': 'xiaoding'}，
# 需要写入星号的形式,否则的话，需要写成上面那种形式
dict1={"age":18,"name":"xiaoding"}
# dtcs2(dict1) # 当然这样是不行的
dtcs2(**dict1)


# 另外就是可以接收任意参数的形式,在这种形式下，会自动判断键值对的参数到两星，单独的值到一星里，另外就是两个星的必须在后面
def wncs(*args,**kwargs):
    print(args)
    print(kwargs)

'''

'''
# 格式化字符串，一种是我们常用的%s %d,这种比较熟悉了，我们记录一下另一中{}占位，形式str.format()
s="我是一个{0}，我今年{1}".format("小丁",12)
print(s)
# 当然也可以有另一种形式
my=["xiaoding",12]
s="我是一个{0}，我今年{1}".format(*my)
# 也可以是下面的形式
s="我是一个{name}，我今年{age}".format(name="xiaobai",age=18)  # 通过参数名称进行的格式化，当然换成字典也和上面的列表一样d
print(s)


# 函数的参数传递的是引用还是一份新的数据对象,结果说明传递的只是一份引用，实际对元数据进行了修改
def lpc(a1):
    a1.append(5555)

list=[1,2,3,4]
lpc(list)
print(list)

# 另外就是要注意函数变量的作用域，作用域越小，级别越高比如
name="lipengchao"
def xuesheng(name):
    name="xiaoding"   #局部变量，自己拥有先使用自己的，没有的话再去全局变量寻找
    # 如果想要修改全局的而不是自己的，重新对全局变量赋值，需要使用关键字global,
    # 不过个人还是喜欢使用传入和return返回，不喜欢这种形式，虽然是复制了一份新的，但是看个人习惯吧
    # global name
    # name="xiaobai"
    print("xuesheng",name)

def xuesheng1():
    # 如果想要修改全局的而不是自己的，重新对全局变量赋值，需要使用关键字global,
    # 不过个人还是喜欢使用传入和return返回，不喜欢这种形式，虽然是复制了一份新的，但是看个人习惯吧
    global name
    name="xiaobai"  # 只能先声明在进行修改
    print("xuesheng1",name)

xuesheng(name)
xuesheng1()
print("外部",name)   # 这里会返回全剧的，函数内的修改并不影响全局的，



# 这里有个问题就是函数返回值的问题
li=[11,33,545]
def fun(li):
    li.append(5443)

li=fun(li) # 但是这一步需要注意，这里将返回值none赋值给li,这样就报错了 'NoneType' object has no attribute 'append'
fun(li)  # 经过处理后 [11, 33, 545, 5443]
print(li)
'''

### 一般情况下，全局变量都设置为大写，局部变量为小写，这样可读性高

'''
# 三元运算 或者成为  三目运算  这样一句话可以替换简单的if else表达式
name="lipengchao" if 1==2 else "xiaoding"
# 虽然和Java的格式不太一样，但是道理一样，条件成立一个值，不成立取else的值，当然如果你不嫌弃麻烦，也可以用if else去写
print(name)

# lambda 一句话用来替换比较简单的(没有方法体可用)函数，比如
def f1(a1):
    return a1+100

print(f1(10))
# 替换成lambda就是
result=lambda a1:a1+100   # 只需要写参数和返回值，其他的都呗替换成关键字lambda,如果有多个参数和返回值用逗号隔开，当然也可以使用默认参数
result1=lambda a1,a2=12:a1+a2
print(result(10))

'''
'''
# 内置函数，这些功能就不用自己再去实现了
abs(-1) # 获取绝对值
# 0或者空的对象转为布尔值都是False,
# all() # 接收一个可以迭代的对象，如果迭代后所有的对象都是真为真，否则为假
list=[1,2,""]
print(all(list))

any(list)  # any也是接收一个可以迭代的对象，只要有一个为真则为真，可以用来判断对象是不是一个空的对象

ejz=bin(23)  # 接收十进制转为二进制    0b10111  ob表示二进制的代称 10111
bjz=oct(23)  # 接收十进制转为八进制    0o27     0o表示八进制
sljz=hex(23) # 接收十进制转为十六进制  0x17     0x 表示十六进制

print(ejz,bjz,sljz)



# bytes用来将字符串转为字节，字节再变成二进制保存在硬盘上，（utf-8一个汉字占用三个字节，gbk一个汉字占用两个字节 每个字节是8位表示）
print(bytes("字节",encoding="utf-8"))  # b'\xe5\xad\x97\xe8\x8a\x82' 转为16进制存储的字节数更少，但是底层需要转为二进制
print(bytes("字节",encoding="gbk"))  # b'\xd7\xd6\xbd\xda'

print(str(bytes("字节",encoding="utf-8"),encoding="utf-8"))  # 字节 再转回来



# callable()  # 判断是否可以被调用，参数传入对象

# 用于转换ascII码和字符
zf=chr(65)  # 将十进制码转为对应的字符A
print(zf)
bm=ord("A") # 将字符转为编码
print(bm)
'''

'''
# 文件操作，打开文件，操作文件，关闭文件
# f=open(file="text",mode="",encoding="")# 我们自己操作默认都使用utf-8如果读入是乱码，可以试试gbk
# f.read() # 也可以传入行号
# f.close()
# 模式：r 只读，w 清空文件后写入，x 当文件存在报错，不存在，创建文件进行写入， a 追加
# f=open(file="text",mode="r",encoding="utf-8")# 我们自己操作默认都使用utf-8如果读入是乱码，可以试试gbk
# f.read() # 也可以传入行号
# f.close()
# 如果模式增加b就是以字符方式操作,比如rb那么Python就不在帮助我们进行转换，那么就需要自己处理字节和字符串转换处理（bytes,str）
# f=open(file="text",mode="wb")# 二进制不需要指定编码
# f.write(bytes("李鹏超",encoding="utf-8")) # 需要指定编码
# f.close()
#
# f=open(file="text",mode="rb")# 二进制不需要指定编码
# data=f.read()
# print(str(data,encoding="utf-8"))
# f.close()


# 如果增加+那就是可读可写
# f=open(file="text",mode="r+",encoding="utf-8")
# # data=f.read(1)  # 读出之后指针会在最后的位置，没有参数读取全部内容，如果有参数，b读取字节，如果没有b按字符读取
# data=f.readline() # 读取当前指针所在的一行数据,对于读取大文件只判断每一行效率上很有好处
# print(data)
#
# # 循环获取文件对象每一行的内容
# for line in f:
#     print(line)
#
# # 写入的时候在指针所在的位置进行写入，如果后面有内容会进行覆盖，覆盖的时候如果是b字节的形式，会每次覆盖一个字符，
# # 如果是字符形式，那么会每次覆盖一个字符的位置,当然这里有一个指定指针位置的方法，
# # 一般都是使用r+ a+无论指定那个位置都会在最后追加，w+会将文件先清空在读写
# f.seek(0) # 传入指针的位置,
# f.truncate() # 清空指针所在位置之后的内容
# f.seekable() # 是否可以引动指针
# print("当前指针的位置在",f.tell())# 获取当前指针的位置
# f.flush()  # 将现在内存的内容保存到硬盘去
# f.readable() # 判断是否可读，返回布尔值
# f.writelines("插入内容")
#
#
#
# print(f.fileno())  # 获取一个文件的数字变现形式，修改后会有变化，可以监控文件是否被修改过
# f.close()

# 通过with操作文件,模块会操作完成自动关闭,2.7之后可以支持读取多个文件，对于需要多个文件内容拼接一个内容,或者转换文件内容比较有效
# 演示的是将第一个文件的内容插入到第二个文件，当然也可以根据需要进行截断
with open(file="text",mode="r",encoding="utf-8") as fr,open(file="text1",mode="w",encoding="utf-8") as fw:
    for line in fr:
        print(line) # 当然这个地方也可以对内容进行处理，比如replace或者split
        fw.write(line)


with open("text","r+",encoding="utf-8") as f:
    for line in f:
        if line.strip().startswith("插入内容") and "4" in line.strip():
            print(line.strip())
            break

    # print(f.tell())
    f.write("\n新增内容\t20181017") # 添加换行
'''

'''
import random
MIN=65
MAX=90  # 这个范围是所有的大写字母

# 随机产生验证码，我们来随机产生四个字母
def scyzm(max,min):
    sjs=random.randrange(min, max)
    zf=chr(sjs)
    print(sjs,zf)
    return zf

yzmlist=[];
for i in range(6):
    if i==random.randrange(1,4):
        sz=random.randrange(0, 10);
        yzmlist.append(str(sz)) # 数字就直接拼接
    else:
        zf=scyzm(MAX, MIN)
        yzmlist.append(zf)
result="".join(yzmlist)
print(result)
# 用于转换ascII码和字符
# zf=chr(126)  # 将十进制码转为对应的字符A
# print(zf)
# bm=ord("A") # 将字符转为编码
# print(bm)
#
s="print(123)"
# 编译,获取一个编译对象,当然也可以传入打开的文件对象，三种模式 single（编译成单行），eval() 编译成一个表达式 ，exec 编译成和Python代码执行一样的东西
r=compile(s,"<string>","exec") # 主要作用就是将字符串编译成Python代码

# 执行Python代码或者字符串，其实exec如果是接收的编译过的就直接执行，如果是接收到字符串，就先编译一下
exec(r)

# eval() 将表达式类型的字符串编译成一个表达式并获取表达式的计算结果，在处理excel的时候很有作用，当然了exec 可以执行所有的Python代码，但是没有返回值，而eval有
s="8*8"
print(eval(s))  # 可以获取返回的结果
# print(exec(r))  # 也可以执行，但是没有返回值，返回值就是两个的重点区别
#
#
# print(dir(dict)) # 传入一个对象，阅览对象提供的方法和功能
help(list)  # 查看对象的帮助信息，其实就是读取了源码的注释，自己也可以去查看源码来获取帮助

# 获取商和余数，比较实用的列子就是分页divmod
n1,n2=divmod(97,10)
print(n1,n2)  # 9 7

s="lipengchao"
print(isinstance(s,str))  # 用来判断对象是不是类型的实例


# filter 参数：1函数  2 可迭代的对象 如果参数1为None，那么就全部为真，返回迭代对象的全部值,
# 功能：对参数2中符合参数1要求的条件数据进行过滤
# 将第二个参数的每一个对象带入到第一个参数中去执行，如果返回真就将当前的循环到的底下那个进行保存，否则就进行抛弃，大致相当于
# result=[];
# for item in 参数2：
#     r=第一个参数（item）;
#     if r:
#         result.append(item)
def f1(a):
    if a>32:
        return True
f2=lambda a:a>32
print(f2(10))

lb1=[11,233,443,2,42,98]  # 尽量不要使用关键字去命名，这样会造成很多不可知的错误
result=filter(lambda a:a>123,lb1)
print(list(result))

# map  对参数二的迭代对象中每个元素做参数一函数中的操作,这样做的作用一般就是代码可以简洁一些，不用去写循环的部分
result=map(lambda a:a+200,lb1)
print(list(result))

# map 是将函数的返回值添加到结果中，filter是将能使函数返回True的循环对象添加到返回结果中

# globals()  所有的全局变量    locals()  存储所有的局部变量
# def f3():
#     a=0;
#     b=0;
#     # print(globals());
#     print(locals())  # {'b': 0, 'a': 0}
#
# f3()

s="李鹏超"
# print(hash(s))   # 作用就是将一个对象转存为一个哈希值，方便存储和查找
# print(id(s))  # 获取内存地址
# issubclass() # 判断一个类是不是另一个类的子类
# print(len(s))  # Python3默认按照字符计算，Python2中默认按照字节计算，而且也只能按照字节计算，3中就可以转换bytes后按字节统计

for i in s:
    print(i);

# max 最大  min 最小  sum 求和

# 次方 两种形式
2**10
pow(2,10)

# 反转
lb1.reverse();

# round 四舍五入
round(2.4)
# zip 将传入的可迭代对象，相同下标的组成一个元组，所有共有下标拼接的元组组成一个列表
# lb1=["xiaoding","18","aihao"];
# lb2=["xiaoxin","18"];
# lb3=["xiaobai","18"];
# 
# re=zip(lb1,lb2,lb3)
# print(list(re)) # [('xiaoding', 'xiaoxin', 'xiaobai'), ('18', '18', '18')]

'''

'''
# json 进行数据的交互和保存，在Python中可以将字符串转换为Python的基本数据类型，如果存在需要引号的地方，必须字符串里是双引号
import json
s1='["名字",233]'
l1=json.loads(s1)
print(l1)
'''

'''
def f1():
    print(123)

def f2(fun):
    fun();

f2(f1)  # 多增加括号，和不增加括号效果一样，只是执行了f1

######################################## 装饰器  主要是用来控制权限的操作 ########################################

# 功能 1 就是在不改变函数内部的情况下，增加外部代码来增加一个额外的功能，在函数的前后都可以新增一些功能
#     2 将装饰函数的返回值重新赋值给被装饰函数
# 形式 @ + 函数名
# 位置： 放在要执行的函数上 会被自动执行,并且会自动将下面的函数当做参数传入

def f4(aaa):
    print("装饰器函数的内部语句") # 装饰函数f4内部的语句
    # 函数名代指整个函数，加上括号，则执行函数
    aaa();  # 如果需要f3原函数，则可以进行执行,所以就是被调用的原函数可以执行也可以不执行，另外前后都可以新增语句
    return "被调用函数的更新后内容";  # 新的f3函数内容


@f4
def f3():
    print("被装饰的函数也就是被调用函数内部的原始语句")

# 如果有返回值的情况下，就不能像上面那样操作

def f5(aaa):
    def f7():
        print("函数前新增的功能")
        # 函数名代指整个函数，加上括号，则执行函数
        f6res=aaa();  # 如果需要f3原函数，则可以进行执行,所以就是被调用的原函数可以执行也可以不执行，另外前后都可以新增语句
        print("函数后新增的功能")
        return f6res
    return f7;  # 新的f6函数内容


@f5
def f6():
    print("被装饰的函数也就是被调用函数内部的原始语句")
    return "原函数的返回值66666666666"

print(type(f6),f6())  # 赋值之后，连被装饰函数f3的属性都变成了装饰函数的返回值


# 原函数在有参数的情况下，
# 问题：开始调用的时候f8是有参数的，但是第二次f8变成了f10之后，是不要参数的
# 其实有这个问题，并不存在，因为在开始调用的时候，其实调用的是f10,f10需要一个一样的参数就可以了

def f9(aaa):
    def f10(name): # 当然如果想要彻底解决参数的问题，可以使用*args,**kwargs
        print("函数前新增的功能")
        res=aaa(name); # 当然如果想要彻底解决参数的问题，可以使用*args,**kwargs
        print("函数后新增的功能")
        return res
    return f10;


@f9
def f8(name):
    print("被装饰的函数也就是被调用函数内部的原始语句",name)
    return "原函数的返回值88888888888"

print(type(f8),f8("xiaoding"))

# 总结上面就是在原始函数不变的基础上，对原函数的功能进行了扩充


import sys
list1 = [{'name': 'xiaoming', 'password': 'xiaoming', 'ye': 500, 'jb': '1', 'zt': '1'}, {'name': 'xiaoding', 'password': '12', 'ye': 300, 'jb': '2', 'zt': '1'}, {'name': 'xiaobai', 'password': '1', 'ye': 100, 'jb': '3', 'zt': '1'}]
namelist=[];
for u in  list1:
    namelist.append(u.get("name"))
    sys.exit(2)

print("xiaoding" in namelist)
'''

'''
# 格式化字符串，个人觉得使用format的方式可读性，易用性都比较好
# 百分号格式的
# 格式化字符串当格式化的时候，字符串中出现了使用%作为占位符的话，如果想要输出一个%字符串，就必须通过%进行转义
# print("我是一个%s,现在输出百分号%%"%"小丁")
# # 如果没有出现，那么就可以只写一个
# print("我是一个小丁,现在输出百分号%")
# # 保留指定小数位数，四舍五入
# print("我是一个小丁,今年的年龄是%.2f"% 23.333333241)

# format格式  语法格式：[fill空白处填充字符[align对齐方式需要width配合[width[,逗号是对位数较多的进行逗号分割[.2小数保留精度[type数据类型]
# s="《{}》年龄《{}》爱好《{}》".format("xiaoding",18,"papapa")  # 里面也可以是空的，按照顺序进行赋值

# yuanzu=("xiaoding",18,"papapa")
# s="《{}》年龄《{}》爱好《{}》".format(*yuanzu) # 这里和传参的时候意思一样，可以将对象内的值对应传入，**也是一样的意思 《xiaoding》年龄《18》爱好《papapa》
# s="《{0[0]}》年龄《{0[1]}》爱好《{0[2]}》".format(yuanzu) # 还支持对传入的参数进行按下标取值

# s="《{0}》,《{0}》《{1}》".format("插入内容1","插入的内容2")  # 首先要说的就是一个引入可以重复去赋值.没有名字，按顺序对应

# s="《{name:s}》《{age:d}》".format(name="xiaoding",age=12) # 当然也可以不指定类型，系统自动判断类型

# s="{:.2%}".format(0.23444)  # 百分号与上面的不同，这里是自动将小数或者整数转为百分比的形式，保留小数位数

# s="《{:s}》年龄《{:d}》考试成绩是《{:.2f}》".format("xiaoding",23,23.333);  # 只指定数据类型，第一个必须是字符，第二个必须是整数，等等

# 也可以转进制,转进制必须是整数，小数是无法转的，后面的值可以比需要的多，但是不会被使用，当然，下面的这种下标方式，用名字也是可以的
# s="《{0:s}》年龄《{1:d}》考试成绩是《{2:.2f}》,成绩的二进制是【{2:b}】，八进制是【{2:o}】，十六进制是【{2:x}】，占平均成绩的《{3:.2%}》".format("xiaoding",23,84,1.23323);
#
# print(s)
'''

'''
# 生成器,主要作用就是在你需要用这个数值的时候才将这个数值加载到内存，不会一次性将所有的数值全部加载到内存中,有yield关键字就是生成器

list1=[11,22,33,4,44];

# res=filter(lambda x:x>22,list1) filter 过滤
# print(res.__str__())

def scq(list1):
    for sj in list1:
        yield sj;

res=scq(list1)  # 没有被使用的时候，获取到一个具有生成数值的对象，这个就是生成器


# 循环将对象内的数据取出来，进入函数将yield关键字后面的数值取出来，可以将数据取出来的就是迭代器，两种形式
# for i in res:
#     print(i)

# 也可以使用这种形式，相当于每次都自己去取出来，不如for循环好用，迭代器的内部实现
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
# print(res.__next__())  # 没有数据会报错
'''

'''
# 递归函数
def func(mingzi):
    mingzi=mingzi*2;
    if len(mingzi)>20:
        return mingzi;
    return func(mingzi);

print(func("xiaoding"))

# 思考题：1*2*3*4*5*6*7
list1=[];
def func(arg):
    print(arg)
    list1.append(arg)
    arg+=1
    if arg>=8:
        return list1
    return func(arg)

print(func(1))
'''

'''
# 导入模块，当然如果要新增目录可以将路径添加到列表中，需要注意的就是，如果前面的路径已经存在和系统重复的名称，会导致导入的包不是你想要的，所以命名要多注意包名不要和系统包名冲突
import sys
for lj in sys.path: # 导入模块的所有路径以及顺序，我们可以看到，是自己的项目路径优先，其次是Python的安装包，然后是第三方安装包
    print(lj)

# 导入的方式  import 模块名  或者 from 模块名 import 函数名  当然都支持as 别名

# 安装第三方包
# 1 pip install 包名  在线
# 2 源码安装：下载源码解压--进入这个目录 Python setup.py install
# 3 使用pycharm方式去处理
# 当然如果有依赖还需要处理依赖

'''

# 序列化,将程序数据类型转为字符串，反序列化，就是将字符串转为程序数据类型
import json
import pickle

# dic1={"1":"1","2":"2","4":"4","5":"5","3":"3"}
# res=json.dumps(dic1);  # 将程序数据类型转为字符串
# print(type(res),res)
# res=json.loads(res) # 反序列化，就是将字符串转为程序数据类型
# print(type(res),res)
'''
import requests
response=requests.get("http://wthrcdn.etouch.cn/weather_mini?city=西安")
response.encoding="utf-8"
# print(type(response.text),response.text)
tq=json.loads(response.text)
tq=tq.get("data")

print("城市：",tq.get("city"))
print("空气指数：",tq.get("aqi"))
print("感冒建议：",tq.get("ganmao"))
print("当前温度：",tq.get("wendu"))
# s1="<![CDATA[<3级]]>"
# print(s1[s1.index("[",6,len(s1))+1:s1.index("]",6,len(s1))])   # 切片包前不包后

wtyb=tq.get("forecast");
print("\n\n下面是五天的天气预报：")
for mt in wtyb:
    fl=mt.get("fengli")
    fl=fl[fl.index("[", 6, len(fl)):fl.index("]", 6, len(fl))+ 1]
    s="日期：{date}\t\t\t{type}\t\t\t最高温度：{high}\t\t\t最低温度：《{low}》\t\t\t风力：{fengli}\t\t\t风向：{fengxiang}"\
        .format(date=mt.get("date"),type=mt.get("type"),high=mt.get("high"),low=mt.get("low"),fengli=fl,fengxiang=mt.get("fengxiang"))
    print(s)

import datetime
xiaoshi=datetime.datetime.now().strftime("%H")
print(xiaoshi,type(xiaoshi))

'''

'''
# 像其他程序传递json的时候，由于其他程序基本都是双引号比较字符串，所以最好是
s1='["122","333","222"]'
print(json.loads(s1))
# 虽然说在Python中双引号在外，或者单引号在外都是正确的,另外相比较dumps和loads,dump=dumps+写入文件  load=读取文件+loads
with open("jsontext20181024","w") as jf:
    dumpres=json.dump(s1,jf)

with open("jsontext20181024","r") as jf:
    loadres=json.load(jf)
    print(loadres)

# pickle 只能Python能操作，不能跨语言，当然也是dumps和loads  ,dump 和load 用法和效果和上面都一样
# 表面上看json更加完美一些，事实上，json只支持Python的基本数据类型适合跨语言去操作，
# 而pickle支持python所有类型，可以对Python类等复杂的对象进行序列化，另外就是Python不同版本也可能会存在不能序列化
'''

# 时间模块常用功能，如果判断时间对象的大小，直接用符号对比就可以了
'''
import time

# tm_wday  0到6 (0是周一)  tm_yday  	1 到 366(儒略历)
# 获取时间戳 从Unix正式上线1970-01-01开始计算的秒数
print("1111",time.time())
# <class 'str'> Thu Oct 25 09:12:18 2018  输出当前时间时间的字符串格式，传入一个时间戳来获取指定时间戳的对应时间
print("2222",type(time.ctime()),time.ctime())
# 以对象的形式输出当前时间的所有属性，传入时间戳的话就是指定时间戳的时间对象,但是这个默认时区有个问题，中国的东八区要差八个小时
print("获取标准时区的时间对象",time.gmtime())
# 获取本地时间对象
print("获取本地时间对象",time.localtime(time.time()))
# 需要时间对象参数,将时间对象转为时间戳
print("33333",time.mktime(time.localtime(time.time())))
# 让程序停止指定的秒数
print("现在我要休息三秒")
time.sleep(3)
print("休息完成")
# 将时间对象转为一个指定的字符串格式
print("将时间对象转为一个指定的字符串格式",time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time())))

# 将字符串按照指定的格式转为时间对象
print("将字符串按照指定的格式转为时间对象",time.strptime("2018-10-25 09-37-46","%Y-%m-%d %H-%M-%S"))


import datetime
# 当前时间 注意两种类型
dqsj1=datetime.datetime.today()
print("当前时间",type(dqsj1),dqsj1)  # 秒后面的单位微秒可以计算程序执行时间
print("当前日期",type(datetime.date.today()),datetime.date.today())
dqsj2=datetime.datetime.now()
print("当前日期",type(dqsj2),dqsj2)
print("时间差异是：",dqsj1-dqsj2)

print(dqsj1.replace(year=2020,month=8))  # 为了跳转到指定的日期，不用复杂的运算，时间对象直接跳转到指定日期，没有指定的属性部分取当前时间的
# 将时间戳转为时间
print(datetime.date.fromtimestamp(time.time()))
print(datetime.datetime.fromtimestamp(time.time()))
# 增加指定的时间，可以点进去看下，timedelta有很多参数可以使用
print(datetime.datetime.now()+datetime.timedelta(weeks=1))
# print(datetime.datetime.now()+10)  直接加就报错了

'''

'''
# 日志模块
# 级别：debug 详细运行日志  info 自己想要记录下，没啥特别的  warning 警告和提醒  error 一般错误 critical 严重错误
# 基本设置,日志的记录文件，记录日志的最低级别，时间格式,测试说明，第一个配置配置过了，后面的配置不起作用
import logging
# 基本设置,日志的记录文件，记录日志的最低级别，时间格式,测试说明，第一个配置配置过了，后面的配置不起作用
logging.basicConfig(filename="/media/lipengchao/study/pycharmproject/lx20171110/jinggao.log",level=logging.WARNING,format="%(asctime)s%(message)s",datefmt="%Y-%m-%d %H:%M:%S")
# logging.basicConfig(filename="/media/lipengchao/study/pycharmproject/lx20171110/test.log",datefmt="%Y-%m-%d %H:%M:%S ") # 不指定级别默认就是警告以上的

# 写入日志的方法
logging.debug("详细运行日志");  # 可以看到默认debug和info是不打印出来的
logging.debug("系统启动了")
logging.info("自己想要记录下，没啥特别的")
logging.warning("警告,不要嘚瑟")
logging.error("一般错误"); # 错误和严重会被打印出来
logging.critical("严重错误"); # 严重，重要



# 如果没有配置文件，那么就打印在屏幕上，否则打印在文件里，如果文件和屏幕都需要输出
# 定义一个写日志的对象
logger=logging.getLogger("lipengchao") # 写日志的对象
logger.setLevel(logging.DEBUG) # 设定一个全局的日志级别,这样的话，debug这些也就记录在里面了
# logger.debug("aaaa李鹏超账户记录的日志") # 记录的和上面一样，没有用户

# 日志输出在哪里的对象 handler
sh=logging.StreamHandler()  # 输出到屏幕的对象
sh.setLevel(logging.WARNING) # 设置屏幕输出的级别，如果没有就使用全局的

fh=logging.FileHandler("/media/lipengchao/study/pycharmproject/lx20171110/wjpmtssc.log");
fh.setLevel(logging.WARNING) # 设置文件输出的级别，如果没有就使用全局的，并且这个级别不能比全局的级别低，否则按全局的级别执行

# 设置每个handler输出的格式# formatter(filename)s，注意文字是s 数字要用d，最有用的就是那个模块的哪一行  module lineno
gszd={"asctime":"时间","name":"用户名","levelname":"日志级别名称","filename":"写日志的文件名称","module":"写日志的模块名称","funcName":"写入日志的函数名称","lineno":"写入日志的代码行号","message":"日志信息","process":"进程号","pathname":"路径名称","processname":"进程名称","thread":"线程id","threadname":"线程名称","":"","":"",};
pmformatter=logging.Formatter\
    ("屏幕日志：(asctime)s-(name)s-(filename)s-(levelname)s-(lineno)d-(funcName)s-(module)s-(message)s");
wjformatter=logging.Formatter("文件日志：(asctime)s-(name)s-(levelname)s-(message)s");

# handle绑定formatter
sh.setFormatter(pmformatter)
fh.setFormatter(wjformatter)

# logger绑定handle
logger.addHandler(sh)
logger.addHandler(fh)

# 使用logger对象进行日志的记录
print("金额：￥%d 元" % 1.6000)
print('%f' % 1.12345678)

'''
# import time
# import datetime
# def pd():
#     pdsj=datetime.strptime("2017-10-18","%Y-%m-%d")
#     kssj=datetime.strptime("1991-01-01","%Y-%m-%d")
#
#     # kssj = datetime.timedelta(1)
#
#
#
# pd()
'''
程序文件说明
bin   执行文件，程序入口
conf  程序配置文件，一些需要用户输入的配置放到这里来获取
modules/core 核心逻辑
log   日志
db    存储数据

'''
# 作业题
'''
# 第一
li=["11","22","33","44"]
print("-".join(li))

# 第二
li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

dict1={"li":li,"tu":tu,"dic":dic};
'''

'''
# 20181109 通过递归完成阶乘  假设从1乘到7

def func(num):
    if num==1:
        return 1
    # print(num) 理解起来不太好理解，主要是在函数返回结果的时候再次调动函数打到函数重复执行的目的
    return num*func(num-1)

print(func(5))
'''


# 反射： 利用字符串去指定模块中操作（查找获取getattr，检查hasattr,删除delattr,增加setattr）指定成员的功能的机制
# 但是这些操作都只是针对内存进行操作，重新加载之后，依旧恢复文件内的内容


'''
import com.lpc.Basic.kztgw3 as gncs

userChoice=input("请输入您需要的函数名称\t\t")
# 如果反射机制找到了对应功能那么就获取功能函数，并执行，否则就提示没找到,输入main()进行测试没有问题
if hasattr(gncs,userChoice):
    fun=getattr(gncs,userChoice)
    fun();
else:
    print("404")
'''

'''
# 不能这样去导入，会导致不认识,这样模块只会截取导入com 如果想要认识这种必须链接属性为true
# str="com.lpc.Basic.kztgw3/main"

str="kztgw3/main"
gnmk,ff=str.split("/")
# 另外包也是可以进行反射的 import sys 等同于  __import__("sys")
gnmk=__import__(gnmk)
if hasattr(gnmk,ff):
    fun = getattr(gnmk, ff)
    fun()
else:
    print("404")
'''
'''
# 如果想要认识这种必须链接属性为true
str="com.lpc.Basic.kztgw3/main"
gnmk,ff=str.split("/")
# 另外包也是可以进行反射的 import sys 等同于  __import__("sys")
gnmk=__import__(gnmk,fromlist=True)  # 如果想要认识这种必须链接属性为true
if hasattr(gnmk,ff):
    fun = getattr(gnmk, ff)
    fun()
else:
    print("404")
'''

'''
# 模块中特殊的变量
import com.lpc.Basic.kztgw3 as drgn

# print(drgn.__doc__)   # 获取被执行的模块顶部三引号的注释，如果没有为None
# print(">>>>>>>>>>>>>>>>>>>",drgn.__cached__) # 被执行的编译的时候pyc字节码文件，没啥用,忘记吧

# print(drgn.__file__)  # 被执行的py文件所在的绝对路径，当然如果在文件所在目录去执行，需要使用os.path.abspath(__file__),os.path.dirname用来获取当前目录的上级目录
# print(drgn.__package__) # 包名com.lpc.Basic

# print(drgn.__dict__)

# print(drgn.__name__)
# 被执行的py文件的名称（含包名），他的特性是等于当前文件的__main__,如果是在其他窗口调用则不等于其他文件的__main__来达到不运行本文件不执行的效果
# if __name__ == '__main__':
#     print("如果是在当前文件下执行，这句话就会被执行，但是如果是将本文件导入其他文件，则不会被执行")

'''


'''
import sys  # 和解释器相关的

print(sys.platform)   # 操作系统平台
print("测试中》》》》》",sys.argv)  # 输出一个第一个元素是当前执行文件路径的列表
print("测试中》》》》》",sys.version) # 解释器版本
print("测试中》》》》》",sys.path)  # 一个解释器相关的路径列表，具体需要的内容自己可以去查看
print("测试中》》》》》",sys.exit(-1))  # 参数状态可以传也可以不传，程序退出



# 重点功能：进度条
def view_bar(i,total):
    rate=i/total
    rate_num=int(rate*100)
    rate_fh=int(rate*100/5)  # 获取到百分比的数字
    bl="\r%s>%d%%"%("="*rate_fh,rate_num)  # \r作用是跳到最前面进行覆盖输出,1一个符号代表两个进度
    sys.stdout.write(bl)
    # 在windows中覆盖刷新正常，但是Linux中看了几个代码效果都一样，不能覆盖,这样看起来倒是不如和shell的样式一样，写成正在处理什么，比例是多少
    sys.stdout.flush()


import time
for i in range(101):
    time.sleep(0.1)
    view_bar(i,100)
'''

# os 模块
import os   # 和系统相关的

# print(os.getcwd()) # 获取当前执行文件的目录
os.chdir("/media/lipengchao/study")  # 没有返回值，用于改变当前目录，相当于cd
# print(os.getcwd())

# print(os.curdir)  # 返回当前目录,一般需要搭配abs使用
# print(os.pardir)  # 返回当前目录的父目录,一般需要搭配abs使用

# os.mkdir("test20181112")  # 创建一个单层目录,如果目录存在就会报错
# os.makedirs("test20181112/lpc/aaa")  # 递归创建目录，如果目录完全存在就会报错
# os.system("touch test20181112/lpc/aaa/lpc.txt")  # 执行一个系统命令
# os.remove("test20181112/lpc/aaa/lpc.txt")  # 删除一个文件，和rm一样，如果为目录则提示错误
# os.removedirs("test20181112/lpc/aaa") # 删除一个目录，如果为空则删除递归到上一个目录,如果上一个也为空，那么也进行删除，如果不为空则提示错误
# os.rmdir("test20181112/lpc/aaa") # 删除一个空目录,这样就删除了aaa,如果aaa不存在，那么就提示错误
# os.rename("test20181112/lpc","test20181112/lpc111")  # 这个重命名大致相当于mv重命名部分的功能,如果要命名的文件不存在，那么就提示错误
# print(os.stat("test20181112/")) # 以元组的方式展示指定目录下的文件信息,大小，时间等等的信息,如果写相对路径，必须以当前目录为相对

# print(os.listdir(os.curdir))  # 以列表的形式列出指定目录下的文件，包含隐藏文件
# print(os.name) # 字符串表示当前使用平台  nt--windows  posix--linux
# print(os.sep) # 获取操作系统的路径分隔符，Linux下为/  windows为\
# print(os.linesep) # 实际测试了都是输出空的，大概就是文档说的Linux下为\t\n  windows为\n 没看出有啥作用
# print(os.pathsep) # 用于分割文件路径的字符串，Linux下为冒号： Windows下为分号；
# print(os.environ) # 以元组内防止字典的形式展示系统环境变量

'''
# os.path下的部分功能
print(os.path.abspath(os.curdir))  # 返回指定目录的绝对路径

# print(os.path.split("test20181112/lpc111/lpc222.txt"))   # 以系统分隔符的形式将路径分割为前面的为一个元素，最后一个分隔符的最后一个路径为一个元素，（目录+文件名，或者是前面目录+最后一个分隔符后的目录）用元组进行展示
# print(os.path.dirname("test20181112/lpc111")) # 返回最后一个系统分隔符前面的部分，最后一个分隔符的后面部分不要，其实就是上面那个分割的第一个元素
# print(os.path.basename("test20181112/lpc111")) # 返回最后一个系统分隔符后面的部分，如果以分隔符结尾则返回空split=（dirname，basename）

print(os.path.exists("test20181112/lpc111/lpc222.txt"))  # 如果目录存在则返回True,测试发现带文件也是可以判断的
print(os.path.isabs("test20181112/lpc111/lpc222.txt"))  # 判断是不是绝对路径
print(os.path.isfile("test20181112/lpc111")) # 判断是不是一个文件，这样为false
print(os.path.isdir("test20181112/lpc111/lpc222.txt"))  # 判断是不是一个目录，这样也是False
print(os.path.join("test20181112/lpc111","test20181112/lpc111/lpc222.txt")) # 有重复的部分就直接拼接了，需要注意，这个函数比字符串的拼接的好处就是自动处理操作系统的路径分隔符
print(os.path.getatime("test20181112/lpc111"))  # 返回指定文件或者路径下的最后【存取】时间
print(os.path.getmtime("test20181112/lpc111"))  # 返回指定文件或者路径下的最后【修改】时间
print(os.path.getsize("test20181112/lpc111/lpc222.txt"))  # 获取指定路径下的总大小

'''

'''
# hues 实现控制台输出彩色

import hues

print(hues.info(11111))
print(hues.success(22222))
'''

'''
# 加密 md5是不可逆的，如果需要判断是否相同只能通过密文进行比较是否一致，另外Python还提供了其他加密方式，一般使用md5
# SHA1、SHA224、SHA256、SHA384、SHA512和MD5算法等

import hashlib
passwd="李鹏超123"
md5key="lipengchao"

md5obj=hashlib.md5(bytes(md5key,encoding='utf-8')) # 创建md5对象,也可以传入一个自己的key,防止有人猜测对应密码,作用是在key的基础上增加密码进行加密
md5obj.update(bytes(passwd,encoding='utf-8'))  # 如果是Python2可以直接对字符串进行加密，但是Python3必须转为字节在进行加密
md5res=md5obj.hexdigest()

# md5res=md5obj.md5(b'12344').hexdigest() 网上也有说这两种方式，不知道是不是没测试好，反正没通过，自己熟悉一种就可以了
# md5res=md5obj.new('md5',b'12344').hexdigest()
print("密码是{passwd},加密后为{md5passwd}".format(passwd=passwd,md5passwd=md5res))
'''

# 正则表达式
import re

'''
2元字符：也就是通配符

. 除换行符之外的任何一个字符
^ 要求以什么开头
$ 要求以什么结尾
× 匹配字符0到多次 和数据库的基本一致
+ 匹配1到多次
？ 匹配0到1次
{3} {1,5}匹配指定的次数，或者指定的次数范围
[bc] b或者c [a-z] a到z之间的字符都可以，但是只代表1个 表示区域内的取值范围都是或的关系 
在中括号里面其他的符号都没有特殊意义，只有三个符号有意义-代表区间 ^ 代表非  
\代表转义取消特殊符号的功能

\d 匹配任何十进制的字符 相当于[0-9]
\D 匹配任何非十进制的字符 相当于[^0-9]

\s 匹配任何空白字符 相当于[\t\n\r\f\v]
\S 匹配任何非空白字符

\w 匹配任何字母数字的字符 相当于[a-zA-Z0-9_] 除了下划线，其他的符号都不包含
\W 匹配任何非字母数字的字符

\b 匹配一个单词边界，也就是指单词和空格的位置,这个貌似不太常见，大概就是/w和/W的交界,所以其他符号也是可以的
'''

'''
str="dfdjkfaadsjladbfladfajaa"
gz1="aa" # 普通字符，这样基本没啥意义，主要是用来匹配通配符
gz2="fd."  # 元字符
gz3="^a"
gz=r"I\b"
print(re.findall(gz,"I-am-a-superman"))  # 以列表的形式展示字符串中所有和给定字符一致的部分
res=re.match("aa","aadfdjkfdsjladfladfajaa") # 参数：规则  待处理的字符串,如果匹配到返回一个对象，如果未匹配到返回None 这个是需要开头就要符合规则，比如aa在结尾是不能匹配的
# 返回的对象有三个方法  <_sre.SRE_Match object; span=(0, 2), match='aa'>
# group() 返回被re匹配的字符串,
# start() 返回匹配开始的位置
# end() 返回匹配结束的位置
# span() 返回刚才两个值的元组
res=re.search("aa",str)
# 找到第一个符合规则的字符串对象，但是不局限于开头，方法还是和上面的对象一样  <_sre.SRE_Match object; span=(19, 21), match='aa'>

# 替换
res=re.sub("a.b","aaa",str,2)  # 将str中符合规则的替换为aaa,最后一个参数可选，表示替换次数，不写就是替换全部
res=re.subn("a.b","aaa",str) # 和上面的不同在于他将替换的总共次数也进行了返回 ('dfdjkfaadsjlaaafladfajaa', 1)
res=re.split("\d+","aaa1bbb2ccc3ddd4")  # 这个函数相当于一个循环去不断的切割符合条件的部分，特殊的就是如果最后是符合条件的分割部分，那么列表的最后一个元素为空
print(res)


# complie 先获取比对规则的对象，然后通过规则去获取匹配结果，这样做的好处就是可以将经常使用的正则表达式编译为一个对象，提高效率
# str="I am a superman !!!"
# regex=re.compile("\S*a\w*")
# res=regex.findall(str)
#
# print(res)

# 转义字符 \  如果需要匹配到一个 \  这样的话需要四个\ 因为Python转义需要两个代表1个，re也需要两个进行代表1个，
# 但是这样的话太复杂，我们使用r前缀来告诉Python后面的内容已经转义过了，这样我们就只需要两个 r"\\"  这样传递进入re就会编译为1个\



# 正则表达式分组  在已经匹配到的数据中进行再次提取
str="23dfdf 232ds !!!"
res=re.match("(?P<name>\d+)(\w+)",str)  # 当然search这些的其他找的规则函数都是一样的，分组的几个方法是根据正则来说的
print(res) # 返回匹配对象
print(res.group())  # 将所有规则匹配到的字符串返回  23dfdf
print(res.groups())  # 将括号内的表达式匹配到的值以元组的形式返回,多个以列表内放置元组的形式返回  ('23', 'dfdf')
print(res.groupdict()) # (?P<name>\d+) 此类格式的表达式中匹配到的值以字典的形式，key为<>中的值，value为匹配到的值，进行返回 {'name': '23'}


# res1=re.findall("(?P<name>\d+)(\w+)",str)
# print(type(res1),res1)  # [('23', 'dfdf'), ('232', 'ds')]
'''