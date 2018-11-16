# 关于正则表达式的操作和应用
import re
print(re.match('\d{3}\d','12323',flags=0))  # 返回值里有三个对象，第一个是march的对象，第二个是成功匹配的下标，第三个是匹配到的字符
print(re.match('\d{3}','12323',flags=0).span())
print(re.match('\d{3}','12323',flags=0).start())  # 返回匹配到的开始位置元素，这个里具体的方法，需要自己在使用中多加操作
print(re.match('\d{3}','12323',flags=0).group())  # 返回匹配到的字符
print(re.match('\d{3}\d','12323',flags=0).groups())  # 返回匹配到的字符
# match和search的区别
print("match进行的精确匹配",re.match('3','123456',flags=0))  # match只有匹配的字符是从第一个字符开始的才能匹配到，如果在后面就无法匹配
print("search进行的精确匹配",re.search('3','1234556',flags=0)) # search只要字符串内可以匹配到reg，那么就算匹配到了

# 贪婪模式和非贪婪模式
print(re.match('^(\d+)(0*)$','125000').groups())  # 默认是贪婪模式，在使用开头结尾的时候，需要使用小括号来辅助，贪婪模式就是前面的开头已经将所有字符匹配完成，后面的结果表达式什么都没有匹配到
print(re.match('^(\d+?)(0*)$','125000').groups()) # 给前面的表达式增加？来切换模式，这样前面的匹配完自己的部分,后面也会将自己的部分匹配到

# 当一个re表达式需要多次使用的时候，我们可以进行预编译，新建一个匹配座机的格式re_startEnd=re.
re_zj=re.compile('^(\d{3})[-\s+](\d{8})$') # 横杠或者空格都可以
print("座机匹配",re_zj.match("023 23344333").groups())  # 这里有个隐藏的错误，就是当没有匹配到的时候无法进行groups的方法，在使用中可能会导致程序报错

# 利用re进行替换
thmz=re.compile('aaa')
restr='aaa20180203aaa'
print(thmz.sub('lpc',restr,1))  # 如果没有匹配到就返回字符串本身
# 当然上面的例子也可以转为
print(re.sub('aaa','lpc',restr))
