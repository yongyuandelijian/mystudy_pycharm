# 功能描述，自动获取excel的表格获取内容
# aaa 20181106

import os                    # 用来操作系统命令
import sys                   # 用来操作程序退出
import time                  # 获取系统时间
import calendar              # 获取当前月天数
import random                # 生成随机时间
import xlrd                  # 读取excel
import xlwt                  # 写入excel
import requests              # 用来访问节假日接口
import json                  # 用于读取节假日接口返回的json
from xpinyin import Pinyin   # 汉字转为拼音

'''
判断当前日期是否是节假日

1、接口地址：http://api.goseek.cn/Tools/holiday?date=数字日期 
2、返回数据：工作日对应结果为 0, 休息日对应结果为 1, 节假日对应的结果为 2 
3、节假日数据说明：本接口包含2017年起的中国法定节假日数据，数据来源国务院发布的公告，每年更新1次，确保数据最新 
---------------------
作者：行内小白
来源：CSDN
原文：https://blog.csdn.net/qq1012566550/article/details/81660169
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
# 节假日接口
JAR_URL = "http://api.goseek.cn/Tools/holiday?date="
headers = {
    "cache-control": "no-cache",
    "postman-token": "72a56deb-825e-3ac3-dd61-4f77c4cbb4d8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",

}

def read_excel(filepath):
    """读取excel中的内容"""
    excel_obj = xlrd.open_workbook(filename=filepath)  # 获取excel对象

    sheet_name_list = excel_obj.sheet_names()  # 获取excel所有sheet的名称
    print(sheet_name_list)

    # 汉字转为拼音，方便创建表存储数据
    p = Pinyin();
    sheet_name_pinyinlist = []
    for sheet_name in sheet_name_list:
        pinyin_name = p.get_pinyin(sheet_name, splitter="").strip()
        # print("现在处理的是%s处理后是%s" %(sheet_name,pinyin_name))
        sheet_name_pinyinlist.append(pinyin_name)

    print("原始sheet名称是：{sheet_name_list},\n转为拼音后是：{sheet_name_pinyinlist}"
          .format(sheet_name_list=sheet_name_list, sheet_name_pinyinlist=sheet_name_pinyinlist));

    # sheet_obj=excel_obj.sheet_by_name(sheet_name[1]) # 根据sheet名称获取数据
    sheet_obj = excel_obj.sheet_by_index(0)  # 获取第1个工作表
    excel_content="";

    for row in sheet_obj.get_rows():
        print("-------------------------------------------------------")
        for cell in row:
            # print(type(cell))
            # print(cell.value)
            # print(cell.value)
            excel_content+=str(cell.value)

    return excel_content

# print(type(sheet_obj.get_rows()))
# row_data=sheet_obj.row_values(1)
#
# col_data=sheet_obj.col_values(1)
#
# print(type(row_data),type(col_data))
# # 获取工作表中数据
# print(type(sheet_obj))



# 写入excel代码,生成考勤记录

def set_style(name,height,bold=False):
    """设置生成excel的样式"""
    # 为样式创建字体并设置字体的一些样式
    font=xlwt.Font()
    font.name=name
    font.bold=bold
    font.color_index=0  # 具体色号也不记得,这个黑色是0
    font.height=height

    style = xlwt.XFStyle()  # 初始化样式
    style.font=font
    return style

def write_excel(path,my_year,my_month):
    """具体写入excel过程"""
    # 如果存在进行删除
    if os.path.exists(path):
        rm_command="rm {path}".format(path=path)
        os.system(rm_command)
    elif not os.path.exists(os.path.dirname(path)):
        sfcj=input("路径不存在,根据用户决定是否自动创建,如果不创建退出程序,如果创建继续执行(y/n)")
        if sfcj=='y':
            createdir_command="mkdir -p {path}".format(path=os.path.dirname(path))
            os.system(createdir_command)
        else:
            sys.exit(1)
    workbook=xlwt.Workbook(encoding='utf-8')  # 创建工作薄
    sheet_name="咸阳运维-{my_year}年{my_month}月".format(my_year=my_year,my_month=my_month)
    worksheet=workbook.add_sheet(sheetname=sheet_name)
    row_title = [u'姓名', u'日期', '签到时间', '签退时间']
    # 生成一个月的每一天
    maxday=calendar.monthrange(my_year,my_month)[1]  # 这个函数返回两个参数,一个是最后一天是周几,第二个是最大天数
    for i in range(len(row_title)):   # 循环次数是列的数量,也就是行的单元格个数,每次循环是一行的数据
        # print("列数是",i)
        # 参数分别是 行号,列号,要写入的内容,样式
        worksheet.write(0,i,row_title[i],set_style('simsun',222,True))   # 里面要做的操作是当前列的每个单元格的内容,参数分别是字体样式,字体大小,是否黑体
        for j in range(maxday):
            rownum=j+1
            # print("行数是", rownum)
            my_month="0"+str(my_month)
            my_day="0"+str(rownum)
            my_date=str(my_year)+"-"+my_month[-2:]+"-"+my_day[-2:]
            start_time = "0" + str(random.randrange(0, 28))
            start_time = "8:" + start_time[-2:]
            end_time = str(random.randrange(10, 58))
            end_time = "18:" + end_time
            # 根据节假日来判断开始和结束时间
            url=JAR_URL+str(time.localtime()[0])+my_month[-2:]+my_day[-2:]
            response_str=requests.get(url,headers)
            response_str.encoding="utf-8"
            json_str=json.loads(response_str.text)
            if json_str.get("data")==1:
                start_time="周末"
                end_time = "周末"
            elif json_str.get("data")==2:
                start_time="节假日"
                end_time = "节假日"
            print("现在要写入的日期是{my_date},签到时间是{start_time},签退时间是{end_time},当天状态是{json_str}".format(my_date=my_date,start_time=start_time,end_time=end_time,json_str=json_str.get("data")))

            row_content = [u'李鹏超', my_date, start_time, end_time]
            worksheet.write(rownum,i,row_content[i], set_style('simsun', 222, False))

    workbook.save(path)  # 保存文件



if __name__ == '__main__':
    now_time = time.localtime()
    year=now_time.tm_year
    month=now_time.tm_mon



    path='/media/lipengchao/study/zhengtong/考勤相关/考勤软件/咸阳运维-{year}年{month}月考勤软件汇总表.xls'.format(year=year,month=month)   # 这个path要包含工作表名称
    dirname=os.path.dirname(path)
    bookname=os.path.basename(path)
    sheetname=os.path.basename(path).split("考勤")[0]

    """
    读取的方法
    str=read_excel(filepath=path)
    print(str)
    print(str.count("李鹏超"))
    """


    try:
        # 只放置可能出错的语句,其他的放到else继续执行
        write_excel(path, year, month)
    except:
        
        # 可以看出except用于捕获运行时异常,并不捕获类似语法错误的编译错误,except的意义主要在于
        # 1 对用户进行友好的提示,也可以隐藏内部的实现
        # 2 帮助程序跳过错误的部分继续执行其他部分而不是提示错误直接程序崩溃
        
        print("出错啦,请检查excel写入的方法")
    else:
        # try代码块执行没有错误,else中的继续执行!!!
        print("位于路径 《{dirname}》下的excel表格 《{bookname}》 中sheet页 《{sheetname}》 生成成功".format(dirname=dirname,
                                                                                         bookname=bookname,
                                                                                         sheetname=sheetname))
    finally:
        print("无论什么结果都必须执行finally")

    print("实际上不需要else也可以继续执行,只是说结构不清晰,还是推荐使用try--except--else结构")



    # sj=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()).split(" ")[0].split("-")
    # sj=str(time.localtime()[0])+"-"+str(time.localtime()[1])
    # print(type(sj),sj)
    # aaa=str(random.randrange(0,28))
    # print(aaa)
    # print("8:"+aaa)
    # start_time = "0" + str(random.randrange(0, 28))
    # start_time = "8:" + start_time[-2:]
    # print(start_time)


