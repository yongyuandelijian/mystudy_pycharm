# 给图片增加水印
from PIL import Image,ImageDraw,ImageFont

# 指定要使用的字体和大小 fontpath是取系统中的一个字体
# font=ImageFont.truetype("C:\Windows\Fonts\simsun.ttc",36)  windows下的
font=ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family-0.83/Ubuntu-BI.ttf",36)  # linux下 ,这个字体不支持汉字

class Addsy(object):
    # 添加自己想要的文字到图片上
    def addMynameToImage(image,text,font=font):
        rgba_image=image.convert("RGBA")  # 对图片对象进行转换
        newimage=Image.new('RGBA',rgba_image.size,(255,255,255,0))
        imagedraw=ImageDraw.Draw(newimage) # 画出图片
        # 设置画出的图片-文字位置
        text_x,text_y=imagedraw.textsize(text=text,font=font)
        text_xy=(rgba_image.size[0]-text_x,rgba_image.size[1]-text_y)
        # 设置文本的颜色和透明度
        imagedraw.text(xy=text_xy,text=text,fill=(76, 234, 124, 180),font=font)
        # 合成图片
        compositeImage=Image.alpha_composite(rgba_image,newimage)
        return compositeImage

    # 添加一个图片水印到传入的图片上,图片什么的还是一开始就应该新建文件夹保存起来,对于项目目录也不适合太过于深，造成处理起来比较麻烦
    def addwatermarktoImage(image,watermark):
        # 将两个图片转为rgba模式进行处理
        rgba_image=image.convert('RGBA')
        rgba_watermark=watermark.convert('RGBA')
        # 获取转换后的图片尺寸
        image_x,image_y=rgba_image.size
        watermark_x,watermark_y=rgba_watermark.size
        # 缩放水印图片
        scale=5
        # 基本图片/（水印图片×缩放倍数） 合并需要两个图片的比例参数，这里练习就做了这个缩放，当然如果水印图片合适，也可以不用缩放，直接计算比例
        watermark_scale=max(image_x/(scale*watermark_x),image_y/(scale*watermark_y))
        # 获取水印图片扩大后的尺寸，并且将水印图片扩大
        new_size=(int(watermark_x*watermark_scale),int(watermark_y*watermark_scale))
        rgba_watermark=rgba_watermark.resize(new_size,resample=Image.ANTIALIAS)  # anitalias 重新取样，抗锯齿平滑滤波
        # 透明度
        rgba_watermark_mask=rgba_watermark.convert("L").point(lambda x:min(x,180))   # L表示 8位像素，表示黑和白。 RGBA：4x8位像素，有透明通道的真彩色。,point函数代表对每个点进行 第二个参数/第一个参数 的倍数加强，这样由返回值可以看到只会变小，不会变大，获取到了一个透明度
        rgba_watermark.putalpha(rgba_watermark_mask) # 设置透明度
        # print('获取的透明度类型是：%'%type(rgba_watermark_mask))

        # 水印图片位置
        rgba_image.paste(rgba_watermark,(image_x-watermark_x,image_y-watermark_y),rgba_watermark_mask)
        return rgba_image


import datetime
if __name__ == '__main__':

    # 对一个图片做一个全面的水印处理
    image_path = "/media/lipengchao/Work/PycharmProjects/studypc/common/img/py20180807.jpg"
    text="AAA"+datetime.date.today().strftime("%Y-%m-%d")
    waterimg_path="/media/lipengchao/Work/PycharmProjects/studypc/common/img/watermark.jpg"
    before_image=Image.open(image_path)
    water_image=Image.open(waterimg_path)
    before_image.show()
    text_image=Addsy.addMynameToImage(image=before_image,text=text,font=font)
    text_image.show()
    result_image=Addsy.addwatermarktoImage(text_image,water_image)
    result_image.show()
    result_image.save("/media/lipengchao/Work/PycharmProjects/studypc/common/img/addsyimage.png")



    '''
    # 添加文本
    imagepath="/media/lipengchao/Work/PycharmProjects/studypc/common/img/py20180807.jpg"
    text="李鹏超的图片>>>"+datetime.date.today().strftime("%Y-%m-%d")
    # print(text)
    before_image=Image.open(imagepath)
    before_image.show()
    after_image=Addsy.addMynameToImage(before_image,text) # 引用方法
    after_image.show()
    # img=Image.open(r"F:\studyimageaddtext.jpg","wb")
    # img.save("addtextimgage.jpg")
    # 由于jpg不支持透明度的问题，所以如果需要保存为jpg需要将图片使用convert转为rgb才可以正常保存，但是png就不需要转换
    # img=after_image.convert("RGB")    # 然后在使用img.save("addtextimgage.jpg")去保存
    after_image.save("addtextimgage.png")  # 保存图片，如果已经有了就会自动覆盖
    '''
    '''
    # 添加图片
    image_path="/media/lipengchao/Work/PycharmProjects/studypc/common/addtextimgage.png"  # 测试了相对路径，不认识
    waterimage_path="/media/lipengchao/Work/PycharmProjects/studypc/common/img/watermark.jpg"
    before_image=Image.open(image_path)
    water_image=Image.open(waterimage_path)
    # print(before_image.getbands(),before_image.mode)
    before_image.show()
    after_image=Addsy.addwatermarktoImage(before_image,water_image)
    after_image.show()
    after_image.save("/media/lipengchao/Work/PycharmProjects/studypc/common/img/addimgimage.png")
    '''

