# 定义必须的名称元组
import collections

# 用于mysql的服务信息
mysql=collections.namedtuple('MySQL',['host','user','password','port','schema','charset'])

print(type(mysql))