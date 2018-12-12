'''
购物商城购物流程
Date:20181026
Author:AAA
'''


import os
import sys
import modules.shopping as shopping
import common.getConfig as getConfig
import common.getLogger as getLogger


class Shoppingprocess(object):

    "商城主流程类" # 类的说明字符串

    def main(self=None):
        # 实例化操作类
        SCGW = shopping.Shopping()
        # 登录次数限制
        LOGIN_LIMIT = 3
        # 已购物品小票清单，在程序退出或者客户主动选择结账的时候进行结账，如果结账成功进行序列化保存,重新加载后，重新清空
        GWQDLIST = []
        # 订单，存储每一个用户一次购物的信息
        QDINFO = {}
        # qdlist = []  # 存放反序列化取出来的历史记录，用来在登录的时候进行展示

        # 定义序列化和反序列化的存储读取路径
        BASICPATH = os.path.abspath("../")
        GWQDPATH = getConfig.get_gwqdpath(BASICPATH)
        YHXXPATH = getConfig.get_yhxxpath(BASICPATH)
        SPXXPATH = getConfig.get_spxxpath(BASICPATH)
        SPFLPATH = getConfig.get_spflpath(BASICPATH)
        YHJBPATH = getConfig.get_yhjbpath(BASICPATH)
        ZTPATH = getConfig.get_ztpath(BASICPATH)
        DQPATH= getConfig.get_dqpath(BASICPATH)
        # 获取写日志对象
        LOGGER = getLogger.getLogger(log_filename=getConfig.get_logall(BASICPATH))
        # 初始化系统基本信息，初始运行一次
        # csh(yhxxpath=YHXXPATH,spxxpath=SPXXPATH,spflpath=SPFLPATH,yhjbpath=YHJBPATH,ztpath=ZTPATH)

        while True:
            # 提示系统功能信息
            print('''
            功能菜单：1 注册 
                    2 登录
                    3 充值
                    4 查看历史购物记录
                    5 查看所有商品分类以及商品,进行购物
                    6 新增商品
                    7 新增商品分类
                    8 新增用户级别
                    9 新增状态
                    10 查看当前打折商品
                    11 修改商品信息
                    12 修改密码
                    13 注销当前登录账户
                    14 退出系统
                    15 初始化系统信息
            ''')
            userchoice = input("请输入您需要的操作功能编号\t\t")
            if userchoice == "1":
                SCGW.zhuce(yhxxpath=YHXXPATH, gwqdpath=GWQDPATH,spxxpath=SPXXPATH,cs=LOGIN_LIMIT)
                continue
            elif userchoice == "2":
                SCGW.login(yhxxpath=YHXXPATH, gwqdpath=GWQDPATH,spxxpath=SPXXPATH,cs=LOGIN_LIMIT)
                continue
            elif userchoice == "3":
                SCGW.chongzhi(username=SCGW.IS_LOGIN, yhxxpath=YHXXPATH)
                continue
            elif userchoice == "4":
                SCGW.sy(yhxxpath=YHXXPATH,spxxpath=SPXXPATH,gwqdpath=GWQDPATH)
                continue
            elif userchoice == "5":
                SCGW.gwlc(spflpath=SPFLPATH,spxxpath=SPXXPATH,yhxxpath=YHXXPATH,gwqdlist=GWQDLIST,qdinfo=QDINFO)
            elif userchoice == "6":
                SCGW.xzspxxlist(spxxpath=SPXXPATH)
                continue
            elif userchoice == "7":
                SCGW.xzspfl(spflpath=SPFLPATH)
                continue
            elif userchoice == "8":
                SCGW.xzyhjb(yhjbpath=YHJBPATH)
                continue
            elif userchoice == "9":
                SCGW.xzzt(ztpath=ZTPATH)
                continue
            elif userchoice == "10":
                SCGW.getdzspxx(spxxpath=SPXXPATH)
            elif userchoice == "11":
                SCGW.xgspxx(spxxpath=SPXXPATH)
            elif userchoice == "12":
                SCGW.xgmm(yhxxpath=YHXXPATH)
            elif userchoice == "13":
                if SCGW.IS_LOGIN:
                    LOGGER.info("{name}退出系统了".format(name=SCGW.IS_LOGIN))
                    SCGW.IS_LOGIN=False
                    print("退出登录成功")
                if not SCGW.IS_LOGIN:
                    print("当前没有登录账户")
                continue
            elif userchoice == "14":
                choice = input("确实要退出系统吗（y/n）")
                if choice == "y":
                    if SCGW.IS_LOGIN:
                        LOGGER.info("{name}退出系统了".format(name=SCGW.IS_LOGIN))
                    sys.exit();
                else:
                    continue
            elif userchoice == "15":
                print("将要对系统基础信息进行初始化，请勿重复使用")
                SCGW.chushihua(YHXXPATH, SPXXPATH, SPFLPATH, YHJBPATH, ZTPATH,DQPATH)
                LOGGER.info("{name}对系统进行了初始化".format(name=SCGW.IS_LOGIN))
            else:
                SCGW.gwlc(spflpath=SPFLPATH, spxxpath=SPXXPATH, yhxxpath=YHXXPATH, gwqdlist=GWQDLIST, qdinfo=QDINFO)
                continue