
# 使用json，通用  ctr+d直接复制一行
import json
xiaoding=dict(name='xiaoding',age=18,lp='fanbingbing')
txtpath="F:\jsonxlh.txt"
'''
# 处理字符串，这样来处理
json_str=json.dumps(xiaoding)
print(json_str)

aaa=json.loads(json_str)
print(aaa['name'])
'''
# 处理文件直接使用dump或者load
filew=open(txtpath,'w')  # json存储的时候不是使用二进制进行存储的和pickle不一样，只是以一样的形式进行存储
print(filew)
json.dump(xiaoding,filew)
filew.close()

filer=open(txtpath,'r')  # 如果为空会报错
json_read=json.load(filer)
print(json_read)
filer.close()

# repr 返回一个任何对象的字符串表达形式
print(repr(filew))

# 练习，写一首诗到文件
filepath='F:\小丁.txt'
# with open(filepath,'w') as file:
#     file.write('  静夜思\n窗前明月光\n疑是地上霜\n举头望明月\n低头思故乡')  # 这里居然空格是管用的，使用\t空格过大
# 统计‘月’出现的频率，通过迭代进行统计
file1=open(filepath,'r')
i=0
str=''
for char in file1:
    i+=1
    rep_str=char.replace('地上霜','天上云')
    print("第%d次循环的内容是\t%s\t替换后的字符串是\t%s"%(i,char,rep_str))
    str=str+char
print(">>>",str.count('月'))
file1.close()

