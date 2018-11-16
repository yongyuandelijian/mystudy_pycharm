# 功能描述，自动获取excel的表格获取内容
# aaa 20181106

import xlrd  # 读取excel
# import xlwt  # 写入excel
from xpinyin import Pinyin # 汉字转为拼音

filepath = "/media/lipengchao/study/zhengtong/咸阳运维项目组考勤情况（201810）.xlsx"
excel_obj = xlrd.open_workbook(filename=filepath)  # 获取excel对象

sheet_name_list = excel_obj.sheet_names()  # 获取excel所有sheet的名称
print(sheet_name_list)

# 汉字转为拼音，方便创建表存储数据
p=Pinyin();
sheet_name_pinyinlist=[]
for sheet_name in sheet_name_list:
    pinyin_name=p.get_pinyin(sheet_name,splitter="").strip()
    # print("现在处理的是%s处理后是%s" %(sheet_name,pinyin_name))
    sheet_name_pinyinlist.append(pinyin_name)


print("原始sheet名称是：{sheet_name_list},\n转为拼音后是：{sheet_name_pinyinlist}"
      .format(sheet_name_list=sheet_name_list,sheet_name_pinyinlist=sheet_name_pinyinlist));

sheet10_obj=excel_obj.sheet_by_name(sheet_name[10]) # 根据sheet名称获取数据
sheet10_obj = excel_obj.sheet_by_index(9) # 获取第十个工作表

for row in sheet10_obj.get_rows():
    print("-------------------------------------------------------")
    for cell in row:
        print(cell)



# print(type(sheet10_obj.get_rows()))
# row_data=sheet10_obj.row_values(1)
#
# col_data=sheet10_obj.col_values(1)
#
# print(type(row_data),type(col_data))
# # 获取工作表中数据
# print(type(sheet10_obj))


