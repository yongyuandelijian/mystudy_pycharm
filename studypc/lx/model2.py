# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MeZiG.py
   Description :
   Author :       bystart
   date：          2018/5/7
-------------------------------------------------
   Change Activity:
                   2018/5/7:
-------------------------------------------------
"""
__author__ = 'bystart'
import os
import re
import time
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36 Avast/65.0.411.162'
}
root_url = "http://www.mzitu.com/all/"

# 本地文件地址
current_dir = os.getcwd()
parent_dir = os.path.abspath(current_dir + os.path.sep + ".")
html_dir = "res" + os.path.sep + "html" + os.path.sep + "start.html"


def deal_path_name(name):
    """去除路径中的特殊字符"""
    pattern = "[?|<|>|\"|\*|\||/|\\\\|:]"
    return re.sub(pattern, "", name)


def create_dir(dirname):
    '''
        创建文件夹
    '''
    print(dirname)
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def update_header(referer):
    headers["Referer"] = "{}".format(referer)


def main():
    # 访问主页
    all_page = requests.get(root_url, headers=headers)
    soup = BeautifulSoup(all_page.text, "lxml")
    # 主页获取每一项的地址，获取合集信息，创建合集文件夹
    # class="archives"是一年
    cls_archives = soup.find_all(class_="archives")
    for archive in cls_archives:
        # 按年份创建文件夹
        year_tag = archive.find_previous_sibling(class_="year")
        year = year_tag.get_text()
        year_path = os.path.join(os.getcwd(), "妹子图" + os.path.sep + year)
        create_dir(year_path)
        # 按年份抓取文件,archive下所有a标签的href
        year_item_count = 0
        all_a = archive.find_all("a")
        for a in all_a:
            # 获取单个合集地址和标题
            year_item_count += 1
            title = a.get_text()
            href = a["href"]
            if str(year).find('2018年') != -1:
                if year_item_count < 361:
                    print(year_item_count, title)
                    continue

            # 创建集合文件夹
            series_dir = os.path.join(year_path, deal_path_name(title))
            create_dir(series_dir)
            # 访问集合 -- 获取合集总数
            series = requests.get(href, headers=headers)
            series_soup = BeautifulSoup(series.text, "lxml")
            count = series_soup.find("div", class_="pagenavi").find_all("span")[-2].get_text()
            for i in range(1, int(count) + 1):
                # 根据合集照片总数，拼接地址进行访问
                url = href + "/" + str(i)
                page = requests.get(url, headers=headers)
                page_soup = BeautifulSoup(page.text, "lxml")
                # 访问具体页面，获取照片src地址
                img_url = page_soup.find(class_="main-image").find("img")["src"]
                # 简单的反--反爬虫处理
                update_header(img_url)
                # 访问照片src,存储到合集文件夹中
                img = requests.get(img_url, headers=headers)
                img_path = os.path.join(series_dir, str(i) + ".jpg")
                # print(img_path)
                print(img.url)
                with open(img_path, "wb+") as f:
                    f.write(img.content)
                # print(img_url)

    # 访问每一项的地址，获取合集照片总数
    # 根据合集照片总数，拼接地址进行访问
    # 访问具体页面，获取照片src地址
    # 访问照片src,存储到合集文件夹中


if __name__ == '__main__':
    main()