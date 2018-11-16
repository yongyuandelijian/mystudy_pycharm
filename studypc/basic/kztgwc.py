'''
主体：购物车小程序练习
需求：1 启动时提示拥有的钱数
     2 显示商品列表
     3 可以重复选择购买的商品
     4 购买时判断余额是否够用，够用直接扣款，不够用提示余额不足，显示余额可以购买的商品列表
     5 允许用户主动退出购买，退出时显示余额和购物清单小票
日期：20181009
作者：aaa
'''

# 定义商品字典，每个商品六个信息，编号，名称，价格，数量，是否有效，当前余额是否可以购买最少1个商品，这个属性纯属为了练习，没啥实际意义
splist1={"spbm":1,"name":"商品1","jg":20,"sl":23,"zt":"有效","gm":""}
splist2={"spbm":2,"name":"商品2","jg":32,"sl":2,"zt":"有效","gm":""}
splist3={"spbm":3,"name":"商品3","jg":2,"sl":9,"zt":"有效","gm":""}
splist4={"spbm":4,"name":"商品4","jg":59,"sl":143,"zt":"有效","gm":""}
# 商店列表，展示所有商品信息
sdlist=[]
sdlist.append(splist1)
sdlist.append(splist2)
sdlist.append(splist3)
sdlist.append(splist4)

# 已购物品小票清单,只存储商品id
gwqdlist=[]
ygsp={"spbm":2,"gmsl":3}
ygsp1={"spbm":3,"gmsl":1}
gwqdlist.append(ygsp)
gwqdlist.append(ygsp1)
# 钱包钱数
qs=500

# 想要展示给客户的有效商品列表
yxsplist=[]
# 提示当前拥有钱数和购物清单的方法
def sy(ye):
    hj=0
    print("\n已购清单是：")
    if len(gwqdlist)==0:
        print("您没有购买任何商品，当前余额为%d"%ye)
        return
    else:
        for yg in gwqdlist:
            for sp in sdlist:
                if sp.get("spbm")==yg.get("spbm"):
                    hj=hj+yg.get("gmsl")*sp.get("jg")
                    print("【%s】,数量\t%d,单价\t%d,小计\t%d"%(sp.get("name"),sp.get("jg"),yg.get("gmsl"),yg.get("gmsl")*sp.get("jg")))
    print("消费合计为%d,余额为%d"%(hj,ye-hj))
# 获取当前有效商品列表，增加程序健壮性
def getspqd(ye):
    print("\n当前余额是：%d,商店商品清单是："%ye)
    for sp in sdlist:
        if sp.get("zt")=="有效" and ye>=sp.get("jg"):
            sp["gm"]="可以购买"
            yxsplist.append(sp)
        elif sp.get("zt")=="有效" and ye<sp.get("jg"):
            sp["gm"]="不足"
            yxsplist.append(sp)
        else:
            pass
    for sp in yxsplist:
        print("商品编号%d,商品名称【%s】,库存数\t%d,单价\t%d,余额%s"
              % (sp.get("spbm"),sp.get("name"),sp.get("sl"),sp.get("jg"),sp.get("gm")))
    return yxsplist





# 购物的方法
def gw(splist,ye):
    ygsp={}
    gmsp=int(input("\n请选择你需要的商品（输入编号即可）\n"))
    for sp in splist:
        # 说明选择了给定列表的商品编号，我们将商品编号获取出来
        # print(sp.get("spbm"),gmsp)
        if gmsp==sp.get("spbm"):
            ygsp["spbm"]=gmsp
            gmsl=int(input("您当前要购买的请输入您要购买的数量\n"))
            ygsp["gmsl"]=gmsl
            if ye<sp.get("jg")*gmsl:
                print("您的余额不足 ！！！")
                break
            break
        else:
            continue
    # print(ygsp) 处理已购买商品小票，如果商品是之前已经购买过就增加数量，否则我们进行追加
    ygspid=[]
    for yg_old in gwqdlist:
        ygspid.append(yg_old.get("spbm"))

    if ygsp.get("spbm") not in ygspid:
        # print("输入的商品还没有购买，进行追加")
        gwqdlist.append(ygsp)
    else:
        for yg_old in gwqdlist:
            # print(yg_old.get("spbm"))

            if yg_old.get("spbm")==ygsp.get("spbm"):
                yg_old["gmsl"]=yg_old.get("gmsl")+ygsp.get("gmsl")
                break
            else:
                continue


    print(gwqdlist)









def main():
    splist=getspqd(qs)

    while True:
        gw(splist, qs)
        choice=input("是否继续购买（y/n）")
        if choice.lower()!='y':
            print("感谢您的购物，期待您的下次光临！！！")
            sy(qs)
            break

if __name__ == '__main__':
    main()

