# 多线程 _thread
import _thread
from time import sleep
from datetime import datetime
# 定义格式化字符串
format_str='%y-%m-%d %H:%M:%S'
# 定义函数格式化时间
def date_time_str(date_time):
    return datetime.strftime(date_time,format_str)
# 线程1
def loop_one():
    print("线程1开始运行时间",date_time_str(datetime.now()))
    print("线程1要开始休息3秒")
    sleep(3)
    print("线程1结束运行的时间：",date_time_str(datetime.now()))
# 线程2
def loop_two():
    print("线程2开始运行时间",date_time_str(datetime.now()))
    print("线程2要开始休息2秒")
    sleep(2)
    print("线程2结束运行的时间：",date_time_str(datetime.now()))
# 主线程
def main():
    print("所有线程开始运行时间：",date_time_str(datetime.now()))
    _thread.start_new_thread(loop_one,())  # 如果不传入元组的参数也要写上空的元组，否则会提示错误
    _thread.start_new_thread(loop_two,())
    sleep(5)  # 很神奇的就是在这里，如果主线程不再这里等待以上两个线程所需要时间的合计，主线程结束，其他线程也就必须跟着结束，加了这段等待之后，其他线程也运行正常了，另外也可以看出，当一个线程休息的时候就会去处理其他线程的事情
    print("所有线程结束运行时间：", date_time_str(datetime.now()))

# 执行主线程
if __name__=='__main__':  # 如果是使用构造的名称判断，那么其实其他名字也可以作为程序入口，但是大家应该都还是适应main这个名字吧
    main()