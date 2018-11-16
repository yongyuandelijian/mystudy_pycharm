'''
提供购物商城所有功能操作,功能列表详见FunctionalDescription
Date:20181026
Author:AAA
'''
import datetime
import json
import os
import sys
import requests
from common import getLogger
from common import getConfig


class Shopping(object):
    IS_LOGIN = False;  # 用来记录登录状态,如果为False就是未登录，如果为用户名称就是已经登录
    LOGGER_ALL = getLogger.getLogger(getConfig.get_logall(os.path.abspath("../")))
    LOGGER_ERROR=getLogger.getLogger(getConfig.get_logerror(os.path.abspath("../")))
    ####################### 装饰器函数 start #######################
    # 检查是否登录d
    def check_login(func):
        def inner(*args, **kwargs):
            result = ""
            if Shopping.IS_LOGIN:
                result = func(*args, **kwargs)
            else:
                print("您没有登录或权限不足，无法使用本功能")
            return result

        return inner

    # 检查是否是高级用户
    def check_gjyh(func):
        def inner(*args, **kwargs):
            result = "";
            if Shopping.IS_LOGIN and Shopping.getdqyh.get("jb") == "2":
                result = func(*args, **kwargs);
            else:
                print("您没有登录，或者登录的账号不是高级用户，无法使用本功能！！！")
            return result

        return inner;

    # 检查是否是管理员
    def check_gly(func):
        def inner(*args,**kwargs):
            result="";
            print(type(Shopping.getdqyh),Shopping.getdqyh)
            if Shopping.IS_LOGIN and Shopping.getdqyh.get("jb")== "3":
                result=func(*args,**kwargs);
            else:
                print("您没有登录，或者登录的账号不是管理员账户，无法使用本功能！！！")
            return result
        return inner;

    ####################### 获取当前用户余额 检查是否登录 start #######################

    def getdqyh(self, yhxxpath):
        yhlb = Shopping.fxlh(self, filepath=yhxxpath)
        for yh in yhlb:
            if yh.get("name") == Shopping.IS_LOGIN:
                return yh

    ####################### 文件操作的方法 start #######################
    # 文件读取的方法
    def wjcz_zd(self,wjlj):
        with open(file=wjlj, mode="r", encoding="utf-8") as zdwj:
            jsonstr = zdwj.read();
            return jsonstr;

    # 文件写入的方法
    def wjcz_zx(self,wjlj, jsonContent):
        with open(file=wjlj, mode="w", encoding="utf-8") as zxwj:
            zxwj.write(jsonContent);
            return True;

    ####################### 文件操作的方法 end #######################

    ####################### 序列化操作方法 start #######################

    # 将传入的对象转为json并进行序列化
    def xlh(self,xlhnr, filepath):
        # print(gwqd)
        wjnr = [];
        # 如果现有内容，追加到列表中，如果没有就直接追加当前对象就行了
        lsnr = Shopping.fxlh(self, filepath)
        if any(lsnr):
            wjnr = lsnr;
            # 信息表获取到的是一个列表,代码表获取到的是一个字典
            if type(wjnr) == list:  # 注意不是字符串
                wjnr.append(xlhnr)  # 列表是将新加的字典作为一个元素
            if type(wjnr) == dict:
                wjnr.update(xlhnr)  # 字典是将新加的字典更新进去
        else:
            wjnr = xlhnr;

        jsonstr = json.dumps(wjnr);
        jg = Shopping.wjcz_zx(self, filepath, jsonstr)
        return jg;

    def fxlh(self,filepath):
        # 判断下路径文件夹和文件是否存在，不存在就创建
        wjnr = '';
        if os.path.exists(filepath):
            jsonstr = Shopping.wjcz_zd(self, filepath)
            if type(jsonstr) == str and jsonstr.strip() != "":
                wjnr = json.loads(s=jsonstr, encoding="utf-8")
            else:
                print("文件没有内容！！！")
        else:
            # 进入之后两种情况，一种是文件和目录都不存在，一种只是文件不存在
            wjml = os.path.dirname(filepath)
            if not os.path.exists(wjml):
                os.makedirs(wjml)
            # wjm=os.path.basename(filepath) 获取文件名，经过测试并没有什么用
            os.mknod(filepath)  # 文件是肯定不存在，创建文件
            print(filepath + "目录或者文件不存在，已经自动创建成功")
        return wjnr;

    ####################### 序列化操作方法 end #######################

    ####################### 初始化数据操作 start #######################

    @check_login
    @check_gly
    def chushihua(self,yhxxpath, spxxpath, spflpath, yhjbpath, ztpath):
        # 初始化一些信息，后续只能通过调用新增信息
        # 用户基础信息
        xiaoming = {"name": "xiaoming", "password": "xiaoming", "ye": 500, "jb": "1", "zt": "1"}
        xiaoding = {"name": "xiaoding", "password": "12", "ye": 300, "jb": "2", "zt": "1"}
        xiaobai = {"name": "xiaobai", "password": "1", "ye": 100, "jb": "3", "zt": "1"}
        userlist = [xiaoming, xiaoding, xiaobai];
        # print("要初始化的用户信息是：", userlist)
        Shopping.xlh(self, userlist, yhxxpath)

        # 定义商品字典，每个商品七个信息，编号，名称，价格，数量,分类，是否有效，当前余额是否可以购买最少1个商品，这个属性纯属为了练习，没啥实际意义
        splist1 = {"spbm": 1, "name": "商品1", "jg": 20,"zl":0.9, "sl": 23, "zt": "1", "fl": "1"}
        splist2 = {"spbm": 2, "name": "商品2", "jg": 32, "zl":1,"sl": 2, "zt": "1", "fl": "2"}
        splist3 = {"spbm": 3, "name": "商品3", "jg": 2, "zl":1,"sl": 9, "zt": "1", "fl": "3"}
        splist4 = {"spbm": 4, "name": "商品4", "jg": 59, "zl":1,"sl": 143, "zt": "1", "fl": "3"}
        splist5 = {"spbm": 5, "name": "商品4", "jg": 123,"zl":0.6, "sl": 532, "zt": "1", "fl": "2"}
        splist6 = {"spbm": 6, "name": "商品4", "jg": 92,"zl":0.5, "sl": 1345, "zt": "1", "fl": "3"}
        SPLB = [splist1, splist2, splist3, splist4, splist5, splist6]
        # 商店列表，展示所有商品信息
        sdlist = []
        sdlist.append(splist1)
        sdlist.append(splist2)
        sdlist.append(splist3)
        sdlist.append(splist4)
        sdlist.append(splist5)
        sdlist.append(splist6)
        print("要初始化的商品信息是：", sdlist)
        Shopping.xlh(self, sdlist, spxxpath)

        # 代码部分
        # 公用代码状态
        ztdic = {"0": "无效", "1": "有效"}
        Shopping.xlh(self, ztdic, ztpath)
        # 商品分类代码
        spfldic = {"1": "分类1", "2": "分类2", "3": "分类3"}
        Shopping.xlh(self, spfldic, spflpath)
        # 用户类别代码
        yhjbdic = {"0":"临时用户","1": "普通用户", "2": "高级用户", "3": "管理员用户"}
        Shopping.xlh(self, yhjbdic, yhjbpath)
        print("初始化成功！！！！")

    ####################### 初始化数据操作 end #######################

    ####################### 获取天气的方法 start #######################
    def hqtq(self):
        response = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=西安")
        response.encoding = "utf-8"
        # print(type(response.text),response.text)
        tq = json.loads(response.text)
        tq = tq.get("data")

        mailContent = "城市:{city}\n空气指数：{aqi}\n感冒建议：{ganmao}\n当前温度:{wendu}\n" \
            .format(city=tq.get("city"), aqi=tq.get("aqi"), ganmao=tq.get("ganmao"), wendu=tq.get("wendu"))

        wtyb = tq.get("forecast");
        yb = ""
        for mt in wtyb:
            fl = mt.get("fengli")
            fl = fl[fl.index("[", 6, len(fl)):fl.index("]", 6, len(fl)) + 1]
            s = "日期：{date}\t\t\t{type}\t\t\t最高温度：{high}\t\t\t最低温度：《{low}》\t\t\t风力：{fengli}\t\t\t风向：{fengxiang}\n" \
                .format(date=mt.get("date"), type=mt.get("type"), high=mt.get("high"), low=mt.get("low"), fengli=fl,
                        fengxiang=mt.get("fengxiang"))
            yb = yb + s

        mailContent = mailContent + "\n\n下面是五天的天气预报：\n" + yb
        return mailContent
    ####################### 获取天气的方法 end #######################

    ####################### 提示当前拥有钱数和购物清单的方法 end #######################

    # 提示当前拥有钱数和购物清单的方法,必须登录才能使用
    @check_login
    def sy(self,yhxxpath, spxxpath, gwqdpath):
        hj = 0;
        dqyh = Shopping.getdqyh(self, yhxxpath)
        ye=dqyh.get("ye");
        print("\n本次已购清单是：")
        gwqdlist=Shopping.fxlh(self, filepath=gwqdpath)
        # 根据需要购物的商品字典设计为{商品编码，购买数量，购物时间}
        if len(gwqdlist) == 0:
            print("您没有购买任何商品，当前余额为%d" % ye)
            return
        else:
            for yg in gwqdlist:
                spxxlist = Shopping.fxlh(self, filepath=spxxpath)
                for sp in spxxlist:
                    if sp.get("spbm") == yg.get("spbm"):
                        hj = hj + yg.get("gmsl") * sp.get("jg");
                        print("【%s】,单价\t%d,数量\t%d,购买时间\t%s,小计\t%d" % (
                            sp.get("name"), sp.get("jg"), yg.get("gmsl"), yg.get("gwsj"),
                            yg.get("gmsl") * sp.get("jg")))
        print("消费合计为%d,余额为%d" % (hj, ye - hj));
        return hj;

    ####################### 提示当前拥有钱数和购物清单的方法 end #######################

    ####################### 购物 start #######################

    # 购物的方法，存储购物清单，更新用户余额，本方法只记录选购一个商品的购物，不涉及结账以及存储文本信息
    @check_login
    def gw(self,yhxxpath,spxxpath,gwqdpath,gwqdlist):
        dqyh = Shopping.getdqyh(self, yhxxpath)
        ye = dqyh.get("ye");
        gmsp = {}; # 根据需要 购物的商品字典设计为{商品编码，购买数量，购物时间}
        gmspbm = input("\n请选择你需要的商品（输入编号即可,输入n退出,输入c进行账户充值）\n");
        if gmspbm.lower() == "n":
            print("感谢您的购物，期待您的下次光临！！！")
            Shopping.sy(self, yhxxpath=yhxxpath, spxxpath=spxxpath, gwqdpath=gwqdpath)
            sys.exit();
        elif gmspbm.lower() == "c":
            czje = float(input("请输入充值金额\t"));
            Shopping.chuzhi(self, Shopping.IS_LOGIN, czje, yhxxpath)
        else:
            gmspbm = int(gmspbm);
            spxxlist=Shopping.fxlh(self, filepath=spxxpath)
            for sp in spxxlist:
                # 说明选择了给定列表的商品编号，我们将商品编号获取出来
                # print(sp.get("spbm"),gmsp)
                if gmspbm == sp.get("spbm"):
                    gmsp["spbm"] = gmsp;
                    gmsl = int(input("您当前要购买的请输入您要购买的数量\n"));
                    gmsp["gmsl"] = gmsl;
                    if ye < sp.get("jg") * gmsl:
                        print("对不起，您的余额不足 ！！！")
                        break;
                    else:
                        gmsp["gwsj"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
                        Shopping.gwqd(self, gmsp, gwqdlist= gwqdlist); # 将选购一次的商品放入本次购物小票
                    break;
                else:
                    continue;
        # return ye

    ####################### 购物 end #######################

    ####################### 购物清单小票 start #######################
    # 处理购物清单的方法,传入购物商品对象，print(ygsp) 处理已购买商品小票，如果商品是之前已经购买过就增加数量，否则我们进行追加
    # 后来我们发现，要展示当前用户的之前购物清单，还需要记录当前购买的用户id,所以我们需要重新设置这个购物清单的格式，修改为一个字典
    # gwqd  {"购买用户":"","购买时间":"","sp":[当前的购物清单]}
    def gwqd(self, ygsp, gwqdlist):
        ygspid = [];
        for yg_old in gwqdlist:
            ygspid.append(yg_old.get("spbm"));

        if ygsp.get("spbm") not in ygspid:
            # print("输入的商品还没有购买，进行追加")
            gwqdlist.append(ygsp);
        else:
            print("本次选购商品，购物清单已经存在，进行数量更新")
            for yg_old in gwqdlist:
                # print(yg_old.get("spbm"))
                if yg_old.get("spbm") == ygsp.get("spbm"):
                    yg_old["gmsl"] = yg_old.get("gmsl") + ygsp.get("gmsl")
                    # 这里更新为最后一次修改的时间，如果需要保留原始的时间，注销下面这句代码
                    yg_old["gwsj"] = ygsp.get("gwsj");
                    break;
                else:
                    continue;


    ####################### 购物清单小票 end #######################

    ####################### 获取商品分类以及全部信息列表 start #######################
    def getspfl(self,spflpath,spxxpath):
        print("\n本店商品分类如下：\n")
        print("分类编码\t\t分类名称")
        spfldic=Shopping.fxlh(self, filepath=spflpath)
        for key in spfldic:
            print("%d\t\t\t%s\t\t\t\t%d" % (key, spfldic.get("key")))
        flbm = input("选择您想要浏览的商品分类代码查看商品,0查看全部\t")
        spxxlist=Shopping.fxlh(self, filepath=spxxpath)
        # 获取商品是否可购买状态，从业务上来是没太大必要，这里主要是对程序扩展性的练习
        yxsplist = Shopping.getyxspqd(self, spxxlist, flbm);
        return yxsplist;


    # 获取当前有效商品列表，增加程序健壮性
    def getyxspqd(self, spxxlist, fl="0"):
        yxsplist=[];
        dqyh = Shopping.getdqyh(self, yhxxpath)
        ye = dqyh.get("ye");
        print("\n分类商品清单是：")
        if fl=="0":
            for sp in spxxlist:
                if sp.get("zt") == "有效" and ye >= sp.get("jg"):
                    sp["gm"] = "可以购买";
                    yxsplist.append(sp);
                elif sp.get("zt") == "有效" and ye < sp.get("jg"):
                    sp["gm"] = "不足";
                    yxsplist.append(sp);
                else:
                    pass;
                for sp in yxsplist:
                    print("商品编号%d,商品名称【%s】,库存数\t%d,单价\t%d,余额%s"
                          % (sp.get("spbm"), sp.get("name"), sp.get("sl"), sp.get("jg"), sp.get("gm")));
                break;
        else:
            for sp in spxxlist:
                if sp.get("fl") == fl:
                    if sp.get("zt") == "有效" and ye >= sp.get("jg"):
                        sp["gm"] = "可以购买";
                        yxsplist.append(sp);
                    elif sp.get("zt") == "有效" and ye < sp.get("jg"):
                        sp["gm"] = "不足";
                        yxsplist.append(sp);
                    else:
                        pass;
                    for sp in yxsplist:
                        print("商品编号%d,商品名称【%s】,库存数\t%d,单价\t%d,余额%s"
                              % (sp.get("spbm"), sp.get("name"), sp.get("sl"), sp.get("jg"), sp.get("gm")));
                    break;
                else:
                    continue;

        return yxsplist;

    ####################### 获取商品分类以及全部信息列表 end #######################

    # 登录后通用功能，只能自己给自己冲，不能管理员随便冲：充值的方法,参数：用户名称，充值金额，返回充值后的余额
    @check_login
    def chongzhi(self,username, yhxxpath):
        czje = int(input("请输入要充值的金额\t\t"))
        yhxx = Shopping.fxlh(self, filepath=yhxxpath)  # 从文件中获取到最新的余额进行充值
        for yh in yhxx:
            if yh.get("name") == username:
                ye_old = yh.get("ye");
                yh["ye"] = ye_old + czje;
                print("恭喜，充值成功，充值前的余额是%d,本次充值%d,充值后的余额是%d" % (ye_old, czje, yh.get("ye")))
                Shopping.xlh(self, yh, yhxxpath)
                return True

    # 通用功能，注册
    def zhuce(self, yhxxpath,gwqdpath,spxxpath, ye=0, jb="1",cs=3):
        jg = False;
        print("欢迎使用注册功能");
        username = input("请输入用户名：\t")
        userpass = input("请输入密码：\t")
        userpass2 = input("请再次输入密码：\t")
        if userpass != userpass2:
            print("两次密码不一致，请重新输入")
            return jg;
        zcxx = {'name': username, 'password': userpass, 'ye': ye, 'jb': jb}
        xlhjg = Shopping.xlh(self, zcxx, yhxxpath)
        if xlhjg:
            print("注册成功")
            log_content="{name}注册成功".format(name=username)
            Shopping.LOGGER_ALL.info(log_content)
            Shopping.login(self, yhxxpath=yhxxpath, gwqdpath=gwqdpath,spxxpath=spxxpath)  # 注册成功后自动触发登录程序
            jg = True;
        else:
            print("注册失败")
        return jg;

    # 管理员账户特有功能，增加字典类型的代码文件，双层装饰器也是分先后的，在上面的先进行判断操作

    @check_login
    @check_gly
    def xzdmdic(self,xzxxdic, wjlj):
        dmdic = Shopping.fxlh(self, wjlj)
        if any(dmdic):
            dmdic.update(xzxxdic)
        else:
            dmdic = xzxxdic
        if Shopping.xlh(self, dmdic, wjlj):
            print("新增代码成功")

    # 管理员账户特有功能，增加列表类型的基础信息文件，也可以通过判断写到上面去，但是感觉分开写的好处，少一层判断效率要高一些

    @check_login
    @check_gly
    def xzxxlist(self,xzxx, wjlj):
        xxlist = Shopping.fxlh(self, wjlj)
        if any(xxlist):
            xxlist.append(xzxx)
        else:
            xxlist = xzxx
        if Shopping.xlh(self, xxlist, wjlj):
            print("新增列表信息成功")

    # 登录方法
    def login(self,yhxxpath, gwqdpath,spxxpath, cs=3):  # 参数：输入错误的次数
        currenttime = datetime.datetime.now();
        ye = 0;

        for i in range(cs):

            if i > 0:
                print("已经输入错误%d次,还有%d机会，请重新输入!!!" % (i, cs - i))

            username = input("请输入您的用户名\t")
            userpass = input("请输入您的密码\t")
            # 从配置文件获取用户信息，如果没有信息提示是否注册，有信息提示欢迎
            userlist = Shopping.fxlh(self, filepath=yhxxpath)
            # print(type(userlist),userlist)
            namelist = []
            for u in userlist:
                namelist.append(u.get("name"))
            if username in namelist:
                # 用来处理输入一次是否正确
                for u in userlist:
                    # print(u.get("name"),u.get("password"))
                    if u.get("name") == username and u.get("password") == userpass:
                        Shopping.IS_LOGIN = username;
                        lsgw = Shopping.fxlh(self, gwqdpath)
                        # print("<%s>"%lsgw)
                        # 如果有内容就提示，没有内容就获取初始余额
                        if any(lsgw):
                            print("历史购物清单是：")
                            for dd in lsgw:
                                if dd.get("gmyh") == username:
                                    ye = dd.get("ye");
                                    # 展示历史购物清单
                                    hj = 0
                                    for yg in dd.get("sp"):
                                        spxxlist=Shopping.fxlh(self, filepath=spxxpath);
                                        for sp in spxxlist:
                                            if sp.get("spbm") == yg.get("spbm"):
                                                hj = hj + yg.get("gmsl") * sp.get("jg");
                                                print("【%s】,单价\t%d,数量\t%d,购买时间\t%s,小计\t%d" % (
                                                    sp.get("name"), sp.get("jg"), yg.get("gmsl"), yg.get("gwsj"),
                                                    yg.get("gmsl") * sp.get("jg")))
                                    print("消费合计为%d" % hj);
                                    break;
                                else:
                                    continue;
                        else:
                            ye = u.get("ye")  # 如果本地文件没有存储相关用户信息，那么就使用初始余额，否则使用文本存储的余额
                        print("尊敬的%s,欢迎你,您的账户余额是%d,今天是%s" % (username, ye, currenttime))
                        return  # 登录的信息处理完成直接退出登录的函数
                        # break;
                    else:
                        continue
            else:
                # 如果不注册分配临时用户，注册不充值或者充值小于500普通用户，充值500（含）以上高级用户
                print("账号不存在!!!")
            # 判断需要提示还是需要退出
            if i == cs - 1:
                print("账号或者密码已经错误三次，回到菜单重新选择！！！")
                return;

    def show(sjdm,dqcj):
        dqcj=dqcj + 1
        print(sjdm,dqcj)
        for dq in dqlb:
            if sjdm == dq.get("sjdm") and dq.get("cjdm") == dqcj:
                sjdm=dq.get("sjdm");
                print(dq.get("dqdm"), dq.get("dqmc"))
        return dqcj,sjdm

if __name__ == '__main__':
    dqlb = Shopping.fxlh(Shopping, filepath="/media/lipengchao/study/pycharmproject/studyProject/db/dqlb.txt")
    # dqlb=[{"dqdm":"1","dqmc":"北京","sjdm":"空","cjdm":1},{"dqdm":"11","dqmc":"东城","sjdm":"1","cjdm":2},{"dqdm":"111","dqmc":"东城街道1","sjdm":"11","cjdm":3},{"dqdm":"112","dqmc":"东城街道2","sjdm":"11","cjdm":3},{"dqdm":"12","dqmc":"西城","sjdm":"1","cjdm":2},{"dqdm":"121","dqmc":"西城街道1","sjdm":"12","cjdm":3},{"dqdm":"122","dqmc":"西城街道2","sjdm":"12","cjdm":3},{"dqdm":"2","dqmc":"陕西","sjdm":"空","cjdm":1},{"dqdm":"21","dqmc":"西安","sjdm":"2","cjdm":2},{"dqdm":"211","dqmc":"西安县城1","sjdm":"21","cjdm":3},{"dqdm":"212","dqmc":"西安县城2","sjdm":"21","cjdm":3},{"dqdm":"22","dqmc":"咸阳","sjdm":"2","cjdm":2},{"dqdm":"221","dqmc":"咸阳县城1","sjdm":"22","cjdm":3},{"dqdm":"222","dqmc":"咸阳县城2","sjdm":"22","cjdm":3}]
    dqcj=0
    sjdm="空"

    while True:
        # 展示第一级
        if dqcj==0:
            dqcj,sjdm=Shopping.show(sjdm,dqcj)
            continue
        else:
            xzsf = input("请输入您所在的地区代码,输入c退回上一层,选择完成输入y")
            if xzsf.strip().lower()=="c":
                dqcj = dqcj - 2;
                if dqcj== 3:
                    print("333333",sjdm)
                    sjdm=sjdm[:len(sjdm)]
                elif dqcj== 2:
                    sjdm = "1"
                else:
                    print("没有上级菜单")
                    sjdm = "空"

                print(sjdm)
                dqcj, sjdm = Shopping.show(sjdm, dqcj)
                continue
            elif xzsf.strip().lower()=="y":
                break;
            else:
                 dqcj,sjdm=Shopping.show(xzsf, dqcj)
                 continue;