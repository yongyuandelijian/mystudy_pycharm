# 从学习面向对象开始，使用新的学习记录
# 20181114

# 类在定义的时候就会产生新的名称空间，用来存放类的变量名和函数名，可以通过类名.__dict__ 查看
# 类中定义的名字都是类的属性，点是访问属性的语法，类有两种属性，数据属性和函数属性
# 对于经典类来说我们可以通过该字典操作类名称空间的名字，但新式类有限制
class studytest(object):
    shuxing1="aaa"

    # __init__ 构造函数，在类进行初始化也就是创建这个对象的时候执行，可以执行任何代码，但是不允许有返回值
    def __init__(self,name):
        self.shuxing1=name
        print("studytest类的构造方法")

    def chi(self):  # 这里想要使用name可以他自己有，也可以类里有，也可以父类有
        print("%s正在吃。。。"%self.shuxing1)

    def he(self):
        print("%s正在喝。。。"%self.shuxing1)

    def wan(self):
        print("%s正在玩。。。"%self.shuxing1)

# 定义英雄,实例化两个英雄

class yingxiong(studytest):
    # 定义初始化英雄必须拥有的属性
    def __init__(self,nicheng,gongjili,shengmingzhi):
        self.nicheng=nicheng
        self.gongjili=gongjili
        self.shengmingzhi=shengmingzhi
        self.dqsmz=shengmingzhi
        self.wuqi=wuqi(200,1)  # 虽然武器类在后面，但是貌似不影响初始化

    # 定义攻击的方法，每次攻击之后生命值减少100，血量小于0，就拜拜
    def gongji(self,yingxiong):
        yingxiong.dqsmz=yingxiong.dqsmz-self.gongjili-self.wuqi.gongjili
        if yingxiong.dqsmz<0:
            # yingxiong.dqsmz=-1
            print("%s已经被击杀！！！"%yingxiong.nicheng)
        else:
            print("当前生命值是%f百分比为%f" % (yingxiong.dqsmz, yingxiong.dqsmz / yingxiong.shengmingzhi * 100))

        return yingxiong

# 定义两个子类来显示不同的英雄,拥有自己的攻击方式
class zhaoxin_zl(yingxiong):
    # 自己没有定义构造函数的时候，还是会继承父类的的构造，这点和Java不同，所以初始化的时候依旧需要按照父类进行传值
    def gongji(self,yingxiong):
        yingxiong.dqsmz = yingxiong.dqsmz - self.gongjili - self.wuqi.gongjili
        if yingxiong.dqsmz<0:
            # yingxiong.shengmingzhi=-1
            studytest.he(studytest)  # 子类中使用父类的方法
            print("%s已经赵信被击杀！！！"%yingxiong.nicheng)
        else:
            print("当前生命值是%f百分比为%f"%(yingxiong.dqsmz,yingxiong.dqsmz/yingxiong.shengmingzhi*100))


        return yingxiong

class gailun(yingxiong):
    nicheng = "盖伦"

# 代码重用的方式除了继承还有组合，指在一个类中以另一个类作为数据属性，成为类的组合
# 定义武器类，每个英雄可以拥有武器
class wuqi(object):
    def __init__(self,gongjili,zt):
        self.gongjili=gongjili # 武器攻击力
        self.zt=zt # 是否可用


# 使用ABC模块实现抽象类，无法被实例化
import abc
class cxl(metaclass=abc.ABCMeta):
    cxsx="抽象类的属性"

    @abc.abstractmethod
    def read(self):
        "子类必须实现读取的功能"
        pass

    def write(self):
        "子类必须有写入的功能"
        pass
# 实现抽象类
class zl(cxl):
    # 类的数据属性应该是共享的，但是语法上是可以把类的数据属性设置为私有的，访问的时候需要通过_类名__属性名称
    __sx2 = "封装属性"
    # 方法变形
    def __bxfs(self):
        self.__sx2="封装的属性在封装的方法中已经被修改"  # 在类内部可以直接使用定义的形式进行调用，在类外部必须使用变形形式
        print("这是一个封装/变形的方法!!!")
    # 以上两处封装的另一个好处就是不会被子类覆盖

    def read(self):
        print("一次读取一行！！！")

    def write(self):
        print("一次写入一行！！！")

# 同样实现抽象类，但是表现形式不同
import sys
import hashlib
import time

