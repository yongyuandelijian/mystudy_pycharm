# coding:utf-8
# 压缩的方法
# 文件压缩工具
import tarfile  # 多用于linux
 # 多用于windows
# str通过encode()方法可以编码为指定的bytes
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
from zipfile import ZipFile
import os
import zipfile
# 读取压缩文件
class compress(object):
    def getzip_file(zip_filepath):  # 传入读取目录
        myzip = ZipFile(zip_filepath, "r")
        print(myzip.namelist())  # 获取到一个列表，压缩包根目录，以及其他文件
        for file_name in myzip.namelist():
            print("当前处理的文件数是", file_name)
            for data in myzip.open(file_name, "r"):
                print("文件名是%s内容是%s" % (file_name, data))  # 经过测试，读取是按照每一行的内容进行读取
                print(">>>", data.decode('utf-8'))
        myzip.close()

    # path="F:\\test"  # 或者使用转义，或者使用r限制转换
    # getzip_file(r"F:\test.zip")

    # 压缩目录


    # 如果给定的路径下有文件就直接添加倒要压缩的文件列表，如果是目录就打开循环处理每一层路径下的文件和文件夹
    def zip_dir(dirname, zipfilename):  # 压缩目录名称和要压缩的目录
        filelist = []  # 用来存储所有要压缩的文件
        if os.path.isfile(dirname):  # 判断压缩目录是否是文件，是就添加到filelist中
            filelist.append(dirname)
        else:
            for root, dirs, files in os.walk(dirname):  # 三个获取到的参数分别是root根目录 dirs是根目录下的子目录 files是存放在根目录下的文件
                print("根目录是%s,子目录是%s,文件是%s" % (root, dirs, files))
                for name in files:  # 将每次出现的文件列表添加到要压缩的文件中，并存储每次的文件路径
                    filelist.append(os.path.join(root, name))
        # 文件获取完成后，执行压缩步骤,当然我们也可以使用自动获取名称
        if "zip" not in zipfilename:
            # zipfilename=dirname[0:dirname.rindex("\\")]+".zip"
            zipfilename = dirname + ".zip"  # 如果没有路径就自动判断
            print("获取到的新名字是", zipfilename)
        zf = zipfile.ZipFile(zipfilename, "w", zipfile.ZIP_DEFLATED, allowZip64=True)  # 创建一个压缩对象
        print("获得的文件列表是：", filelist)
        for tar in filelist:
            arcname = tar[len(dirname):]  # 获取每一层目录以及目录下的文件路径
            print("获得的文件名称是", arcname)
            zf.write(tar, arcname)  # 将内容写入arcname文件中
        zf.close()

    # dirname="F:\\my"   # 当然也可以采用引用位置使用r前缀
    # zipfilename="F:\\my.zip"  # 这个位置不是例子示范的那样直接使用，必须要带路径才可以
    # zip_dir(dirname,zipfilename)

    # import os
    # import zipfile
    # 导入处理图片的包
    # import matplotlib.pyplot  as showimg # 用于显示图片  默认的这个只能读取png格式的，要初始化其他包才能读取其他格式
    # import matplotlib.image as readimg # 用于读取图片 matplotlib默认范围太小，只能读取png，我们先不学习
    from PIL import Image  # 处理图片
    # import matplotlib.pyplot as plt

    # 解压文件
    def unzip_dir(zipfilepath):
        # 获取路径，判断路径的合法性
        for i in range(3):
            if i == 3:
                print("小丁很生气，三次都输入不对，不要你输入了！！！")
                break
            # 获取文件的绝对路径，如果是项目内的文件，直接通过名称就可以获取,项目外的就只能传入的时候写全路径，否则获取的时候会以项目所在的当前系统目录进行添加获取，并不一定存在
            fullzipfilepath = os.path.abspath(zipfilepath)
            # 获取解压出来的文件根目录,截取后列表的第一个元素的所有字符，当然后面的【0：】是否添加都无所谓
            unzipdir = fullzipfilepath.split('.zip')[0][0:]
            print("压缩包的路径不带后缀名是", unzipdir)
            if not os.path.exists(fullzipfilepath):  # 如果输入的路径实际不存在，我们就让重新输入，给三次机会
                zipfilepath = input("第%d次传入的路径是%s在系统中不存在，请输入正确的压缩文件路径:" % (i, fullzipfilepath))
                i += 1
                continue
            elif fullzipfilepath.find(".zip") < 0:  # 我们不用index，这个要是没找到就抛出异常，看着不爽，当然也可以自己去处理
                zipfilepath = input("文件名不是zip压缩文件，输入的文件名有问题")
                i += 1
                continue
            else:
                print("路径存在，我们将进行解压")
                # 进行解压：
                print("压缩包的路径和名称是", fullzipfilepath)
                zf = zipfile.ZipFile(fullzipfilepath, "r")  # 读取压缩包，获取压缩包文件列表
                for filename in zf.namelist():
                    temppath = os.path.join(unzipdir, filename)  # 获取到的路径有正反斜杠
                    # print('88888',temppath);   liunx下不存在这种斜杠的问题可以不用处理
                    filepath = os.path.normpath(temppath)  # 转换之后，斜杠正常
                    print("当前我们处理的压缩包内文件是", filepath)
                    # 获取目录的名字，如果不存在，就先创建目录
                    dirname = os.path.dirname(filepath);
                    if not os.path.exists(dirname):
                        os.makedirs(dirname)  # 递归创建目录，如果使用makedir如果上一层不存在就会报错，要创建的存在也会抛出异常
                    print("333333", filename)
                    # print(zf.getinfo(filename))  # 这个信息包含内容较多，我们可以获取名称或者压缩率等信息
                    zf.extract(filename)  # 自动进行了解压下一层和命名保存，根据filename进行的处理创建路径和文件
                zf.close();
                # os.remove(filename) 当然也可以先把原来的压缩包删除掉
                break;


if __name__ == '__main__':
    zipfilename = "my.zip";
    compress.unzip_dir(zipfilepath=zipfilename);