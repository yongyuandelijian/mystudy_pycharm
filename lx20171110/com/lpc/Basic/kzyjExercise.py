'''
import sys
import sys as xt  # 支持导入包（模块）的重命名
from math import pi as yzl # 导入函数（方法）
print('python的搜索路径是：',sys.path,"\n",xt.path_hooks)
# 序列解包 要求等号两边的数量要相等
x,y,z,=1,2,3 #  ,4 如果后面对应的值过多则提示值太多不能判断,当然两个值的时候也会提示值的个数不够，不能判断
print(x,y,z)
# 上面的步骤也可以等价于如下：
nums=11,22,33
x,y,z=nums
print(x,y,z)
# 链式赋值 将同一个值付给多个变量
x=y=z=10
print(x)

# 增量赋值 ,当然标准运算符都支持，+ - * / %
x+=1
print(x)
# 居然还可以操作字符串
x="hello"
x+="world"  # 当然如果符号选择*这样表面逻辑都过不去的就会报错
x*=2 # 赋值两遍并且拼接
print(x)

# 布尔值 除去0 1 true false这种通用的，元组，列表,字典的有无也可以被bool转为布尔值，虽然有无可以被转为布尔，但是这几种布尔值却不相等
print(bool({}))
# 简单的判断语句，另外就是if支持嵌套，和Java类似就不再介绍
if x=='hello world':
    print("x的值是hello world,小丁很高兴")
elif x=="hello":
    print(x,"的值是hello")
else:
    print(x,"不是hello world，小丁很生气")

# x和y是同一个引用对象，内存指向同一个对象 is ,is not
x=y=1
z=1
if x is y:
    print("x和y是同一个对象")
else:
    if x is z:
        print("x和z是同一个对象")
    else:
        print("x和y还有z都不是一个对象")
z=2
# 如果条件满足，正常执行，如果执行错误，或者条件不满足，则提示后面的参数 断言 assert其实相当于if not这个描述不准确，准确的说是相当于一个try catch如果条件出错就进行一个提示
assert z<0,"太好了，数字大于0"
'''
# while
n = 0
hj = 0
while n <= 100:
    hj += n
    print("本次合计是：%d" % hj)
    n += 1
else:  # 循环结束的时候执行的语句，else属于循环的一部分，所以比之后的代码执行要早
    print("第%d次循环" % n)
print("1到100的和是：%d" % hj)

# for  整个结构类似于Java中的1.7新特性，可以直接取出列表中的元素
mylist = ['aa', 'bb', 'cc']
for i in mylist:
    if i == 'bb':
        break
else:  # 可以看到跳出后else内的语句没有被执行，说明else属于循环的一部分，如果循环跳出，那么直接跳过else的语句块
    print(">>>>当前元素是：%s" % i)

mydic = {"1": "gailun", "2": "debang"}
for myVar in mydic:
    if myVar == '1':
        continue
    print(">>>>字典的值是%s,对应的值是%s" % (myVar, mydic[myVar]))  # 直接取到的是key

# 使用序列解包的方法来解决
for myKey, myValue in mydic.items():
    print("字典的对应键值对是【%s:%s】" % (myKey, myValue))

# 如果需要使用下标,range参数需要数字
number = [1, 2, 3]
name = ["xiaoding", "xiaoqiang", "xiaoli"]
for i in range(len(number)):
    print("%s的学号是：%d" % (name[i], number[i]))

for name, num in zip(name, number):  # 将两个序列返回一个元组的列表
    if num=='2':
        pass # pass用来预留代码段维护代码结构完整
    print(name, "的学号是：", num)

