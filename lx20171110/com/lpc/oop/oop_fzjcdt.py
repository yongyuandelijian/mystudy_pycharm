'''
class MyClass(object):
    name ='小丁'  # 这里的name居然在方法中不能使用
    def updateName(self,name):
        if name=='小丁':
            name='小李'
        return name

#  调用
aaa=MyClass()  #  实例化，好处就是不用在定义类型
print(aaa.name)
print(aaa.updateName('小丁'))

# 构造函数,说明语法上是支持两个类在一个文件内的
class myInit():
    def __init__(self):
        print("I am init funcation")

    def ybfun(self):
        print("一般方法，需要初始化后调用")

aaa1=myInit()
aaa1.ybfun()


# 如果构造函数内定义了必须传入参数，那么初始化的时候必须要进行对应的参数
class dcInit(object):
    def __init__(self):
        print("------------------无参数的构造函数------------------")


    def __init__(self,name):   # 初始化的时候自动调用
        name=name+'--你好，欢迎你--'
        print(name)

    def myfun1(self,name): # 只能主动调用
        print("--查看name是否被改变--",name)
# aaa3=dcInit()这样初始化就会报错，如果无参的设置在后面就不会报错了
aaa2=dcInit("xiaohuang")

aaa2.myfun1("xiaohei")


结果：
I am init funcation
一般方法，需要初始化后调用
xiaohuang--你好，欢迎你--
--查看name是否被改变-- xiaohei

上面测试了构造函数的顺序，说明，构造函数，谁在后就执行谁，按照被执行的构造函数来初始化，也就是说可以写多个，但是执行的时候只能按最后的来执行
'''


# 类的访问权限

class Student(object):
    def __init__(self,name,score):
        # self.name=name
        # self.score=score
        # 由于业务实际情况学生的名字和分数是不可以随便修改的，所以我们定义为私有的，只能内部修改
        self.__name=name
        self.__score=score

    def __info(self):  # 可以通过self关键字来获取自身的对象
        if self.__score<60:
            self.__score=60
        print("内部修改%s的成绩是%f"%(self.name,self.__score))

    # get  set 方法名字只能修改  必须是get__attrs这种格式，否则还是会被当作一般函数来使用
    def get__name(self):
        return self.__name

    def get__score(self):
        if 0<=self.__score<=100:
            return self.__score
        else:
            print("分数必须介于0到100之间！！！")
            return -1

    def family(self):
        print("基类不知道有没有女朋友")
# 这个方法，在构造的时候也进行了执行,这个应该是构造内的方法，不能放在外面来写
#    def __setattr__(self, name,score):
#       self.__score=score
#       return self.get__score()
'''
stu=Student("小丁",23)
print("修改前%s的成绩是%f"%(stu.get__name(),stu.get__score()))
# stu.__info()私有方法也是在外部不能进行调用
# stu.score=100
stu.__score=1000 # 这不知道为啥可以修改  print(stu.__score)也可以调用
print("外部修改后%s的成绩是%f"%(stu.get__name(),stu.get__score()))
'''

# 继承 实现代码的复用，可以直接使用父类的方法和参数
class tuhao(Student):
    def family(self):
        return (self.get__name()+"有女朋友！！！")

class diaosi(Student):
    def family(self):
        return (self.get__name()+"是单身狗！！！")

xiaoming=tuhao("小明",18)
xiaoding=diaosi("小丁",24)
# 多态
print("土豪子类的方法",(xiaoming.get__name(),xiaoming.family(),xiaoming.get__score()))
print("屌丝子类的方法",(xiaoding.get__name(),xiaoding.family()))

print("小明是不是学生类型",(isinstance(xiaoming,tuhao)))  # 实例是父类Student的类型也是实例化tuhao类的类型
print("屌丝是不是学生类型",(isinstance(tuhao,Student)))  # 子类tuhao不是父类staudent的类型

print(isinstance(223,int))   # 这个函数非常好，可以校验输入的数据类型


def dt(self,student):
    if 80<student.get__score()<=100:
        print("%s童鞋表现不错"%student.get__name())
    elif 60<student.get__score()<=80:
        print("%s童鞋表现一般"%student.get__name())
    else:
        print("%s童鞋表现较差" % student.get__name())
    return

# 多重继承，就是一个子类可以继承多个父类
class xiaoming(tuhao,Student): # 小明是土豪也是学生，这样小明既有学生学习的方法，也有土豪有女票的方法
    pass
# dt(Student(xiaoming))  事实说明如果在编写的时候每个类混合在一起比较乱，在调用的时候，就会对应的非常麻烦

