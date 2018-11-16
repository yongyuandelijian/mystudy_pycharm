# 用来判断传入的路径是否正确，如果在系统中不存在那么就提示输入
import os
class JudgementPath(object):
    def __init__(self,path):
        fullpath=os.path.abspath(path)
        if not os.path.exists(fullpath):
            inputpath=input("请输入正确的路径！！！")
        return inputpath