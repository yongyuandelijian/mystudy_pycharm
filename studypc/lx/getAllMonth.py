# import urllib.request  # 用于请求页面获得页面的源代码 被requests替代
import re  # 可以利用正则进行页面对象的转化
import os  # 用来判断以及操作系统文件夹或者文件
# import lxml # bs4需要的用来解析xml，html文件解析器
from bs4 import BeautifulSoup  # 用来从网页抓取数据
import bs4
import requests #
import pymysql # 用于操作数据库
from common import csv_utils
from common import text_utils
from common import sqlconf_utils
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36 Avast/65.0.411.162'
}
root_url = "http://tjj.xys.gov.cn"

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
    add_url=''
    ljlist = {}
    for tag in root_res:
        lj = tag.find_all('a')
        for a in lj:
            regex=r"\d{4}年\d{1}-\d{1,2}月[\u4e00-\u9fa5]{0,4}各县(市区|区)主要经济指标"  # u代表字符编码utf-8 r代表非转义
            if re.search(regex,a.get_text().strip()):
                # 找出我们需要的，虽然取第一个应该就可以实现，但是我们使用判断年月的方式来操作
                # print("截取到的年月是",re.match('\d{4}年\d{1}-\d{1,2}',a.get_text()).group())
                ljlist[re.match('\d{4}年\d{1}-\d{1,2}', a.get_text()).group()] = a['href']
                # print(ljlist)
                # add_url=a['href']
                # print("链接是%s文字是%s" % (a['href'], a.get_text()))
                # break 简单的办法就是获取到第一个就直接退出，但是我们在这里做联系用匹配年月的方式来操作
    print("字典结果是：",ljlist)
    return ljlist

# compile regular expressions and find
# all stuff we need
def getAllContent(url):
    # 从第一页中拿到href并返回内容
    # 进入第二页开始处理数据
    # url = href + "/" + str(i)
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
        regexp = ""
        tag=ele.find_all('tr')
        for tr in tag:
            tdlist=[]
            for td in tr:
                # 分为两种情况，当取到tr时类型是navigableString输出tab空格,取到td的时候就是tag输出他的内容
                # if type(td)==bs4.element.NavigableString:
                #     # content += '\t'
                #     print("\t")
                # el
                if type(td) == bs4.element.Tag:
                    # content +=repr(td.get_text().strip())  # 直接传递这样一个字符串出去，放进记事本那还可以，放入规格的文件是有问题的
                    # print(td.get_text().strip())
                    # 将列表内的为‘’的值替换为》》》
                    if td.get_text().strip()=='':
                        tdlist.append("》》》")
                    else:
                        tdlist.append(td.get_text().strip())
                    # 我们将结果处理成一个列表
                # print("取到的元素是%s,类型是%s"%(td,type(td)))
            # print(tdlist)
            content.append(tdlist)
            # print("\n")
    # print(content)
    return content

def main():
    textpath="F:\zqnr.txt"
    csvPath='F:\csvtest.csv'
    csvHead="csv练习插入"
    # 循环处理每个链接
    content=[]
    try:
        for lb in getUrl(root_url).items():
            url=root_url+lb[1]
            print('现在要处理的是路径是>>>',url)
            content.append(getAllContent(url))  # 为了练习csv我们还是使用字符串
        # 转为字符串插入结果
        contentstr=""
        for yy in content:
            # print("1",yy)
            for yh in yy:
                # contentstr = " ".join(content)  # 当然也可以使用下面的方式再次进行循环取出，但是为了练习，我们还是使用不同的方式
                for yg in yh:
                    contentstr+=yg
            print("\n")
        text_utils.writeFile(textpath,contentstr)  # 写入记事本
        csv_utils.write_csvFile(csvPath,"csv练习",content)  # 写入csv格式文本，他也可以直接写入上面的数组,而且数组貌似还格式相对合理一些
        print("多个月份的页面拼接最终结果",contentstr)

        mysql=sqlconf_utils.get_sqlconfig(r"C:\Users\Administrator\PycharmProjects\studypc\config\sqlConfig.ini") # r代表非转义的字符处理
        print("数据库配置文件的信息是：",mysql)
    except Exception as e:
        print("failed",e)


if __name__ == '__main__':
    main()


