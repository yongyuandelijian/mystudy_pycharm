# -*- coding:utf-8 -*-
import cv2
import numpy as np
import copy
from PIL import Image
import pytesseract
import math


''' 根据该像素周围点为黑色的像素数（包括本身）来判断是否把它归属于噪声，如果是噪声就将其变为白色'''
'''
    input:  img:二值化图
            number：周围像素数为黑色的小于number个，就算为噪声，并将其去掉，如number=6，
            就是一个像素周围9个点（包括本身）中小于6个的就将这个像素归为噪声
    output：返回去噪声的图像
    
    从结果上看到，实际上大于６的几乎正好找到了干扰线，数字都被过滤掉了，我们反向操作应该就可以过滤到数字
'''

def del_noise(img,number):
    height = img.shape[0]
    width = img.shape[1]
    # 对图像进行复制一份，如果是使用copy.copy方法那么就只是直接引用
    img_new = copy.deepcopy(img)
    print(img[0][1])
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            point = [[], [], []]
            count = 0
            # 当前像素点的左上，左，左下
            point[0].append(img[i - 1][j - 1])
            point[0].append(img[i - 1][j])
            point[0].append(img[i - 1][j + 1])
            # 下，当前，上
            point[1].append(img[i][j - 1])
            point[1].append(img[i][j])
            point[1].append(img[i][j + 1])
            # 右上，右，右下
            point[2].append(img[i + 1][j - 1])
            point[2].append(img[i + 1][j])
            point[2].append(img[i + 1][j + 1])
            for k in range(3):
                for z in range(3):
                    if point[k][z] == 0:
                        count += 1
            # 我们将符号换过来，大于等于阀值
            if count >= number:
                img_new[i, j] = 255
    return img_new


def del_noise2(im_cut):
    ''' variable：bins：灰度直方图bin的数目
                  num_gray:像素间隔
        method：1.找到灰度直方图中像素第二多所对应的像素，即second_max,因为图像空白处比较多所以第一多的应该是空白，第二多的才是我们想要的内容。
                2.计算mode
                3.除了在mode+-一定范围内的，全部变为空白。
    '''
    bins = 16
    num_gray = math.ceil(256 / bins)
    hist = cv2.calcHist([im_cut], [0], None, [bins], [0, 256])
    lists = []
    for i in range(len(hist)):
        # print hist[i][0]
        lists.append(hist[i][0])
    second_max = sorted(lists)[-2]
    bins_second_max = lists.index(second_max)

    mode = (bins_second_max + 0.5) * num_gray

    for i in range(len(im_cut)):
        for j in range(len(im_cut[0])):
            if im_cut[i][j] < mode - 15 or im_cut[i][j] > mode + 15:
                # print im_cut[i][j]
                im_cut[i][j] = 255
    return im_cut


def del_noise1(img,number):
    height = img.shape[0]
    width = img.shape[1]
    # 对图像进行复制一份，如果是使用copy.copy方法那么就只是直接引用
    img_new = copy.deepcopy(img)
    print(img[0][1])
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            point = [[], [], []]
            count = 0
            # 当前像素点的左上，左，左下
            point[0].append(img[i - 1][j - 1])
            point[0].append(img[i - 1][j])
            point[0].append(img[i - 1][j + 1])
            # 下，当前，上
            point[1].append(img[i][j - 1])
            point[1].append(img[i][j])
            point[1].append(img[i][j + 1])
            # 右上，右，右下
            point[2].append(img[i + 1][j - 1])
            point[2].append(img[i + 1][j])
            point[2].append(img[i + 1][j + 1])
            for k in range(3):
                for z in range(3):
                    if point[k][z] == 0:
                        count += 1
            # 我们将符号换过来，大于等于阀值
            if count <= number:
                img_new[i, j] = 255
    return img_new


if __name__=='__main__':
    img_dir = '/media/lipengchao/study/pycharmproject/studypc/common/img/yzm20180906.png'
    kernel = np.ones((5, 5), np.uint8)
    image = cv2.imread(img_dir)
    # # 灰度化效果比较差，还不如IMAGE的处理效果
    # # print(image.shape)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #
    # # 二值化
    result = cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
    # 去噪声
    img=del_noise2(result)




    # img = del_noise(result, 7)
    # img = del_noise1(img, 2)
    # # img = del_noise(img, 3)
    # # 加滤波去噪
    # im_temp = cv2.bilateralFilter(src=img, d=15, sigmaColor=130, sigmaSpace=150)
    # im_temp = im_temp[1:-1,1:-1]
    # im_temp = cv2.copyMakeBorder(im_temp, 83, 83, 13, 13, cv2.BORDER_CONSTANT, value=[255])
    # cv2.imwrite('/media/lipengchao/study/pycharmproject/studypc/common/img/yzmclh20180907.png', im_temp)

    image=Image.open("/media/lipengchao/study/pycharmproject/studypc/common/img/yzmclh20180907.png")
    image.show()
    image = Image.open("/media/lipengchao/study/pycharmproject/studypc/common/img/yzm20180906.png")
    image.show()
    code=pytesseract.image_to_string(image)
    print("图片预处理完成！",code)