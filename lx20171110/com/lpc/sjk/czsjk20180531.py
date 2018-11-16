import  pymysql
import datetime

# create tables
def createTable(tablename):
    # get connect
    connect=pymysql.connect(host="localhost",user="root",passwd="123456",db="test",port=3306)

    # get cursor
    cursor=connect.cursor()

    # execute sql
    cursor.execute("DROP TABLE IF EXISTS %s"%tablename)  # 开始使用了，追加的方式，提示错误，更换成%形式传入参数，正常

    # 使用预处理语句创建表
    tablesql="""
    create table %s
    (
    id INT(11),
    col1 VARCHAR(50),
    col2 VARCHAR(300),
    col3 VARCHAR(500),
    bak1 VARCHAR(20)
    )
    """%tablename   # 要执行的sql字符串
    # execute sql
    try:
        cursor.execute(tablesql)
        print("create table success")
    except Exception as e:
        print("create table failed",e)
    finally:
        connect.close()

# insert
def insertDate(data):
    connect=pymysql.connect(host="localhost",user="root",passwd="123456",port=3306,db="test")
    cursor=connect.cursor()
    insertSQL="INSERT INTO pylx_20180531 (id,col1,col2,col3) VALUES(%d,'%s','%s','%s')"%(data[0],data[1],data[2],data[3])
    try:
        cursor.execute(insertSQL)
        connect.commit()
        print("insert success")
    except Exception as e:
        connect.rollback()
        print("insert failed:",e)
    finally:
        connect.close()
# query
def queryData():
    connect=pymysql.connect(host="localhost",user="root",passwd="123456",port=3306,db="test")
    cursor=connect.cursor()
    querySQL="SELECT * FROM pylx_20180531"
    try:
        cursor.execute(querySQL)
        result = cursor.fetchall()  # 返回一个全部行的结果集
    except Exception as e:
        print("发现了一个错误",e)
    finally:
        connect.close()
    return result

# update
def updateData(id):
    connect=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db="test")
    cursor=connect.cursor()
    updateSQl="UPDATE pylx_20180531 SET bak1='bakcol' WHERE id=%d"%id
    try:
        cursor.execute(updateSQl)
        connect.commit()
        print("update success")
    except Exception as e:
        connect.rollback()
        print("update failed",e)
    finally:
        connect.close()
# delete
def deleteData(id):
    connect=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db="test")
    cursor=connect.cursor()
    deleteSQL = "DELETE FROM pylx_20180531 WHERE id=%d"%id
    try:
        cursor.execute(deleteSQL)
        connect.commit()
        print("delete success,影响的行数是",cursor.rowcount)
    except Exception as e:
        connect.rollback()
        print("delete failed",e)
    finally:
        connect.close()

def main():
    # createTable('pylx_20180531') 创建表

    # 插入数据
    # data=(1,'xiaoding',"23",datetime.datetime.now().strftime("%Y-%m-%d"))
    # if type(data).__name__!="tuple" or len(data)<4:
    #     print("对不起，传入的数据有误，请重新传入")
    # else:
    #     insertDate(data)

    # # 查询数据
    # result=queryData()
    # for row in result:
    #     for i in row:
    #         print("当前取出的元素是》》》",i)

    # 修改
    # updateData(1)

    # 删除
    deleteData(1)



if __name__ == '__main__':
    main()