'''
获取配置文件中的内容
Date:20181026
Author:AAA
'''

import configparser

pzwj="/media/lipengchao/study/pycharmproject/studyProject/conf/basicConfig"

cf = configparser.ConfigParser();
cf.read(filenames=pzwj, encoding="utf-8")

def get_logall(basicpath):
    logallpath=basicpath+"/log/"+cf.get("log","log_all")
    return logallpath;

def get_logerror(basicpath):
    logerrorpath=basicpath+"/log/"+cf.get("log","log_all")
    return logerrorpath;

def get_gwqdpath(basicpath):
    gwqdpath = basicpath + "/db/"+cf.get("db","gwqdpath")
    return gwqdpath;

def get_yhxxpath(basicpath):
    yhxxpath = basicpath + "/db/"+cf.get("db","yhxxpath")
    return yhxxpath;

def get_spxxpath(basicpath):
    spxxpath = basicpath + "/db/"+cf.get("db","spxxpath")
    return spxxpath;

def get_spflpath(basicpath):
    spflpath = basicpath + "/db/"+cf.get("db","spflpath")
    return spflpath;

def get_yhjbpath(basicpath):
    yhjbpath = basicpath + "/db/"+cf.get("db","yhjbpath")
    return yhjbpath;

def get_ztpath(basicpath):
    ztpath = basicpath + "/db/"+cf.get("db","ztpath")
    return ztpath;

# import os
# basicpath = os.path.abspath("../")
# basicpath=basicpath+"/log/"
# print(cf.items("log"))