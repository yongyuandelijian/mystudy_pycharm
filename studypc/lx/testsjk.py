import pymysql
connect=pymysql.connect(host="localhost",user="lpc",passwd="lipengchao",port=3306,db="lpctest")
cursor=connect.cursor()
insertSQL="insert into test_20180606 (jg,yf,je,tbbh) value(%s,%s,%d,%d)"
try:
    cursor.execute(insertSQL,'22','33',44,55)
    connect.commit()
    print("插入数据库成功！！！")
except Exception as e:
    print("小丁很生气，数据插入数据库错误！",e)
finally:
    connect.close()