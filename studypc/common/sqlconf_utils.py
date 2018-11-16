# 用于读取到数据库配置文件的相关配置
import configparser

def get_sqlconfig(filename):
    cf=configparser.ConfigParser() # 获取一个读取对象
    cf.read(filenames=filename,encoding='utf8') #读取配置文件
    # 读取对应的文件参数
    host=cf.get('mysql','host')
    port=cf.get('mysql','port')
    schema=cf.get('mysql','schema')
    user=cf.get('mysql','user')
    password=cf.get('mysql','password')
    charset=cf.get('mysql','charset')
    return host,port,schema,user,password,charset  # 返回需要的参数

# path="C:\Users\Administrator\PycharmProjects\studypc\config\sqlConfig.ini"
mysql=get_sqlconfig(r"C:\Users\Administrator\PycharmProjects\studypc\config\sqlConfig.ini")  # 传入上面的变量就报错了，搞不懂
print(mysql) # 返货的是一个元组

