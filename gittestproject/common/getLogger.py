'''
提供记录日志操作
Date:20181027
Author:AAA
'''
# 级别：debug 详细运行日志  info 自己想要记录下，没啥特别的  warning 警告和提醒  error 一般错误 critical 严重错误
# 基本设置,日志的记录文件，记录日志的最低级别，时间格式,测试说明，第一个配置配置过了，后面的配置不起作用
import logging

def getLogger(log_filename):
    # 基本设置,日志的记录文件，记录日志的最低级别，时间格式,测试说明，第一个配置配置过了，后面的配置不起作用
    # logging.basicConfig(filename=log_filename, level=logging.WARNING,format="%(asctime)s%(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    # 定义一个写日志的对象
    logger = logging.getLogger("lipengchao")  # 写日志的对象
    logger.setLevel(logging.DEBUG)  # 设定一个全局的日志级别

    # 日志输出对象，屏幕和文件都输出
    sh = logging.StreamHandler()  # 输出到屏幕的对象
    sh.setLevel(logging.WARNING)  # 设置屏幕输出的级别

    fh = logging.FileHandler(log_filename)
    fh.setLevel(logging.DEBUG)  # 设置文件输出的级别

    # 设置输出的格式
    # gszd = {"asctime": "时间", "name": "用户名", "levelname": "日志级别名称", "filename": "写日志的文件名称",
    #         "module": "写日志的模块名称","funcName": "写入日志的函数名称", "lineno": "写入日志的代码行号",
    #         "message": "日志信息", "process": "进程号", "pathname": "路径名称",
    #         "processname": "进程名称", "thread": "线程id", "threadname": "线程名称" }

    wjformatter = logging.Formatter("%(asctime)s-%(name)s-%(filename)s-%(levelname)s-%(lineno)d-%(funcName)s-%(message)s")
    pmformatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")

    # 将格式指定到对应的handle
    sh.setFormatter(pmformatter)
    fh.setFormatter(wjformatter)

    # logger绑定handle
    logger.addHandler(sh)
    logger.addHandler(fh)

    return logger


# if __name__ == '__main__':
#     DEBUG_LOG_FILENAME = "/media/lipengchao/study/pycharmproject/studyProject/log/test.log"
#     logger=getLogger(DEBUG_LOG_FILENAME)
#     # 使用logger对象进行日志的记录
#     logger.debug("{debug}登录了")
#     logger.info("{info}登录了")
#     logger.warning("{warning}登录了")
#     logger.error("{error}登录了")
#     logger.critical("{critical}登录了")