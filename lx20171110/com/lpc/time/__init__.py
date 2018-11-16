import time

print("当前时间戳是：%f"%time.time())

# localtime(秒数) 返回当前时区的结构时间 默认是当前时间
aaa=time.localtime()  # 返回一个当前时间九个组成部分的元组，如果输入秒数参数就按照输入的时间戳进行转换
print("localtime返回当前时区的结构时间：",aaa) # 当然就可以使用元组的操作对其进行操作
# gmtime 返回0时区的结构时间 默认是当前时间
print("gmtime返回0时区的结构时间：",time.gmtime())

# mktime 将结构时间返回时间戳 如果不输入结构参数就会提示参数错误,与上面的操作反向
t=(2018,5,8,14,47,0,0,0,1)  # 这个地方后面的参数都直接输入0也是可以的，只要日期时间到秒一致小数点前面就会一致，小数点后面的是毫秒数，后面的周什么的，没有发现对结果有影响
print("mktime将结构时间返回当前时间戳：",time.mktime(t))

# asctime用于将localtime和gmtime返回的结构时间转为可读的格式

print("asctime用于将结构时间转为可读格式",time.asctime(aaa))

# ctime 用于将一个时间戳转为可读格式,参数为秒
print("ctime用于将时间戳转为可读格式,如果没有参数，就是当前时间戳",time.ctime(23))

# time.clock() 在Windows上第一次调用返回进程运行的实际时间，可以很方便的判断一段代码执行的效率
print("返回进程运行的实际时间",time.clock())

# sleep() 和Java一样用于暂停，参数为秒数
# time.sleep(1)
print("sleep停一秒进行输出")

# time.clock() 在Windows上第一次调用返回进程运行的实际时间，第二次进行调用，返回第一次调用后到现在的时间，在linux上返回的是cpu处理这段命令的时间
print("第二次进行调用，返回第一次调用后到现在的时间",time.clock())

# strftime()
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

# strptime()
print(time.strptime('2018-05-15','%Y-%m-%d'))

# datetime
import  datetime
# 常量
print('datetime能标示的最小年份和最大年份是',datetime.MINYEAR,datetime.MAXYEAR)
# 方法
print("本地当前时间是",datetime.datetime.today())
print("指定的时区当前时间是",datetime.datetime.now())  # 如果传入市区的参数就获取制定市区的当前时间，没有就是本地的

# utcnow() 返回一个当前utc时间的datetime对象
print("返回一个当前utc时间的datetime",datetime.datetime.utcnow())  # utc标准时间
# fromttimestamp(timestamp,[tz])  传入时间戳和时区的信息，返回一个datetime对象
print("传入时间戳和时区的信息，返回一个datetime对象",datetime.datetime.fromtimestamp(time.time()))

# 日期模块，另外发现日历模块传入的参数也可以使用比如thenyear=2018的这种形式进行传入，也可以直接传入2018的数字进行传入
import  calendar

print(calendar.calendar(theyear=2018,w=2,l=1,c=6)) # thenyear是年份的表头，w是每日之间的间隔字符数，c是指每月之间的间隔字符数，l是指每个星期的行数 ，返回一个日历，返回整年日历

print("返回每周开始日期，默认是0也就是从星期一开始",calendar.firstweekday())

print("判断参数的年份是不是闰年",calendar.isleap(2018))  # 这个方法有意思，如果不传参数不是默认当前年，而是什么都不返回，如果有参数则返回true或者false

print("返回在指定年份之间的闰年数量",calendar.leapdays(2017,2021))  # 这个函数是包含开始年份，但是不包含结束年份的计算

print("返回一个指定年月的日历",calendar.month(theyear=2018,themonth=5,w=2,l=1))  # 也就是返回指定年份和月份的日历，返回正月日历

print("将指定月份按照每一周的日期一个列表的形式进行返回，如果有和其他月份日期交叉的周，其他月份的日期返回为0",calendar.monthcalendar(year=2018,month=5))

print("返回指定年月的起始日期情况",calendar.monthrange(2018,4))  # 经过测试发现，返回两个整数，第一个是该月1号所在星期数（但是总是比实际星期几少1也就是这个返回数字加1才是实际星期数，这个主要是因为周一是0的原因没，在使用的时候需要注意，第二个数是该月的最大日期数，也就是该月的天数）

print("没看清作用是啥",calendar.setfirstweekday(0))

print(calendar.weekday(2018,5,17))