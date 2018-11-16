# 获取系统当前状态，每天进行邮件的发送
# 李鹏超　20180914  由于３．５的混乱，所以果断使用了３．７版本，不然全部是乱的，版本太多了，我估计初始化都初始化到３．６上面去了

import psutil
import time

today=time.strftime("%Y-%m-%d %H:%M:%S")


def getSystemStatus():
    result = {}s
    # cpu 信息
    hxs=psutil.cpu_count(logical=False)  # 不带参数为逻辑核心个数(也就是线程数)，带参数为物理核心个数
    xcs=psutil.cpu_count()  # 发现在开机时间长了之后物理核心的获取数会混乱错误，所以这个方法还是慎用，但是逻辑核心数准确
    cpuinfo = {"hxs": hxs, "xcs": xcs}
    # print(psutil.cpu_times())
    ci= psutil.cpu_times()
    cpuinfo["user"]=ci.user  # 用户ｕｓｅｒ任务的ＣＰＵ时间
    cpuinfo["idle"]=ci.idle  # cpu空闲时间比
    cpuinfo["iowait"]=ci.iowait  # 由于ｉｏ等待ＣＰＵ空闲时间占比
    cpuinfo["system"]=ci.system  # 执行系统内核和中断时间占比
    cpuinfo["percent"]=psutil.cpu_percent()  # 使用率

    # memory 信息 total（内存总数）、used（已使用的内存数）、free（空闲内存数）、buffers（缓冲使用数）、cache（缓存使用数）、swap（交换分区使用数）
    memoryinfo={}
    # print(psutil.virtual_memory())
    mi=psutil.virtual_memory()
    memoryinfo["total"]=mi.total
    memoryinfo["used"]=mi.used
    memoryinfo["free"]=mi.free
    memoryinfo["percent"]=mi.percent

    # print(psutil.swap_memory())  # 获取swap信息

    # disk 信息  一部分是利用率 disk_usage，一部分是分区信息，一部分是io  disk_io_counters　磁盘IO信息包括read_count（读IO数）、write_count（写IO数）、read_bytes(IO读字节数)、write_bytes（IO写字节数）、read_time（磁盘读时间）、write_time（磁盘写时间）
    # print(psutil.disk_partitions())
    diskinfo=""
    disk_fq=psutil.disk_partitions()
    for fq in disk_fq:
        # print(fq.device)
        # print("测试》》》》》",psutil.disk_usage("/"));  # 传入的参数是挂载点不是驱动名称
        fqsyl = psutil.disk_usage(fq.mountpoint);
        diskinfo+="驱动名称是%s,挂载点是《%s》，文件格式是《%s》,总大小是《%d GB》,已使用《%d GB》，未使用《%d GB》，使用率是《%d%%》"\
                 %(fq.device,fq.mountpoint,fq.fstype,fqsyl.total/1024/1024/1024,fqsyl.used/1024/1024/1024,fqsyl.free/1024/1024/1024,fqsyl.percent)
        diskinfo+="\n";
        # 获取当前磁盘分区使用率
        # for syl in fqsyl:
        #     print(syl);
        #   print("当前驱动器是%s,总大小是%d,已使用%d，未使用%d，使用率是%d%%"%(fq.device,fqsyl.total,fqsyl.used,fqsyl.free,fqsyl.percent))
    # read_count 读取io数，write_count 写入io数，read_bytes 读取字节数，read_time 读取时间
    print("硬盘总体的ｉｏ信息是：",psutil.disk_io_counters());
    print("每个分区硬盘的ｉｏ信息是：", psutil.disk_io_counters(perdisk=True));  # 每个分区的情况

    # net信息
    # print("所有网卡地址情况", psutil.net_if_addrs());
    # print("没看到有啥用",psutil.net_if_stats());
    # print("网络地址情况比第一个详细一些", psutil.net_connections());
    # print("没看到有啥用》》》》", psutil.net_io_counters());
    netio=psutil.net_io_counters();  # 网络总体发包情况
    netioinfo={};
    netioinfo["fssj"]=netio.bytes_sent;
    netioinfo["jssj"]=netio.bytes_recv;
    netioinfo["fsb"]=netio.packets_sent;
    netioinfo["jsb"]=netio.packets_recv;
    netioinfo["err"]=netio.errin+netio.errout;
    netioinfo["drop"]=netio.dropin+netio.dropout;

    # 其他系统信息
    other={};
    kjsj=psutil.boot_time();  #　开机时间，返回时间戳，需要进行转换
    kjsj=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(kjsj));
    other["kjsj"] = kjsj;
    # print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(1537318016.0)),time.asctime(time.localtime(1537318016.0)))

    # 当前用户信息
    dqyh=psutil.users();  # 对象包含，用户名，回话编号，登录地址，登录开始时间，程序线程号
    # print(dqyh[0].name)
    logintime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(dqyh[0].started));
    yhinfo={"username":dqyh[0].name,"terminal":dqyh[0].terminal,"host":dqyh[0].host,"logintime":logintime,"pid":dqyh[0].pid};

    # 查看系统进程
    # print("直接展示所有进程号，感觉实际作用很小,估计也就用于循环使用了和后面的方法搭配使用",psutil.pids());
    for jc in psutil.pids():
        print("当前处理的进程号是：",jc);
        print(psutil.Process(jc))
        # print(psutil.cpu_stats())     # psutil.LINUX可以用来判断是不是某个操作系统


    result["cpu"]=cpuinfo;
    result["memory"]=memoryinfo;
    result["disk"]=diskinfo;
    result["net"]=netioinfo;
    result["other"]=other;
    result["dqyh"]=yhinfo;
    return result;

# %%百分号转义百分号，大多情况下都是反斜杠进行转义
def main():
    result=getSystemStatus();
    content='''
    现在时间是%s，电脑开机时间是：%s，当前登录的用户是%s，登录地址是%s，登录时间是%s，登录进程是%s
    获取到的电脑硬件情况是：
        cpu信息：cpu拥有%d个核心数，%d线程，执行用户任务时间是%d,空闲时间是%d,由于io等待导致的空闲时间是%d,总体使用率是百分之%d;
        内存信息：内存总共大小为%d,已经使用的为%d，空闲的为%d，占比为%d%%；
        硬盘信息：%s;
        网络总体情况：总共发送字节数%d，接收字节数%d，发包数%d，收包数%d，错误数%d，丢包数%d；
    '''% (today,result["other"]["kjsj"],result["dqyh"]["username"],result["dqyh"]["host"],result["dqyh"]["logintime"],result["dqyh"]["pid"],
          result["cpu"]["hxs"],result["cpu"]["xcs"],result["cpu"]["user"],result["cpu"]["idle"],result["cpu"]["iowait"],result["cpu"]["percent"],
          result["memory"]["total"],result["memory"]["used"],result["memory"]["free"],result["memory"]["percent"],
          result["disk"],
          result["net"]["fssj"],result["net"]["jssj"],result["net"]["fsb"],result["net"]["jsb"],result["net"]["err"],result["net"]["drop"]
          );
    print(content);


if __name__ == '__main__':
    main();
