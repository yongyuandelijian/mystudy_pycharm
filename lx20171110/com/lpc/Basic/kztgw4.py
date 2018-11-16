'''
主体：购物车小程序练习
需求：1 启动时提示拥有的钱数
     2 显示商品列表
     3 可以重复选择购买的商品
     4 购买时判断余额是否够用，够用直接扣款，不够用提示余额不足，显示余额可以购买的商品列表
     5 允许用户主动退出购买，退出时显示余额和购物清单小票
新增需求： 1 允许多用户登录，《如果该用户上次已经登录，则可以查看购买历史，为了练习我们使用json来进行序列化（必须要有购买时间）》，以及自己余额，并且可以充值
         2 商品需要按照分类来进行展示购买，目前设定为两级菜单
20181017新增需求，1 改造为类以及类的各种函数
                2 商品信息以及用户信息存储到文件中，
                3 新增用户修改密码功能，以及注册功能
                4 分为普通用户和高级用户，管理员用户，购买到一定的钱数，就可以变成高级用户
                    普通用户权限：登录，注册，修改密码，查看自己的历史购买记录，查看所有商品，只能按原价购买
                    高级用户：除了普通用户权限外，可以按照打折价格购买商品
                    管理员用户：除了具备上面所有的权限外，还具备查看用户信息的权限，并且可以根据用户信息去搜索
                5 用设计数据库表的模式去设计文本存储的内容
                6 设计的所有功能，除了使用注册和随便看看功能，不需要验证是否登录，其他所有功能，充值，查看历史清单，购物，都要已经登录的状态验证，
                7 新增查看所有打折商品功能

20181025 新增需求：1 商城自己的用户，购物结算，当钱不够或者充钱的时候，需要通过银行验证调用银行信用卡的额度来购买或者充值，如果金额不足给出提示，充足则进行充值
                 2 从欠款之日开始计算，如果欠款利息超过欠款的本金的话，冻结账户
                 3 每个月22号为出账期，十号为还款日，过期未还的话，按照欠款总额的万分之五每日计息
                 4 用户间可以转账，但是转账按照提现的规则进行收费，记录每月日常消费流水（日志info）
                 5 提供还款接口
                 6 可以提现，但是只能提取剩余额度的50%，并且要收取提取额的百分五手续费
                 7 ATM记录操作日志（日志debug）
                 7 银行要拥有自己的账户存储，可以添加用户，增加余额等功能
                 3 分五个级别记录日志


日期：20181018
设计原则：1 设计文件操作，我们也可以设计成和数据库一样的操作方式来设计文件夹的文本
        2 凡是动了基础数据的，必须在函数内开始进行取出来，结束时，放回文件

作者：aaa
'''
import datetime
import json
import os
import sys
import requests


