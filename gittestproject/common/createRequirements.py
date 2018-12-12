import os
import sys
# 生成项目指定的环境包文件
# 目前存在的问题就是python的执行文件路径不能自动获取


# 找到当前目录
xm_dir=os.path.abspath("..")  # /media/lipengchao/study/pycharmproject/studypc/common没问题
print(xm_dir)

# 在pycharm中查看使用的Python位置
python_dir="/usr/bin/python3.6";

# 执行系统命令进行导出，当然这些过程都是可以在命令行中完成的
commad_str="{python_dir} -m pip freeze >{xm_dir}/requirements.txt".format(python_dir=python_dir,xm_dir=xm_dir);
os.system(commad_str)

