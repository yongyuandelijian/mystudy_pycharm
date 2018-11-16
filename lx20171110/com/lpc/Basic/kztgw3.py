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

日期：20181018
设计原则：1 设计文件操作，我们也可以设计成和数据库一样的操作方式来设计文件夹的文本
        2 凡是动了基础数据的，必须在函数内开始进行取出来，结束时，放回文件

作者：aaa
'''
import datetime
import json
import os


IS_LOGIN=False # 用来记录登录状态,如果为False就是未登录，如果为用户名称就是已经登录

####################### 装饰器函数 检查是否登录 start #######################
def check(func):
    def inner(*args,**kwargs):
        result=""
        if IS_LOGIN:
            result=func(*args,**kwargs)
        else:
            print("您没有登录或权限不足，无法使用本功能")
        return result
    return inner


####################### 文件操作的方法 start #######################
# 文件读取的方法
def wjcz_zd(wjlj):
    with open(file=wjlj,mode="r",encoding="utf-8") as zdwj:
        jsonstr=zdwj.read()
        return jsonstr

# 文件写入的方法
def wjcz_zx(wjlj,jsonContent):
    with open(file=wjlj,mode="w",encoding="utf-8") as zxwj:
        zxwj.write(jsonContent)
        return True

####################### 文件操作的方法 end #######################


####################### 序列化操作方法 start #######################

# 将传入的对象转为json并进行序列化
def xlh(xlhnr,filepath):
    # print(gwqd)
    wjnr=[]
    # 如果现有内容，追加到列表中，如果没有就直接追加当前对象就行了
    lsnr = fxlh(filepath)
    if any(lsnr):
        wjnr = lsnr
        # 信息表获取到的是一个列表,代码表获取到的是一个字典
        if type(wjnr)==list:        # 注意不是字符串
            wjnr.append(xlhnr) # 列表是将新加的字典作为一个元素
        if type(wjnr)==dict:
            wjnr.update(xlhnr) # 字典是将新加的字典更新进去
    else:
        wjnr=xlhnr

    jsonstr = json.dumps(wjnr)
    jg=wjcz_zx(filepath, jsonstr)
    return jg

def fxlh(filepath):
    # 判断下路径文件夹和文件是否存在，不存在就创建
    wjnr = ''
    if os.path.exists(filepath):
        jsonstr = wjcz_zd(filepath)
        if type(jsonstr) == str and jsonstr.strip() != "":
            wjnr = json.loads(s=jsonstr, encoding="utf-8")
        else:
            print("文件没有内容！！！")
    else:
        # 进入之后两种情况，一种是文件和目录都不存在，一种只是文件不存在
        wjml=os.path.dirname(filepath)
        if not os.path.exists(wjml):
            os.makedirs(wjml)
        # wjm=os.path.basename(filepath) 获取文件名，经过测试并没有什么用
        os.mknod(filepath) # 文件是肯定不存在，创建文件
        print(filepath+"目录或者文件不存在，已经自动创建成功")
    return wjnr

####################### 序列化操作方法 end #######################


####################### 初始化数据操作 start #######################
def csh(yhxxpath,spxxpath,spflpath,yhjbpath,ztpath):
    # 初始化一些信息，后续只能通过调用新增信息
    # 用户基础信息
    xiaoming = {"name": "xiaoming", "password": "xiaoming", "ye": 500, "jb": "1","zt":"1"}
    xiaoding = {"name": "xiaoding", "password": "12", "ye": 300, "jb": "2","zt":"1"}
    xiaobai = {"name": "xiaobai", "password": "1", "ye": 100, "jb": "3","zt":"1"}
    userlist = [xiaoming, xiaoding, xiaobai]
    # print("要初始化的用户信息是：", userlist)
    xlh(userlist, yhxxpath)


    # 定义商品字典，每个商品七个信息，编号，名称，价格，数量,分类，是否有效，当前余额是否可以购买最少1个商品，这个属性纯属为了练习，没啥实际意义
    splist1 = {"spbm": 1, "name": "商品1", "jg": 20, "sl": 23, "zt": "1", "fl": "1", "gm": ""}
    splist2 = {"spbm": 2, "name": "商品2", "jg": 32, "sl": 2, "zt": "1", "fl": "2", "gm": ""}
    splist3 = {"spbm": 3, "name": "商品3", "jg": 2, "sl": 9, "zt": "1", "fl": "3", "gm": ""}
    splist4 = {"spbm": 4, "name": "商品4", "jg": 59, "sl": 143, "zt": "1", "fl": "3", "gm": ""}
    splist5 = {"spbm": 5, "name": "商品4", "jg": 59, "sl": 532, "zt": "1", "fl": "2", "gm": ""}
    splist6 = {"spbm": 6, "name": "商品4", "jg": 59, "sl": 1345, "zt": "1", "fl": "3", "gm": ""}
    SPLB = [splist1, splist2, splist3, splist4,splist5,splist6]
    # 商店列表，展示所有商品信息
    sdlist = []
    sdlist.append(splist1)
    sdlist.append(splist2)
    sdlist.append(splist3)
    sdlist.append(splist4)
    print("要初始化的商品信息是：", sdlist)
    xlh(sdlist, spxxpath)

    # 代码部分
    # 公用代码状态
    ztdic = {"0": "无效", "1": "有效"}
    xlh(ztdic,ztpath)
    # 商品分类代码
    spfldic = {"1": "分类1", "2": "分类2", "3": "分类3"}
    xlh(spfldic,spflpath)
    # 用户类别代码
    yhjbdic = {"1": "普通用户", "2": "高级用户", "3": "管理员用户"}
    xlh(yhjbdic,yhjbpath)
####################### 初始化数据操作 end #######################


####################### 提示当前拥有钱数和购物清单的方法 end #######################

####################### 提示当前拥有钱数和购物清单的方法 end #######################
# 提示当前拥有钱数和购物清单的方法
def sy(splist,ye,gwqdlist):
    hj=0
    print("\n本次已购清单是：")
    if len(gwqdlist)==0:
        print("您没有购买任何商品，当前余额为%d"%ye)
        return
    else:
        for yg in gwqdlist:
            for sp in splist:
                if sp.get("spbm")==yg.get("spbm"):
                    hj=hj+yg.get("gmsl")*sp.get("jg")
                    print("【%s】,单价\t%d,数量\t%d,购买时间\t%s,小计\t%d"%(sp.get("name"),sp.get("jg"),yg.get("gmsl"),yg.get("gwsj"),yg.get("gmsl")*sp.get("jg")))
    print("消费合计为%d,余额为%d"%(hj,ye-hj))
    return ye-hj

# 获取商品分类列表
def getspfl(ye,SDLIST):
    print("\n本店商品分类如下：\n")
    print("分类编码\t\t分类名称\t\t\t分类拥有商品数量")
    for spfl in SDLIST:
        print("%d\t\t\t%s\t\t\t\t%d"%(spfl.get("flbm"),spfl.get("flmc"),len(spfl.get("sp"))))
    flbm=int(input("选择您想要浏览的商品分类代码查看商品,0查看全部\t"))
    # print(flbm)
    yxsplist=getspqd(ye,flbm)
    # print(yxsplist)
    return yxsplist


# 获取当前有效商品列表，增加程序健壮性
def getspqd(ye,SDLIST,yxsplist,fl=0):
    print("\n分类商品清单是：")
    for spfl in SDLIST:
        if spfl.get("flbm")==fl:
            for sp in spfl.get("sp"):
                if sp.get("zt") == "有效" and ye >= sp.get("jg"):
                    sp["gm"] = "可以购买"
                    yxsplist.append(sp)
                elif sp.get("zt") == "有效" and ye < sp.get("jg"):
                    sp["gm"] = "不足"
                    yxsplist.append(sp)
                else:
                    pass
            for sp in yxsplist:
                print("商品编号%d,商品名称【%s】,库存数\t%d,单价\t%d,余额%s"
                      % (sp.get("spbm"), sp.get("name"), sp.get("sl"), sp.get("jg"), sp.get("gm")))
            break
        else:
            continue

    return yxsplist



# 购物的方法,传入用户名，商品列表，余额，返回当前用户余额
def gw(username,splist,ye):
    ygsp={}
    gmsp=input("\n请选择你需要的商品（输入编号即可,输入n退出,输入c进行账户充值）\n")
    if gmsp.lower()=="n":
        print("感谢您的购物，期待您的下次光临！！！")
        sy(ye)
    elif gmsp.lower()=="c":
        czje=float(input("请输入充值金额\t"))
        ye=cz(username,czje)
    else:
        gmsp=int(gmsp)
        for sp in splist:
            # 说明选择了给定列表的商品编号，我们将商品编号获取出来
            # print(sp.get("spbm"),gmsp)
            if gmsp==sp.get("spbm"):
                ygsp["spbm"]=gmsp
                gmsl=int(input("您当前要购买的请输入您要购买的数量\n"))
                ygsp["gmsl"]=gmsl
                if ye<sp.get("jg")*gmsl:
                    print("对不起，您的余额不足 ！！！")
                    break
                else:
                    ygsp["gwsj"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    gwqd(ygsp)
                break
            else:
                continue
    return ye
    # print(ygsp)



# 处理购物清单的方法,传入购物商品对象，print(ygsp) 处理已购买商品小票，如果商品是之前已经购买过就增加数量，否则我们进行追加
# 后来我们发现，要展示当前用户的之前购物清单，还需要记录当前购买的用户id,所以我们需要重新设置这个购物清单的格式，修改为一个字典
# gwqd  {"购买用户":"","购买时间":"","sp":[当前的购物清单]}
def gwqd(ygsp,gwqdlist):
    ygspid = []
    for yg_old in gwqdlist:
        ygspid.append(yg_old.get("spbm"))

    if ygsp.get("spbm") not in ygspid:
        # print("输入的商品还没有购买，进行追加")
        gwqdlist.append(ygsp)
    else:
        for yg_old in gwqdlist:
            # print(yg_old.get("spbm"))

            if yg_old.get("spbm") == ygsp.get("spbm"):
                yg_old["gmsl"] = yg_old.get("gmsl") + ygsp.get("gmsl")
                # 这里更新为最后一次修改的时间，如果需要保留原始的时间，注销下面这句代码
                yg_old["gwsj"]=ygsp.get("gwsj")
                break
            else:
                continue


# 登录后通用功能，只能自己给自己冲，不能管理员随便冲：充值的方法,参数：用户名称，充值金额，返回充值后的余额
@check
def chuzhi(username,je,yhxxpath):
    yhxx=fxlh(filepath=yhxxpath)    # 从文件中获取到最新的余额进行充值
    for yh in yhxx:
        if yh.get("name")==username:
            ye_old=yh.get("ye")
            yh["ye"]=ye_old+je
            print("恭喜，充值成功，充值前的余额是%d,本次充值%d,充值后的余额是%d"%(ye_old,je,yh.get("ye")))
            xlh(yh,yhxxpath)
            return True
        

# 通用功能，注册
def zhuce(username,password,userpass2,yhxxpath,cs=3,ye=0,jb="1"):
    jg=False
    if password != userpass2:
        print("两次密码不一致，请重新输入")
        return jg
    zcxx={'name': username, 'password': password, 'ye': ye, 'jb': jb}
    xlhjg=xlh(zcxx,yhxxpath)
    if xlhjg:
        print("注册成功")
        login(cs,yhxxpath) # 注册成功后自动触发登录程序
        jg=True
    else:
        print("注册失败，请刷新后重新注册")
    return jg

# 管理员账户特有功能，增加字典类型的代码文件
@check
def xzdmdic(xzxxdic,wjlj):
    dmdic=fxlh(wjlj)
    if any(dmdic):
        dmdic.update(xzxxdic)
    else:
        dmdic=xzxxdic
    if xlh(dmdic,wjlj):
        print("新增代码成功")

# 管理员账户特有功能，增加列表类型的基础信息文件，也可以通过判断写到上面去，但是感觉分开写的好处，少一层判断效率要高一些
@check
def xzxxlist(xzxx,wjlj):
    xxlist=fxlh(wjlj)
    if any(xxlist):
        xxlist.append(xzxx)
    else:
        xxlist=xzxx
    if xlh(xxlist,wjlj):
        print("新增列表信息成功")

# 登录方法，需要一个用户列表，为了练习，我们在这里使用元组
def login(yhxxpath,gwqdpath,cs=3): # 参数：输入错误的次数
    IS_LOGIN=False
    currenttime=datetime.datetime.now()
    ye=0

    for i in range(cs):

        if i > 0:
            print("已经输入错误%d次,还有%d机会，请重新输入!!!" % (i, cs - i))

        username = input("请输入您的用户名\t")
        userpass = input("请输入您的密码\t")
        # 从配置文件获取用户信息，如果没有信息提示是否注册，有信息提示欢迎
        userlist=fxlh(yhxxpath)
        # print(type(userlist),userlist)
        namelist=[]
        for u in userlist:
            namelist.append(u.get("name"))
        if username in namelist:
            # 用来处理输入一次是否正确
            for u in userlist:
                # print(u.get("name"),u.get("password"))
                if u.get("name") == username and u.get("password") == userpass:
                    IS_LOGIN=username
                    lsgw = fxlh(gwqdpath)
                    # print("<%s>"%lsgw)
                    # 如果有内容就提示，没有内容就获取初始余额
                    if any(lsgw):
                        print("历史购物清单是：")
                        for dd in lsgw:
                            if dd.get("gmyh")==username:
                                ye=dd.get("ye")
                                # 展示历史购物清单
                                hj=0
                                for yg in dd.get("sp"):
                                    for sp in SPLB:
                                        if sp.get("spbm") == yg.get("spbm"):
                                            hj = hj + yg.get("gmsl") * sp.get("jg")
                                            print("【%s】,单价\t%d,数量\t%d,购买时间\t%s,小计\t%d" % (
                                            sp.get("name"), sp.get("jg"), yg.get("gmsl"), yg.get("gwsj"),
                                            yg.get("gmsl") * sp.get("jg")))
                                print("消费合计为%d" %hj)
                                # print("%s历史购物json是%s" % (dd.get("gmyh"), dd.get("sp")))
                                break
                            else:
                                continue
                    else:
                        ye = u.get("ye")  # 如果本地文件没有存储相关用户信息，那么就使用初始余额，否则使用文本存储的余额
                    print("尊敬的%s,欢迎你,您的账户余额是%d,今天是%s" % (username, ye, currenttime))
                    return IS_LOGIN# 登录的信息处理完成直接退出登录的函数
                    # break
                else:
                    continue
        else:
            # 如果不注册分配临时用户，注册不充值或者充值小于500普通用户，充值500（含）以上高级用户
            print("账号不存在!!!")
        # 判断需要提示还是需要退出
        if i == cs-1:
            print("账号或者密码已经错误三次，回到菜单重新选择！！！")
            return
# 流程
def main():
    # 登录次数限制
    login_limit = 3
    # 已购物品小票清单,只存储商品id
    gwqdlist = []
    # 订单，存储每一个用户一次购物的信息
    qdinfo = {}
    qdlist = []  # 存放反序列化取出来的历史记录，用来在登录的时候进行展示
    # 想要展示给客户的有效商品列表
    yxsplist = []

    # 定义序列化和反序列化的存储读取路径
    filepath = os.path.abspath("../wjj")
    gwqdpath = filepath + "/gwqd.txt"
    yhxxpath = filepath + "/yhxx.txt"
    spxxpath = filepath + "/spxx.txt"
    spflpath = filepath + "/spfl.txt"
    yhjbpath = filepath + "/yhjb.txt"
    ztpath = filepath + "/zt.txt"

    # 初始化系统基本信息，初始运行一次
    # csh(yhxxpath=yhxxpath,spxxpath=spxxpath,spflpath=spflpath,yhjbpath=yhjbpath,ztpath=ztpath)
    while True:
        # 提示系统功能信息
        print('''
        功能菜单：1 注册 
                2 登录
                3 充值
                4 查看历史购物记录
                5 查看所有商品
                6 新增商品
                7 新增商品分类
                8 新增用户级别
                9 新增状态
                10 查看当前打折商品
                11 修改商品信息
                12 注销当前登录账户
                13 退出系统
        ''')
        userchoice=input("请输入您需要的操作功能编号\t\t")
        if userchoice=="1":
            print("欢迎使用注册功能")
            username = input("请输入用户名：\t")
            userpass = input("请输入密码：\t")
            userpass2= input("请再次输入密码：\t")
            zhuce(username=username, password=userpass,userpass2=userpass2, yhxxpath=yhxxpath,cs=login_limit)
            continue
        elif userchoice=="2":
            print("欢迎使用登录功能")
            login(yhxxpath=yhxxpath,gwqdpath=gwqdpath,cs=login_limit)
            continue
        elif userchoice=="3":
            czje = int(input("请输入要充值的金额\t\t"))
            chuzhi(username=IS_LOGIN,je=czje,yhxxpath=yhxxpath)
            continue
        elif userchoice=="4":
            查看历史购物记录
        elif userchoice=="5":
            查看所有商品
        elif userchoice=="6":
            新增商品
        elif userchoice=="7":
            spfl={}
            flbm=input("输入新增商品分类编码")
            flmc=input("输入新增商品分类名称")
            if flbm.strip() and flmc.strip():
                spfl={flbm:flmc}
                xzdmdic(xzxxdic=spfl,wjlj=spflpath)
            continue
        elif userchoice=="8":
            yhjb = {}
            jbbm = input("输入新增用户级别编码")
            jbmc = input("输入新增用户级别名称")
            if jbbm.strip() and jbmc.strip():
                yhjb = {jbbm: jbmc}
                xzdmdic(xzxxdic=yhjb, wjlj=yhjbpath)
            continue
        elif userchoice=="9":
            zt = {}
            ztbm = input("输入新增状态编码")
            ztmc = input("输入新增状态名称")
            if ztbm.strip() and ztmc.strip():
                zt = {ztbm: ztmc}
                xzdmdic(xzxxdic=zt, wjlj=ztpath)
            continue
        elif userchoice=="10":
            查看当前打折商品
        elif userchoice=="11":
            修改商品信息
        elif userchoice=="12":
            注销当前登录账户
        elif userchoice=="13":
            choice = input("确实要退出系统吗（y/n）")
            if choice=="y":
                break
            else:
                continue
        else:
            查看所有商品




    '''
    # 可以输入错误的次数
    
    splist = getspfl(ye)
    while True:
        ye = gw(username, splist, ye)  # 这一步会处理充值的金额，所以进行返回余额
        choice = input("是否继续购买（y/n）")
        if choice.lower() != 'y':
            print("感谢您的购物，期待您的下次光临！！！")
            ye = sy(splist, ye)  # 这一步会进行结账，所以我们进行返回余额
            u["ye"] = ye
            qdinfo["gmyh"] = username
            qdinfo["ddsj"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            qdinfo["sp"] = gwqdlist
            qdinfo["ye"] = ye
            xlh(qdinfo, filepath)
            return
    '''

if __name__ == '__main__':
    main()