import threading
from time import sleep
from datetime import datetime

loops=[4,2]
format_str='%y-%m-%d %H:%M:%S'
# 用于输出一个指定格式的时间函数
def date_time_str(date_time):
    return datetime.strftime(date_time,format_str)

def loop(n_loop,n_sec):
    print('线程（',n_loop,')开始执行',date_time_str(datetime.now()),'先休眠',n_sec,'秒')
    sleep(n_sec)
    print('线程（', n_loop, ')执行结束,结束于', date_time_str(datetime.now()))

def main():
    print('----所有线程开始执行：',date_time_str(datetime.now()))
    threads=[]
    n_loops=range(len(loops))

    for i in n_loops:
        t=threading.Thread(target=loop,args=(i,loop[i]))
        threading.Thread()
        threads.append(t)

    for i in n_loops: # start threads
        threads[i].start()

    for i in n_loops: # wait for all
        threads[i].join() #threads to finish

    print("-------所有线程结束于：",date_time_str(datetime.now()))

if __name__ == '__main__':
    main()



