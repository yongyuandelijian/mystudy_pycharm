# 这种方式识别后，效果不是很理想，对于所有的点都打乱了
from PIL import Image
from numpy import *
import pytesseract
im = Image.open('F:\pycharmproject\studypc\common\img\yzm20180906.png')
im = im.convert('RGB')
#拉长图像，方便识别。这个方法有一点作用就是拉大之后有些字符被干扰的面积变小了就可以识别，但是这个不是解决问题的办法，毕竟有些干扰字符就是和字在一起的
im = im.resize((200,80))
a = array(im)
for i in range(len(a)):
    for j in range(len(a[i])):
      if a[i][j][0] == 255:
        a[i][j]=[0,0,0]
      else:
        a[i][j]=[255,255,255]
im = Image.fromarray(a)
im.show()
vcode = pytesseract.image_to_string(im)
print(vcode)