'''
主体：购物车小程序练习
需求：1 启动时提示拥有的钱数
     2 显示商品列表
     3 可以重复选择购买的商品
     4 购买时判断余额是否够用，够用直接扣款，不够用提示余额不足，显示余额可以购买的商品列表
     5 允许用户主动退出购买，退出时显示余额和购物清单小票
新增需求： 1 允许多用户登录，《如果该用户上次已经登录，则可以查看购买历史，为了练习我们使用json来进行序列化（必须要有购买时间）》，以及自己余额，并且可以充值
         2 商品需要按照分类来进行展示购买，目前设定为两级菜单
日期：20181010
评价：勉强算是通过了，总的来说还是有很多问题，但是给我感触最深的就是，文件操作真的是不如数据库方便，是非常麻烦的要维护数据之间的依赖关系，
而数据库只要一次成型，后续只需要根据需要去修改自己需要的内容即可，这种东西开发效率极低，功能越写越多的时候，需要考虑之前的功能就越多，
造成的调试花费的时间越久。
作者：aaa
'''
import datetime
import json
import os
from common import text_utils

# 定义商品字典，每个商品六个信息，编号，名称，价格，数量，是否有效，当前余额是否可以购买最少1个商品，这个属性纯属为了练习，没啥实际意义

splist1 = {"spbm": 1, "name": "商品1", "jg": 20, "sl": 23, "zt": "有效", "gm": ""}
splist2 = {"spbm": 2, "name": "商品2", "jg": 32, "sl": 2, "zt": "有效", "gm": ""}
splist3 = {"spbm": 3, "name": "商品3", "jg": 2, "sl": 9, "zt": "有效", "gm": ""}
splist4 = {"spbm": 4, "name": "商品4", "jg": 59, "sl": 143, "zt": "有效", "gm": ""}
SPLB=[splist1, splist2, splist3, splist4]
# 分类列表
spfllist1 = {"flbm": 1, "flmc": "分类1", "sp": [splist2, splist1]}
spfllist2 = {"flbm": 2, "flmc": "分类2", "sp": [splist3]}
spfllist3 = {"flbm": 3, "flmc": "分类3", "sp": [splist4]}
# 商店列表，展示所有商品信息
SDLIST = []
SDLIST.append(spfllist1)
SDLIST.append(spfllist2)
SDLIST.append(spfllist3)

# 已购物品小票清单,只存储商品id
gwqdlist = []
# ygsp={"spbm":2,"gmsl":3}
# ygsp1={"spbm":3,"gmsl":1}
# gwqdlist.append(ygsp)
# gwqdlist.append(ygsp1)
# 订单，存储每一个用户一次购物的信息
qdinfo={}
qdlist=[]  # 存放反序列化取出来的历史记录，用来在登录的时候进行展示
# 想要展示给客户的有效商品列表
yxsplist = []

xiaoming = {"name": "xiaoming", "password": "xiaoming", "ye": 500}
xiaoding = {"name": "xiaoding", "password": "12", "ye": 300}
xiaobai = {"name": "xiaobai", "password": "1", "ye": 100}
userlist = (xiaoming, xiaoding, xiaobai)
# 定义序列化和反序列化的存储读取路径
filepath = '/media/lipengchao/study/pycharmproject/studypc/txt/gwqd.txt'

# 将传入的对象转为json并进行序列化
def xlh(gwqd,filepath):
    # print(gwqd)
    # 如果现有内容，讲内容取出来，追加到列表中，如果没有就直接追加当前对象就行了，这样看，操作文件的时候，相互关系太复杂真的是比操作数据库复杂好多，数据的相互关系，全部靠程序进行维护
    lsnr=fxlh(filepath)
    if any(lsnr):
        # print(type("111111",lsnr))
        qdlist=lsnr
    qdlist.append(gwqd)
    gwqdjson=json.dumps(qdlist)
    # 文件没有的话会自动创建，文件夹没有的话，需要自己处理,在调用之前进行了手动处理
    text_utils.writeFile(filepath,gwqdjson)
    # print(gwqdjson)
    return filepath

def fxlh(filepath):
    jsonstr=text_utils.readFile(filepath)
    # print('<%s>'%jsonstr)
    qdlist=''
    if type(jsonstr)==str and jsonstr.strip()!="":
        # print(type('是一个字符串'))
        qdlist = json.loads(s=jsonstr, encoding="utf-8")
    else:
        print("不是一个字符串或者为空",jsonstr)
    # print(qdlist)
    return qdlist

# 提示当前拥有钱数和购物清单的方法
def sy(splist,ye):
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
def getspfl(ye):
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
def getspqd(ye,fl=0):
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
def gwqd(ygsp):
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




# 登录方法，需要一个用户列表，为了练习，我们在这里使用元组

def login(cs): # 参数：输入错误的次数
    # print(username,userpasss)
    currenttime=datetime.datetime.now()
    ye=0

    for i in range(cs):

        if i > 0:
            print("已经输入错误%d次,还有%d机会，请重新输入!!!" % (i, cs - i))

        username = input("请输入您的用户名\t")
        userpass = input("请输入您的密码\t")
        # 用来处理输入一次是否正确
        for u in userlist:
            # print(u)
            if u.get("name") == username and u.get("password") == userpass:
                # print(os.path.basename(filepath))
                dirname=os.path.dirname(filepath)
                # 测试说明，这个方法是可以自动创建子目录
                if not os.path.exists(dirname):
                    os.mkdir(filepath)
                # 连带文件一起判断，文件和目录不存在就创建
                if not os.path.exists(filepath):
                    os.system(r"touch {}".format(filepath)) # 调用系统命令来创建文件
                lsgw=fxlh(filepath)
                # print("<%s>"%lsgw)
                # 如果有内容就提示，没有内容就获取初始余额
                print("历史购物清单是：")
                if any(lsgw):
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
                splist = getspfl(ye)
                while True:
                    ye=gw(username,splist, ye)  # 这一步会处理充值的金额，所以进行返回余额
                    choice = input("是否继续购买（y/n）")
                    if choice.lower() != 'y':
                        print("感谢您的购物，期待您的下次光临！！！")
                        ye=sy(splist,ye) # 这一步会进行结账，所以我们进行返回余额
                        u["ye"]=ye
                        qdinfo["gmyh"] = username
                        qdinfo["ddsj"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        qdinfo["sp"] = gwqdlist
                        qdinfo["ye"]=ye
                        xlh(qdinfo, filepath)
                        return
                break
            else:
                continue

        # 判断需要提示还是需要退出
        if i == cs-1:
            print("账号或者密码已经错误三次，程序退出！！！")
            return


# 充值的方法,参数：用户名称，充值金额，返回充值后的余额
def cz(username,je):
    for zh in userlist:
        if zh.get("name")==username:
            ye_old=zh.get("ye")
            zh["ye"]=zh.get("ye")+je
            print("恭喜，充值成功，充值前的余额是%d,本次充值%d,充值后的余额是%d"%(ye_old,je,zh.get("ye")))
            print(zh)
            return zh.get("ye")






def main():

    login(3)


if __name__ == '__main__':
    main()

    # xlh(spfllist1.get("sp"))
    # fxlh(filepath)