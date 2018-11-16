#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '$Package_name'
__author__ = '$USER'
__mtime__ = '$DATE'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import sys
import os
class haowan():
    def by(name):
        print("神兽保佑{name}，永无bug".format(name=name))


    if __name__ == '__main__':
        # print(sys.argv)  # 获取当前执行脚本所在的路径
        # print(__file__)  # 获取当前执行脚本所在的路径
        # 列表中依次是：0 当前执行文件所在的目录  1 当前项目的路径    3 当前使用Python可执行文件的路径  5 当前扩展软件包的路径
        zlj=sys.path;
        for lj in zlj:
            print("1111111\t",lj)
        # print("22222",os.path)  # 没啥用