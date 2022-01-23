from PIL import Image
# 如果PIL没有，改为 pip3 install Pillow
# 图像旋转
def readImg():
    # 读取图像
    im = Image.open("power.png")
    # 上下、左右翻转；逆时针90、180、270等角度的旋转
    out = im.transpose(Image.FLIP_LEFT_RIGHT)
    # out = im.transpose(Image.FLIP_TOP_BOTTOM)
    # out = im.transpose(Image.ROTATE_90)
    # out = im.transpose(Image.ROTATE_180)
    # out = im.transpose(Image.ROTATE_270)

    out.save('newImg.png')
    # out.show();
    # im.show()


readImg()
