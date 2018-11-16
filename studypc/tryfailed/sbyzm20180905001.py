from PIL import Image,ImageEnhance,ImageFilter,ImageDraw
'''
这种思路不能对验证码干扰线进行处理，理论上分析思路正确，实际上，放大可以看到实际不是这样的，所以放弃20180905
'''

image_linux_path = "/media/lipengchao/study/pycharmproject/studypc/common/img/yzm20180906.png"
image=Image.open(image_linux_path)
# 灰化
image=image.convert("L")
# 对图片进行处理，二值化图片
table=[]
for i in range(256):
    if i<127:
        table.append(0)
    else:
        table.append(1)
image=image.point(table,"1")
'''
去除干扰线
干扰线特点分析
干扰横线:像素上下位置像素为空白
干扰竖线:像素左右位像素为空白
干扰斜线或干扰点:像素上下左右像素为空白
'''
w=image.width
h=image.height
image.show()
# 获取在图片范围内每个点的上下左右位置,外层找到每一行的点，内层处理每一横向点的纵向
for x in range(1,w-1):
    left=x-1
    right=x+1
    for y in range(1,h-1):
        up=y-1
        down=y+1
        # 将距离边框2个像素的地方直接设为背景黑色，（结果发现这样反而会将边角的内容破坏）其他地方如果为白色就说明有东西，在判断四周情况
        # if x>=w-2 or x<=2:
        #     image.putpixel((x,y),0)
        # elif y>=h-2 or y<=2:
        #     image.putpixel((x,y),0)
        # 如果像素位置的颜色和字体颜色一致，那么获取周围像素点颜色 0为黑色  255为白色,这个位置是错误的思路，实际获取颜色发现黑白只有0和1，所以下面循环都没用
        # print('当前像素点是%s%s颜色是%s'%(x,y,image.getpixel((x,y))))
        if image.getpixel((x,y))==1:
            # 正方向  以目标像素点为中心店,获取周围像素点颜色
            upcolor=image.getpixel((x,up))
            downcolor=image.getpixel((x,down))
            leftcolor=image.getpixel((left,y))
            rightcolor=image.getpixel((right,y))

            # 斜方向
            leftupcolor=image.getpixel((left,up))
            leftdowncolor=image.getpixel((left,down))
            rightupcolor=image.getpixel((right,up))
            rightdowncolor=image.getpixel((right,down))

            # 去除竖线干扰，如果下面为横线白色，就判断左边和左下以及右边，右下是不是全是黑色，如果全是黑色，那就说明这个像素位置不是字，字体的话，周围不可能全部是背景（这种如果是数字1我看要凶多吉少了）
            if downcolor==1:
                if leftcolor==0 and leftdowncolor==0 and rightcolor==0 and rightdowncolor==0:
                    image.putpixel((x,y),0)

            # 去除横干扰线
            if rightcolor==1:
                if rightdowncolor==0 and rightupcolor==0 and upcolor==0 and downcolor==0:
                    image.putpixel((x,y),0)

            # 去除斜线，如果当前点不是背景色，上下左右正方向都是背景色说明就是斜线
            if upcolor==0 and downcolor==0 and leftcolor==0 and rightcolor==0:
                image.putpixel((x,y),0)


image.show()
