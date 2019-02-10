# 用来从51cto上按照关键字爬取工作情况

import csv
import re

import requests
from lxml import etree
from bson import ObjectId
from pymongo import MongoClient
client = MongoClient() #链接数据库
db = client.java2 #创建一个pythondb数据库


headers = {
    "cache-control": "no-cache",
    "postman-token": "72a56deb-825e-3ac3-dd61-4f77c4cbb4d8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",

}
key1 = input('请输入要搜索的职位：')
def get_url():
    urll = "https://search.51job.com/list/030800%252C040000%252C030200,000000,0000,00,9,99,java,2,1.html"
    response = requests.get(urll, headers=headers)
    html = etree.HTML(response.content.decode('gbk'))
    max_page =int("".join(re.findall('(\d+)',"".join(html.xpath("//span[@class='td']/text()"))))) #正则表达式只能匹配字符串，列表里面的匹配不了
    for i in range(1,max_page+1): #(1,10)是打印到9的所有要加1
        url = "https://search.51job.com/list/030800%252C040000%252C030200,000000,0000,00,9,99,{0},2,{1}.html"
        key = key1
        url = url.format(key,i)
        yield url


def pase_page():
    for i in get_url():
        url = i
        #print(url)
        response = requests.get(url,headers=headers)
        html = etree.HTML(response.content.decode('gbk'))  # 解码成gbk后输出，请求的是gbk，但是python默认的是
        #输出的是utf-8，所以把utf-8解码成gbk就可以输出了，这样请求和输出就一样了,decode 相当于输出
        #编码的输入和输出要一致。


        lists = html.xpath("//div[@id='resultList']//div[@class='el']")
        for list in lists:
            item = {}
            # newObjectId = ObjectId()
            # item['_id'] = newObjectId  # 保存到mongondb数据库必须填这两个
            item["职位"] = "".join(list.xpath("./p/span/a/text()")).replace('\r\n', '').replace(' ', '')
            item["公司名称"] = "".join(list.xpath("./span[@class='t2']/a/text()")).replace('\r\n', '').replace(' ', '')
            item["工作地点"] = "".join(list.xpath("./span[@class='t3']/text()")).replace('\r\n', '').replace(' ', '')
            item["薪资"] = "".join(list.xpath("./span[@class='t4']/text()")).replace('\r\n', '').replace(' ', '')
            item["发布时间"] = "".join(list.xpath("./span[@class='t5']/text()")).replace('\r\n', '').replace(' ', '')
            # posts = db.java2  # 创建表
            # posts.insert_one(item)  # 往表里插入数据
            # print('保存到mogondb数据库成功')
            yield item


def save_excel():
    header = ['职位', '公司名称', '工作地点', '薪资', '发布时间']
    with open('python_test.csv', 'w', newline='') as f:  # w是写入
        # 标头在这里传入，作为第一行数据
        writer = csv.DictWriter(f, header)
        writer.writeheader()
    for i in pase_page():
        item = i
        # print(item)
        # print(type(item))
        header = ['职位', '公司名称', '工作地点', '薪资', '发布时间']
        with open('python1.csv', 'a', newline='') as f:  # a是追加
            writer = csv.DictWriter(f, header)
            writer.writerow(item)
            print(item)


if __name__ == '__main__':

    #pase_page()
    save_excel()