# 根据输入的时间获取可见度和温度
class Tql(object):
    # 构造要求传入参数
    def __init__(self,input_time):
        self.input_time=input_time

    # 可见度  假设9点到18点期间可见度是9 温度是22  其他时间可见度是2 温度是9
    def getkjd(self):
        kjd=0
        if 18>=self.input_time>=9:
            kjd=9
        else:
            kjd=2
        return kjd

    # 温度
    def getwd(self):
        wd=0
        if 18>=self.input_time>=9:
            wd=22
        else:
            wd=9
        return wd