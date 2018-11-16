class Student(object):
    def __init__(self,name):
        print(name+"是一个学生")

    def study(self):
        print("学习中。。。。。")

    # 将内定的专有方法返回值进行修改就可以修改系统默认的返回方法定义的值
    def __str__(self):
        return "这是系统返回给前台用户的方法定义"
    # __str__()是返回给前台客户的值，__repr__是返回给开发者的值
    def __repr__(self):
        return "这是系统返回给开发者的方法定义"
    # 当然也是可以不用分开定义，直接等于就可以了   __repr__=__str__

    def __getattr__(self, item):  # item是属性的名称
        if item=='name':
            return "没名字"  # 这样就实现了如果没有name这个属性就会给个默认返回的值

xiaoming=Student("xiaoming")
print(xiaoming)
print(Student("xiaoming"))


class fbnq(object):
    def __init__(self):
        self.a,self.b=0,1  # 初始化两个计数器

    def __iter__(self):
        return self  # 实例本身就是迭代对象，返回自己就可以了

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b  # 计算下一个值
        if self.a>100:  # 循环条件
            raise StopIteration()
        return self.a # 返回下一个值

    # 提供可以获取下表指定的值方法
    def __getitem__(self, item):
        a,b=1,1
        for x in range(item):
            a,b=b,a+b
            # b=a+b  这样是不行的，第一个数字如果不变化为第二个数字，那么总会是初始的a和b
        return a

aaa=fbnq()
print("第二个值是：",aaa[5])


for n in fbnq():
    print(n)


# __getattr__

xiaohei=Student("xiaohei")
print(xiaoming.name)

# __call__ 定义了此方法可以直接对实例进行调用
