'''
自动识别验证码的功能，帮助爬虫自动登录
参数，传入二维码图片，输出二维码图片内容
李鹏超 20180809
'''

from PIL import Image,ImageFont,ImageDraw,ImageFilter    # 新版本的Python讲pil的功能整合到pillow中，所以就不用单独初始化pil，只需要初始化pillow，用法还是和以前一样
import random   # 用于产生随机数放在图片上，当然随机数之后链接到汉字或者图片也是可以的，我们这里先做一个基本的
import pytesseract # 用于识别图像中的文字
from numpy import *
import cv2

class yzm(object):
    fontlinuxpath="/usr/share/fonts/truetype/deepin/DeepinOpenSymbol6.ttf"  # Linux中使用
    fontwinpath="C:\Windows\Fonts\simsun.ttc"
    # 随机码,默认每次产生一个
    def ran_sjm(length=1):
        code=[]
        for i in range(length):
            #code+=str(random.randint(1,99))  # 不转换的话，会由于上面声明了字符串而报错,随机范围定在最大两位数,这样不能打印两位数字
            code.append(str(random.randint(1,9))) # 这样就可以产生多个字符的,但是显示起来两位数之间位置很大，两个数字之间位置很小
        return code

    # 随机颜色,产生一个rgb的随机数
    def ran_color(s=1,e=255):
        return random.randint(s,e),random.randint(s,e),random.randint(s,e)


    # 生成验证码 参数 长length  宽 width 高 height  ，返回图片和验证码信息

    def scyzm(length=4,width=120,height=40):
        image=Image.new('RGB',(width,height),(255,255,255)) # 创建图片对象，母版颜色全白
        font=ImageFont.truetype(yzm.fontwinpath,32)  # 我们使用默认字体当初始化
        imagedraw=ImageDraw.Draw(image)  # 获得一个imagedraw对象,类似与获取当前图像的画笔，后面才能使用画笔的point对每一个点进行绘制
        # 随机填充每个像素,由于测试的时候在家滤镜根本看不清，先不加
        for x in range(width):
            for y in range(height):
                imagedraw.point(xy=(x,y),fill=(random.randint(10,168)))  # 第一个参数是当前像素的x和y的坐标用来确定位置，第二个参数用来确定填充的颜色，颜色定义的过于靠近255会导致显示不清晰的几率增大

        # 验证码
        code=yzm.ran_sjm(length)

        # 将验证码写在图片上
        for i in range(length):
            # print(code[i]);
            imagedraw.text(xy=(30*i+random.randint(-3,3),1+random.randint(-3,3)),text=code[i],fill=yzm.ran_color(),font=font);
            # 在这里我们将干扰线也写在图片上，当然也可以单独用循环定义干扰线的条数
            begin = (random.randint(0,width-10), random.randint(0, height-5));  # 开始的像素位置
            end = (random.randint(0,width-20), random.randint(0, height-3));  # 高度随机来保证线条的弯曲不固定，宽度，看自己需要，初步先定在整个宽度的一半
            imagedraw.line(xy=[begin, end], fill=yzm.ran_color(), width=3);

        # 进行模糊滤镜
        image=image.filter(ImageFilter.EDGE_ENHANCE);  # 边界加强滤镜，过滤蓝光的滤镜会导致非常模糊，看自己需要来进行设置
        # print(code)
        # image.show();
        return code,image;


    # 识别验证码
    def sbyzm(image_path,fz):  # 图像和二值化的阈值
        # 打开并确认图片
        image=Image.open(image_path);

        # 对图片进行处理，灰化图片
        image=image.convert("L"); # 首先将颜色转为两种颜色
        # 对图片进行处理，二值化图片,我们把例子的颜色反过来，黑色字体，白色背景
        table=[];
        for i in range(256):
            if i<fz:
                table.append(1);
            else:
                table.append(0);
        # im.point(table) = > 图像im.point(function) = > 图像
        # 返回图像的副本，其中每个像素都通过给定的表进行映射。 该表应包含图像中每个波段的256个值。如果使用函数，则应该使用单个参数。对每个可能的像素值调用一次该函数，并将结果表应用于图像的所有波段。
        image=image.point(table,'1');
        # 对图片进行处理，去噪


        image.show();
        image.save("/media/lipengchao/study/pycharmproject/studypc/common/img/yzm20180906.png");
        code=pytesseract.image_to_string(image);  # 现在的问题就是识别有误差的问题，我们先将图片进行处理之后在进行识别
        print(code)
        return code;

'''
# code=tesseract.image_to_string(image); 都是不靠谱的，会提示找不到图片
# code=pytesser3.image_file_to_string(image);
# code=pytesser3.image_file_to_string(image_path)

'''

if __name__ == '__main__':
    # code,image=yzm.scyzm();
    # image.show();
    # image.save("img/yzm.png");
    image_win_path=r"F:\pycharmproject\studypc\common\img\yzm.png";    # 通过测试发现，图片有干扰颜色以及干扰线条的时候，都不能正确的进行识别，干扰颜色导致识别错误，干扰线条导致无法识别
    image_linux_path="/media/lipengchao/study/pycharmproject/studypc/common/img/yzm.png";
    code=yzm.sbyzm(image_linux_path,127);