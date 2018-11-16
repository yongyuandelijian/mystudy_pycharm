# 读取配置文件
# 对这种形式不是很习惯，所以我们使用自己编写的sqlconf  20180613
from common.name_tuples_zf import mysql  # 导入其他类的变量

import configparser

class ConfigReader:
    # path 为配置文件的完整路径，由调用者传入
    def __int__(self,path):
        if path is None or len(path)<1: #简单的判断下路径的合法性
            raise ValueError('路径无效!!!')
        else:
            self.conf=configparser.ConfigParser()
            self.conf.read(path)

    # 获取所有配置
    def get_mysql_info(self):
        host=self.conf.get('mysql','host')   # 当变量定义为self的时候就会供其他方法来使用
        user=self.conf.get('mysql','user')
        password=self.conf.get('mysql','password')
        port=self.conf.get('mysql','port')
        schema=self.conf.get('mysql','schema')
        charset=self.conf.get('mysql','charset')
        print(host)
