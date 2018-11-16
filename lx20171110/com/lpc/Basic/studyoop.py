# 从学习面向对象开始，使用新的学习记录
# 20181114

# 类在定义的时候就会产生新的名称空间，用来存放类的变量名和函数名，可以通过类名.__dict__ 查看
# 类中定义的名字都是类的属性，点是访问属性的语法，类有两种属性，数据属性和函数属性
# 对于经典类来说我们可以通过该字典操作类名称空间的名字，但新式类有限制
class studytest():
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


if __name__ == '__main__':

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

    # 2 类的函数属性是绑定给对象使用的，obj.method成为绑定的方法，内存地址都不一样




