'''
购物商城购物流程
Date:20181026
Author:AAA
'''


import os
import datetime
from modules import shopping
from common import getConfig


class Shoppingprocess(object):

    "商城主流程类" # 类的说明字符串

    def main(self=None):
        # 实例化操作类
        scgw = shopping.Shopping();
        # 登录次数限制
        login_limit = 3;
        # 已购物品小票清单，在程序退出或者客户主动选择结账的时候进行结账，如果结账成功进行序列化保存
        gwqdlist = [];
        # 订单，存储每一个用户一次购物的信息
        qdinfo = {};
        qdlist = [];  # 存放反序列化取出来的历史记录，用来在登录的时候进行展示

        # 定义序列化和反序列化的存储读取路径
        basicpath = os.path.abspath("../")
        gwqdpath = getConfig.get_gwqdpath(basicpath)
        yhxxpath = getConfig.get_yhxxpath(basicpath)
        spxxpath = getConfig.get_spxxpath(basicpath)
        spflpath = getConfig.get_spflpath(basicpath)
        yhjbpath = getConfig.get_yhjbpath(basicpath)
        ztpath = getConfig.get_ztpath(basicpath)
        # 初始化系统基本信息，初始运行一次
        # csh(yhxxpath=yhxxpath,spxxpath=spxxpath,spflpath=spflpath,yhjbpath=yhjbpath,ztpath=ztpath)

        while True:
            # 提示系统功能信息
            print('''
            功能菜单：1 注册 
                    2 登录
                    3 充值
                    4 查看历史购物记录
                    5 查看所有商品,进行购物
                    6 新增商品
                    7 新增商品分类
                    8 新增用户级别
                    9 新增状态
                    10 查看当前打折商品
                    11 修改商品信息
                    12 注销当前登录账户
                    13 退出系统
                    14 初始化系统信息
            ''')
            userchoice = input("请输入您需要的操作功能编号\t\t")
            if userchoice == "1":
                scgw.zhuce(yhxxpath=yhxxpath, gwqdpath=gwqdpath,spxxpath=spxxpath,cs=login_limit)
                continue
            elif userchoice == "2":
                scgw.login(yhxxpath=yhxxpath, gwqdpath=gwqdpath,spxxpath=spxxpath,cs=login_limit)
                continue
            elif userchoice == "3":

                scgw.chongzhi(username=scgw.IS_LOGIN, yhxxpath=yhxxpath)
                continue
            elif userchoice == "4":
                scgw.sy(yhxxpath=yhxxpath,spxxpath=spxxpath,gwqdpath=gwqdpath)
                continue
            elif userchoice == "5":
                scgw.getspfl(spflpath=spflpath, spxxpath=spxxpath)
                while True:
                    dqyh = scgw.getdqyh(yhxxpath)
                    ye = dqyh.get("ye");
                    scgw.gw(yhxxpath=yhxxpath,spxxpath=spxxpath,gwqdpath=gwqdpath,gwqdlist=gwqdlist);
                    choice = input("是否继续购买（y/n）");
                    if choice.lower() != 'y':
                        print("感谢您的购物，期待您的下次光临！！！");
                        hj=scgw.sy(yhxxpath, spxxpath, gwqdpath);  # 这一步会进行结账，所以我们进行返回余额
                        dqyh["ye"] = ye-hj;
                        qdinfo["gmyh"] = dqyh.get("name");
                        qdinfo["ddsj"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        qdinfo["sp"] = gwqdlist;
                        qdinfo["ye"] = ye-hj;
                        scgw.xlh(xlhnr=qdinfo,filepath=gwqdpath)
                        break;
                    continue;
            elif userchoice == "6":
                spbm = input("输入新增商品编码")
                name = input("输入新增商品名称")
                jg = int(input("输入新增商品价格"))
                sl = int(input("输入新增商品数量"))
                fl = input("输入新增商品分类")
                spxx = {"spbm": spbm, "name": name, "jg": jg, "sl": sl, "zt": "1", "fl": fl, "gm": ""}
                scgw.xzxxlist(xzxx=spxx, wjlj=spxxpath)
                continue
            elif userchoice == "7":
                spfl = {}
                flbm = input("输入新增商品分类编码")
                flmc = input("输入新增商品分类名称")
                if flbm.strip() and flmc.strip():
                    spfl = {flbm: flmc}
                    scgw.xzdmdic(xzxxdic=spfl, wjlj=spflpath)
                continue
            elif userchoice == "8":
                yhjb = {}
                jbbm = input("输入新增用户级别编码")
                jbmc = input("输入新增用户级别名称")
                if jbbm.strip() and jbmc.strip():
                    yhjb = {jbbm: jbmc}
                    scgw.xzdmdic(xzxxdic=yhjb, wjlj=yhjbpath)
                continue
            elif userchoice == "9":
                zt = {}
                ztbm = input("输入新增状态编码")
                ztmc = input("输入新增状态名称")
                if ztbm.strip() and ztmc.strip():
                    zt = {ztbm: ztmc}
                    scgw.xzdmdic(xzxxdic=zt, wjlj=ztpath)
                continue
            elif userchoice == "10":
                查看当前打折商品
            elif userchoice == "11":
                修改商品信息
            elif userchoice == "12":
                scgw.IS_LOGIN=False; # 取消登录状态就可以了
                print("退出登录成功")
                continue
            elif userchoice == "13":
                choice = input("确实要退出系统吗（y/n）")
                if choice == "y":
                    break;
                else:
                    continue
            elif userchoice == "14":
                print("将要对系统基础信息进行初始化，请勿重复使用")
                scgw.chushihua(yhxxpath, spxxpath, spflpath, yhjbpath, ztpath)
            else:
                scgw.getspfl(spflpath=spflpath, spxxpath=spxxpath)
                while True:
                    dqyh = scgw.getdqyh(yhxxpath)
                    ye = dqyh.get("ye");
                    scgw.gw(yhxxpath=yhxxpath, spxxpath=spxxpath, gwqdpath=gwqdpath, gwqdlist=gwqdlist);
                    choice = input("是否继续购买（y/n）");
                    if choice.lower() != 'y':
                        print("感谢您的购物，期待您的下次光临！！！");
                        hj = scgw.sy(yhxxpath, spxxpath, gwqdpath);  # 这一步会进行结账，所以我们进行返回余额
                        dqyh["ye"] = ye - hj;
                        qdinfo["gmyh"] = dqyh.get("name");
                        qdinfo["ddsj"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        qdinfo["sp"] = gwqdlist;
                        qdinfo["ye"] = ye - hj;
                        scgw.xlh(xlhnr=qdinfo, filepath=gwqdpath)
                        break;
                    continue;