class Scgw(object):
    IS_LOGIN = False;  # 用来记录登录状态,如果为False就是未登录，如果为用户名称就是已经登录

    ####################### 装饰器函数 start #######################
    # 检查是否登录
    def check_login(func):
        def inner(*args, **kwargs):
            result = ""
            if Scgw.IS_LOGIN:
                result = func(*args, **kwargs)
            else:
                print("您没有登录或权限不足，无法使用本功能")
            return result

        return inner

    # 检查是否是管理员，其实这个地方同时判断了是否登录和登录后是不是管理员，为了练习所以后面可能有的函数被两个都装饰了
    def check_gly(func):
        def inner(*args,**kwargs):
            result="";
            if Scgw.IS_LOGIN and Scgw.getdqyh.get("jb")=="3":
                result=func(*args,**kwargs);
            else:
                print("您没有登录，或者登录的账号不是管理员账户，无法使用本功能！！！")
            return result
        return inner;

    ####################### 获取当前用户余额 检查是否登录 start #######################
    @check_login
    def getdqyh(self, yhxxpath):
        yhlb = Scgw.fxlh(self, filepath=yhxxpath)
        for yh in yhlb:
            if yh.get("name") == Scgw.IS_LOGIN:
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
        lsnr = Scgw.fxlh(self,filepath)
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
        jg = Scgw.wjcz_zx(self,filepath, jsonstr)
        return jg;

    def fxlh(self,filepath):
        # 判断下路径文件夹和文件是否存在，不存在就创建
        wjnr = '';
        if os.path.exists(filepath):
            jsonstr = Scgw.wjcz_zd(self,filepath)
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
        Scgw.xlh(self,userlist, yhxxpath)

        # 定义商品字典，每个商品七个信息，编号，名称，价格，数量,分类，是否有效，当前余额是否可以购买最少1个商品，这个属性纯属为了练习，没啥实际意义
        splist1 = {"spbm": 1, "name": "商品1", "jg": 20, "sl": 23, "zt": "1", "fl": "1", "gm": ""}
        splist2 = {"spbm": 2, "name": "商品2", "jg": 32, "sl": 2, "zt": "1", "fl": "2", "gm": ""}
        splist3 = {"spbm": 3, "name": "商品3", "jg": 2, "sl": 9, "zt": "1", "fl": "3", "gm": ""}
        splist4 = {"spbm": 4, "name": "商品4", "jg": 59, "sl": 143, "zt": "1", "fl": "3", "gm": ""}
        splist5 = {"spbm": 5, "name": "商品4", "jg": 123, "sl": 532, "zt": "1", "fl": "2", "gm": ""}
        splist6 = {"spbm": 6, "name": "商品4", "jg": 92, "sl": 1345, "zt": "1", "fl": "3", "gm": ""}
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
        Scgw.xlh(self,sdlist, spxxpath)

        # 代码部分
        # 公用代码状态
        ztdic = {"0": "无效", "1": "有效"}
        Scgw.xlh(self,ztdic, ztpath)
        # 商品分类代码
        spfldic = {"1": "分类1", "2": "分类2", "3": "分类3"}
        Scgw.xlh(self,spfldic, spflpath)
        # 用户类别代码
        yhjbdic = {"0":"临时用户","1": "普通用户", "2": "高级用户", "3": "管理员用户"}
        Scgw.xlh(self,yhjbdic, yhjbpath)
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
        dqyh = Scgw.getdqyh(self,yhxxpath)
        ye=dqyh.get("ye");
        print("\n本次已购清单是：")
        gwqdlist=Scgw.fxlh(self,filepath=gwqdpath)
        # 根据需要购物的商品字典设计为{商品编码，购买数量，购物时间}
        if len(gwqdlist) == 0:
            print("您没有购买任何商品，当前余额为%d" % ye)
            return
        else:
            for yg in gwqdlist:
                spxxlist = Scgw.fxlh(self, filepath=spxxpath)
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
        dqyh = Scgw.getdqyh(self, yhxxpath)
        ye = dqyh.get("ye");
        gmsp = {}; # 根据需要 购物的商品字典设计为{商品编码，购买数量，购物时间}
        gmspbm = input("\n请选择你需要的商品（输入编号即可,输入n退出,输入c进行账户充值）\n");
        if gmspbm.lower() == "n":
            print("感谢您的购物，期待您的下次光临！！！")
            Scgw.sy(self,yhxxpath=yhxxpath,spxxpath=spxxpath,gwqdpath=gwqdpath)
            sys.exit();
        elif gmspbm.lower() == "c":
            czje = float(input("请输入充值金额\t"));
            Scgw.chuzhi(self,Scgw.IS_LOGIN,czje,yhxxpath)
        else:
            gmspbm = int(gmspbm);
            spxxlist=Scgw.fxlh(self,filepath=spxxpath)
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
                        Scgw.gwqd(self, gmsp,gwqdlist= gwqdlist); # 将选购一次的商品放入本次购物小票
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
        spfldic=Scgw.fxlh(self,filepath=spflpath)
        for key in spfldic:
            print("%d\t\t\t%s\t\t\t\t%d" % (key, spfldic.get("key")))
        flbm = input("选择您想要浏览的商品分类代码查看商品,0查看全部\t")
        spxxlist=Scgw.fxlh(self,filepath=spxxpath)
        # 获取商品是否可购买状态，从业务上来是没太大必要，这里主要是对程序扩展性的练习
        yxsplist = Scgw.getyxspqd(self,spxxlist, flbm);
        return yxsplist;


    # 获取当前有效商品列表，增加程序健壮性
    def getyxspqd(self, spxxlist, fl="0"):
        yxsplist=[];
        dqyh = Scgw.getdqyh(self, yhxxpath)
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
    def chuzhi(self,username, je, yhxxpath):
        yhxx = Scgw.fxlh(self,filepath=yhxxpath)  # 从文件中获取到最新的余额进行充值
        for yh in yhxx:
            if yh.get("name") == username:
                ye_old = yh.get("ye");
                yh["ye"] = ye_old + je;
                print("恭喜，充值成功，充值前的余额是%d,本次充值%d,充值后的余额是%d" % (ye_old, je, yh.get("ye")))
                Scgw.xlh(self,yh, yhxxpath)
                return True

    # 通用功能，注册
    def zhuce(self,username, password, userpass2, yhxxpath, cs=3, ye=0, jb="1"):
        jg = False;
        if password != userpass2:
            print("两次密码不一致，请重新输入")
            return jg;
        zcxx = {'name': username, 'password': password, 'ye': ye, 'jb': jb}
        xlhjg = Scgw.xlh(self,zcxx, yhxxpath)
        if xlhjg:
            print("注册成功")
            Scgw.login(self,cs, yhxxpath)  # 注册成功后自动触发登录程序
            jg = True;
        else:
            print("注册失败，请刷新后重新注册")
        return jg;

    # 管理员账户特有功能，增加字典类型的代码文件，双层装饰器也是分先后的，在上面的先进行判断操作

    @check_login
    @check_gly
    def xzdmdic(self,xzxxdic, wjlj):
        dmdic = Scgw.fxlh(self,wjlj)
        if any(dmdic):
            dmdic.update(xzxxdic)
        else:
            dmdic = xzxxdic
        if Scgw.xlh(self,dmdic, wjlj):
            print("新增代码成功")

    # 管理员账户特有功能，增加列表类型的基础信息文件，也可以通过判断写到上面去，但是感觉分开写的好处，少一层判断效率要高一些

    @check_login
    @check_gly
    def xzxxlist(self,xzxx, wjlj):
        xxlist = Scgw.fxlh(self,wjlj)
        if any(xxlist):
            xxlist.append(xzxx)
        else:
            xxlist = xzxx
        if Scgw.xlh(self,xxlist, wjlj):
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
            userlist = Scgw.fxlh(self,filepath=yhxxpath)
            # print(type(userlist),userlist)
            namelist = []
            for u in userlist:
                namelist.append(u.get("name"))
            if username in namelist:
                # 用来处理输入一次是否正确
                for u in userlist:
                    # print(u.get("name"),u.get("password"))
                    if u.get("name") == username and u.get("password") == userpass:
                        Scgw.IS_LOGIN = username;
                        lsgw = Scgw.fxlh(self,gwqdpath)
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
                                        spxxlist=Scgw.fxlh(self,filepath=spxxpath);
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