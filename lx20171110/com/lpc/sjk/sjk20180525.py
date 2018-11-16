import pymysql

# get connection
conn=pymysql.connect(host="localhost",port=3306 ,user="root",db="test",passwd="123456")

# create cursor
cur=conn.cursor()

# execute sql
cur.execute("select version()")

# fetchone get a result
data=cur.fetchone()

# print
print("result is",data)

# close conect
conn.close()
