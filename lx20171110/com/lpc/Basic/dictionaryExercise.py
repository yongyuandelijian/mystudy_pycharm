# 20180107
# lpc
# 字典是一种可变容器，可以存储任意类型对象
mydic={1:"盖伦",2:"赵信",3:"皇子",4:"剑圣",5:"潘森"}
print("我的英雄是：",mydic[1])

# dict 函数是将其他有规律的对应转换为字典的函数
##############################################特殊情况
# mydic = dict((1,'aa'),(2,'bb'),(3,'cc')) # 报错提示获取的参数是3个 应该是由于里层外层都是小括号导致的无法区分内层和外层的关系
# mydic = dict[('a','aa'),('b','bb')] # 'type' object is not subscriptable  不知道为啥原因？
mydic = dict([('a','aa'),('b','bb')]) # 和以上对比，dict函数在创建过程中需要将他们当作一个整体来进行处理，这个情况比较特殊
###################################################
mydic = dict(a='aa',b='bb',c='cc') # 成功
# 增删改查
mydic['a']='按照key更新value'
mydic['aa']=1 # 没有这个key的时候，直接在最后进行了新增，所以可以看到是不可以根据值去更新key，key是不可变的 ,此处和update方法有些类似，区别在于update方法需要传入一个字典当作参数
del mydic['aa']  # 如果没有指定key那么就会删除整个字典，在使用字典就会提示未声明字典
# del mydic
# mydic.clear() 这两者有区别，虽然都是删除了所有元素，但是上面直接是对象不存在的，clear只是里面的元素不存在，但是字典还是存在的
print("使用dict函数创建的字典：",mydic,"字典的键值对个数是：",len(mydic),"类型是:",type(mydic),"字典的第一个值是：%(a)s"%mydic)
# 如果声明两次重复的key那么最后一次的会覆盖之前的key值，使用格式化方式获取value的时候key的值要直接写在括号内，不必写引号之类的，从报错可以看出来，系统源码应该是添加了引号
mydic2=mydic
mydic1=mydic.copy()
mydic1['d']="dd"  # 增加一个没有变化
mydic1['d']='修改副本新增的值之后'
mydic1['a']='修改副本和原字典都有的值之后'
mydic2['e']='ee'  # 赋值引用对象之后会修改原字典，其他操作应该也是一样的
print(mydic,"copy之后的：\n",mydic1,'\n赋值到mydic2增加之后的是：\n',mydic2)
# 使用了以上代码对引用和copy做了测试区别，在使用中需要注意，避免逻辑错误

# 创建新字典 fromkeys
key=("1","2","3")
mydic1.fromkeys(key) # 没有默认value  # 如果mydic1不为空，那么不会保持原值不变
mydic3 = {}
# mydic3=mydic3.fromkeys(key) # 没有声明的字典不能使用fromkeys函数，这样的函数估计也只是适合快速增加key
mydic3=mydic3.fromkeys(key,10)
print("fromkeys创建之后：",mydic3,"\n获取字典的值一种可以直接使用【key】进行获取，",mydic3["1"],"判断key是否在一个字典内", 'a' in mydic3,"\n另一种也可以使用get(key,[defalut])进行获取，get的好处是没有获取到不会报错，输出默认值：",mydic3.get('a','没找到key对应的值'))
itemfhz=mydic3.items()
print(itemfhz)  # dict_items([('1', 10), ('2', 10), ('3', 10)]) 返回了一个元组数组
keylist=mydic3.keys()
print(keylist)
print(mydic3.values())

# update方法
mydic3.update(mydic2)
print(mydic3)  # 如果存在相同key进行覆盖更新为参数的value，如果不存在则直接新增参数的key和value对

# setdefalut 查找key对应的值，如果找到返回对应值，如果找不到将默认值和查找值以键值对的方式存进字典
mydic3.setdefault('teshu','xiaoding')
print("使用setdefalut查找之后：",mydic3,"对字符串使用格式化：%-10s"%mydic3["e"])