class zl2(cxl):
    def __init__(self,score):
        self.score=score

    # 这种方式对一些属性提供了访问的接口，而且达到了Java内封装的目的，可以设置相应的get和set方法，通常跟self.__属性名称搭配使用
    @property
    def tx(self):
        if self.score<60:
            self.score = 60
            # raise Exception("得分太低，不合法",self.score)  手动提示错误的方法，由于怕影响其他测试结果先注释起来
        return self.score

    # 绑定方法与非绑定方法，  暂时不太懂应用环境，先了解
    # 1 普通没有修饰的方法，都是绑定对象的方法 ，自动将对象作为第一个参数传入
    # 2 绑定类的方法需要classmethod装饰，自动将类作为cls传入
    # 3 非绑定方法 使用staticmethod装饰，谁都可以调用，没有传值的效果
    @classmethod
    def bdl(cls):
        print("绑定类的方法，自动将类传入",cls.read(zl2))  # 输出score提示没有属性，但是方法可以执行，具体还没弄懂
        print("命令行参数是===========================================开始")
        for i in sys.argv:  # 是一个包含命令行参数的列表
            print(i)
        print("命令行参数是===========================================结束")

        print("解释器自动查找所需模块的路径的列表===========================================开始")
        for i in sys.path:  # Python 解释器自动查找所需模块的路径的列表
            print(i)
        print("解释器自动查找所需模块的路径的列表===========================================结束")

        return cls(score=zl2.tx)

    @staticmethod
    def create_id(mima_key):  # 传入一个密码要加的key然后转为md5
        mima=mima_key+str(time.time())
        jm=hashlib.md5(mima.encode('utf-8'))
        return jm.hexdigest()



    def read(self):
        print("一次读取十行！！！")

    def write(self):
        print("一次写入十行！！！")

# 在写入逻辑类的时候，只需要调用父类，展示的地图，传入什么英雄就展示什么英雄
class zhantai():
    def __init__(self,yingxiong):
        print("现在展示的是",yingxiong.nicheng)

# 包装，我们通过继承父类，并对父类进行加工处理，这里我们练习为list的clear方法增加权限控制
class myList(list):
    def __init__(self,item,tag=False):
        super().__init__(item)  # 根据传入的对象进行创建列表
        self.tag=tag  # 是否可以删除的状态


    def clear(self):
        if not self.tag:
            raise Exception("你不能清除列表，此事件将被报告")
        else:
            super().clear()

# 描述符,包含一下三个方法中的一个或者多个的新式类就叫做描述符,并且分为两种, 总的来说,感觉有点像是Java中的实体类,用来描述数据的
# 一种是至少实现了__get__() 和__set__()称为数据描述符,
# 如果没有实现__set__()就称为非数据描述符
class msf:  # 这个位置在Python3中不加括号msf和加括号msf()以及继承object msf(object)都是一样的

    # shuxing="xiaoding"

    def __get__(self, instance, owner):
        # getmsf="aaa" 也不是理解的这样
        print("get在执行中。。。。")

    def __set__(self, instance, value):
        print("set在执行中。。。。")

    def __delete__(self, instance):
        print("delete在执行中。。。。")

class dymsf():

    shuxing=msf()   # 将描述符定义为类的属性,虽然描述符本身是一个类,但是不能将他只能以这种方式被调用,而不是我们开始理解的那样



