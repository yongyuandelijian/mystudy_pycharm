# import urllib.request  # 用于请求页面获得页面的源代码 被requests替代
import re  # 可以利用正则进行页面对象的转化
import os  # 用来判断以及操作系统文件夹或者文件
# import lxml # bs4需要的用来解析xml，html文件解析器
from bs4 import BeautifulSoup  # 用来从网页抓取数据
import bs4
import requests
import pymysql # 用来操作数据库
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36 Avast/65.0.411.162'
}
root_url = "http://tjj.xys.gov.cn"
ny=''  # 用来接收本次数据年月的全局变量
# open url and read
# def readurl(url):
#     page=urllib.request.urlopen(url)  # 获得是一个页面对象
#     html=page.read()
#     page.close()
#     return html   被如下的两句话就可以替代
def getUrl(root_url):
    response=requests.get(root_url,headers)
    response.encoding='utf-8'
    soup=BeautifulSoup(response.text,'lxml')
    root_res=soup.find_all(class_='main')
    add_url=''  # 如果只返回一个内容，插入数据的时候不知到是目前的数据所属年月
    ljlist = {}
    for tag in root_res:
        lj = tag.find_all('a')
        for a in lj:
            regex=r"\d{4}年\d{1}-\d{1,2}月[\u4e00-\u9fa5]{0,4}各县(市区|区)主要经济指标"  # u代表字符编码utf-8 r代表非转义
            if re.search(regex,a.get_text().strip()):
                # 找出我们需要的，虽然取第一个应该就可以实现，但是我们使用判断年月的方式来操作
                # print("截取到的年月是",re.match('\d{4}年\d{1}-\d{1,2}',a.get_text()).group())
                ljlist[re.match('\d{4}年\d{1}-\d{1,2}月', a.get_text()).group()] = a['href']
                # print(ljlist)
                # add_url=a['href']
                # print("链接是%s文字是%s" % (a['href'], a.get_text()))
                # break 简单的办法就是获取到第一个就直接退出，但是我们在这里做联系用匹配年月的方式来操作
    # print("字典结果是：",ljlist.keys())
    # 对字典进行循环比对
    # print(ljlist[max(ljlist.keys())])
    ny=max(ljlist.keys())
    add_url=ljlist.get(ny)
    resurl=(ny,add_url)
    # print(resurl)
    return resurl

# compile regular expressions and find
# all stuff we need
def getAllContent(url):
    # 从第一页中拿到href并返回内容
    # 进入第二页开始处理数据
    url = 'http://tjj.xys.gov.cn/sjzx/xysj/515620.htm'
    page = requests.get(url, headers=headers)
    page.encoding='utf-8' # 不指定会导致中文乱码，最好就是指定，默认是iso-8859-1
    soup = BeautifulSoup(page.text,'lxml')  # 将html转为了soup对象,是全部的内容
    # print("soup没有属性的对象是》》》%s,有属性的对象是%s"%(soup.h3.string,soup.div.get('id')))
    # print("获取元素的所有子节点内容",soup.body.contents[0])

    # for v in soup.body.children:
    #     print("获取到下一级子元素",v)

    # for des in soup.body.descendants:
    #     print("所有子孙节点都获取到",des.string)

    # for a in soup.body.stripped_strings:  # 这个方法还是最实用
    #     print("所有子孙节点都获取到并且去除空格", a)

    # 找到我们需要的那个节点
    res=soup.find_all(class_="ny_nr")  # 获取到了这个制定节点下的所有内容
    content=[]  # 用来存储需要的内容
    for ele in res:
        # regexp = ""
        tag=ele.find_all('tr')
        for tr in tag:
            for td in tr:
                # 分为两种情况，当取到tr时类型是navigableString输出tab空格,取到td的时候就是tag输出他的内容
                # if type(td)==bs4.element.NavigableString:
                #     content += '\t'
                # elif type(td) == bs4.element.Tag:  数据持久化就不需要这个空格的位置了
                if type(td) == bs4.element.Tag:
                    # content +=repr(td.get_text().strip()) 这样存储不够科学，如果全部需要则可以放开
                    # print(td.get_text().strip())
                    # 如果是生产总值，那具体的数据就在当前单元格的父级标签（第一行）的14个兄弟标签（第二行的前三个单元格）
                    if '生产总值' in td.get_text().strip():
                        tr1=td.parent
                        # print(tr1)
                        for i in range(14):
                            tr1 = tr1.next_sibling.next_sibling
                            # 面临相同的情况，每隔一行会有一行空值
                            if type(tr1) == bs4.element.Tag:
                                count = 0
                                contentlist = []
                                for td1 in tr1:
                                    if type(td1) == bs4.element.Tag:
                                        if count < 3:
                                            contentlist.append(td1.get_text().strip())
                                            # print("调试需要的每行前三列数据>>>%s<<<" % td1.get_text().strip())
                                            count += 1
                                contentlist.append(getUrl(root_url)[0])  # 每一行增加上年月数据
                                # print("每一行的内容列表",contentlist)
                            # print("第%d次获取行\n元素是%s,元素类型是%s"%(i,tr1.next_sibling,type(tr1.next_sibling)))
                                content.append(contentlist)
                # print("取到的元素是%s,类型是%s"%(td,type(td)))
    # 清除掉第一行没用的信息
    content.pop(0)
    print("获取到的全部内容是%s共%d个项"%(content,len(content)))
    return content

def sjk(content):
    connect=pymysql.connect(host="localhost",user="lpc",passwd="lipengchao",port=3306,db="lpctest",charset="utf8")
    # connect.encoding='utf8'  # 这个方式效果只能转换一半，不如上面的方式好
    cursor=connect.cursor()
    # print(content)
    insertSQL=""
    try:
        for lb in content:
            # print("当前插入的数据是>>>>>>>：",(lb[0], lb[3], lb[1], lb[2]))
            # 注意这个varchar类型的需要增加引号的问题，不然就会把varchar当做数字来看就会报错
            insertSQL="insert into test_20180606 (jg,yf,je,tbbh) values ('%s','%s',%d,%d)"%(lb[0], lb[3], float(lb[1]), float(lb[2]))
            print("要执行的语句是》》》》》",insertSQL)
            cursor.execute(insertSQL)
        connect.commit()
        print("插入数据库成功！！！")
    except Exception as e:
        connect.rollback()
        print("小丁很生气，数据插入数据库错误！",e)
    finally:
        connect.close()

def writeFile(path,content):
    try:
        file = open(file=path, mode='w',encoding='utf-8')
        file.write(content)
        print("write sucess", file.name)
    except Exception as e:
        print("write failed", e)
    finally:
        file.close()


def main():
    path="F:\zqnr.txt"
    try:
        url=root_url+getUrl(root_url)[1]
        print("正在处理的页面地址是",url)
        content = getAllContent(url)
        # writeFile(path,content) 不在使用写入文件，进行数据库的插入
        sjk(content)
        print("main执行完毕》》》》")
    except Exception as e:
        print("main failed",e)


if __name__ == '__main__':
    main()