if __name__ == '__main__':
    '''
    
    
    1 下面的这样理解是错误的
    例子由于类的属性中包含,所以不会触发描述符,如果调用类中没有的额就会触发
    msf.shuxing # 调用属性,出发get
    print("get之后的描述符",msf.shuxing)
    msf.shuxing="小李" # 设置属性,出发set
    print("set之后的描述符", msf.shuxing)
    del msf.shuxing  # 删除属性,触发delete
    print("del之后的描述符", msf.shuxing)
    
    2 这样理解也不对
    msf.getmsf
    

    3 这样理解也不对
    m1=msf()
    m1.name="aaa"  # 描述符的对象在执行对象操作的时候不会触发一下三个类
    '''
    dymsf.shuxing  # 这个时候就触发了get

    # 这样不会触发上面的描述符输出,可能会误认为描述符对类不起作用,实际上并不是这样,而是因为优先级的问题
    # 1 类属性
    # 2 数据描述符
    # 3 实例属性
    # 4 非数据描述符
    # 5 找到属性触发AttributeError
    dymsf.shuxing='bbb'  # 这样会覆盖掉原来的描述符,这样描述符就没用了
    del dymsf.shuxing  # 这样会删除原来的描述符,描述符也就不起作用了,

    # 总结,这个位置吧,其实单独说下描述符也没有错误,但是这应该是一种高层次的东西,放在初学的话还是不容易理解,开始还是不去看的好,这基本等同于Java中一个类充当另一个类属性的形式差不多,

    c1=dymsf()
    c1.shuxing
    c1.shuxing='aaa'
    del c1.shuxing






    '''
    # 多态
    c1=zl()
    c1.read()

    c2=zl2(20)
    c2.read()

    # 内置方法
    print(isinstance(c2,cxl))  # 判断参数1是不是参数2的对象
    print(issubclass(zl2,cxl))  # 判断参数1是不是参数2的子类  c2,cxl  c2,zl2 对象不是类的子类,zl2,cxl必须是类名

    # 反射 就是可以根据字符串操作对象相关属性的机制

    # 1 判断参数1中有没有参数2这个属性和方法
    print("判断是否有字符串形式的方法或者属性",hasattr(zl2,"read1"))

    # 2 获取参数2字符串形式的对象
    myid=getattr(zl2,"create_id")
    print(myid("111"))  # 获取到对象加括号执行初始化

    # 3 修改对象
    # setattr(zl2,"create_id","修改对象为新的数据")
    # print("修改后的对象值为",c2.create_id)  # 原先的方法已经被覆盖为一个字符串了

    # delattr(zl2,"create_id")
    # print(c2.create_id()) # 删除后在执行，已经提示不存在




    # 特性property装饰后，可以像访问属性的方式访问方法
    print(c2.tx)
    # 绑定类的方法
    v1=zl2.bdl()
    print("绑定类的方法返回。。。",v1)  # 直接返回类，就可以调用类内部的情况

    # 非绑定的方法,利用md5创建id
    curid=c2.create_id("李鹏超的密码")
    print("非绑定的方法",curid)



    # 抽象类，在Python中也包含接口的概念
    print(c1.cxsx)  # 可以看出抽象类的属性不是强制要有的

    # 封装 如果是在定义类的内部就可以直接使用
    print("封装（变形）后的类的属性是",c1._zl__sx2)  # 通过 实例名._类名__属性名
    c1._zl__bxfs()  # 通过这种形式来访问变形/封装的方法，这种形式就是没有自动提示，在一定程度上具有安全效果

    # 在写这一块代码的时候，有个问题，要把类的继承和方法的参数区分开，继承的不要当成参数，只需要处理好方法内要求的参数即可
    gl=gailun("盖伦",100,600)
    zt=zhantai(gl)  # 定义的时候传入父类，引用的时候传入子类

    l1=[1,2,34,5,3]
    ml=myList(l1)
    # ml.clear()
    print("111111111111111",ml)

    exec('print("22222222222222222222执行字符串形式的Python语句")')
    
    # 实例化两个英雄
    gailun=yingxiong("盖伦",100,600)
    zhaoxin=yingxiong("赵信",120,500)

    zx=zhaoxin_zl("赵信",120,500)

    zx.gongji(gailun)
    # print("%s的生命值剩余%d" % (gailun.nicheng, gailun.shengmingzhi))
    # 父类的吃喝玩，这里可以看到修改了类的继承对象之后，对象不用修改马上就拥有了父类的方法
    gailun.chi()

    # 战斗,传进来谁就打谁

    zhaoxin=gailun.gongji(zhaoxin)
    # print("%s的生命值剩余%d"%(zhaoxin.nicheng,zhaoxin.shengmingzhi))


    # print(gailun.__str__())

    
    ##############  操作属性  ###########
    studytest.shuxing1="bbb"  # 修改
    studytest.shuxing2="ccc"  # 新增，也就是说如果修改值，如果属性存在就进行修改，不存在就进行新增

    print(studytest.shuxing1,studytest.shuxing2)
    del studytest.shuxing2    # 使用del关键字进行删除

    ##############  操作方法  ##############
    studytest.chi(studytest)

    ##############  初始化对象  ##############
    duixiang1=studytest("小丁1") # 类似于方法的调用，也可以称之为实例化
    # 多次初始化是不同的对象引用，相当于都继承了被初始化的类，但是他们的
    duixiang2=studytest("小丁2")
    duixiang3=studytest("小丁3")

    duixiang1.chi()  # 这两种形式，（对象名，类名）去调用大同小异,duixiang1.chi()等同于studytest.chi(studytest)

    print(duixiang1.__dict__) # 类的所有属性都会以字典的形式存储在这个变量了,可以通过字典取值方式取出对应的变量
    print(duixiang1.__dict__["shuxing1"])

    # 类有两种属性，数据属性和函数属性

    # 1 类的数据属性是所有对象共享的，id（id是Python的实现机制编号，和内存地址不是一个）都一样，实际测试之后是不一样的
    print(id(duixiang1),id(duixiang2),id(duixiang3))
    print(id(duixiang1.shuxing1), id(duixiang2.shuxing1), id(duixiang3.shuxing1))
    # obj.shuxing会首先从自己的名称空间里去找，找不到去类中寻找，再找不到，再去父类中寻找，如果全部找不到抛出异常

    # 2 类的函数属性是绑定给对象使用的，obj.method成为绑定的方法，内存地址都不一样,也就是初始化了对象之后，每个对象操作的时候不会影响其他对象

    '''





