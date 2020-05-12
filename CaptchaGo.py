import tesserocr
from PIL import Image
from savePicToLocal import get_image_jsp_aspx


def getUrlPic():
    # 保存jsp或aspx这类的动态变化图片
    url_jsp_aspx = 'http://my.cnki.net/elibregister/CheckCode.aspx'
    imgPath_jsp_aspx = './download/jsp_aspx/pic_jsp_aspx.png'
    get_image_jsp_aspx(url_jsp_aspx, imgPath_jsp_aspx)
    dealPic(imgPath_jsp_aspx)


def dealPic(picPath):
    # 获取图像
    image = Image.open(picPath)
    # 图像预处理
    # 转化灰度值
    image_L = image.convert('L')
    image_L.show()
    # # 转化二值化——结果不太理想的操作
    # image_2 = image.convert('1')
    # image_2.show()
    # 再指定二值化阈值
    threshold = 160
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image_2_ehreshold = image_L.point(table, '1')
    image_2_ehreshold.show()
    result = tesserocr.image_to_text(image)
    print('1111', result.replace(' ', ''))
    result_2_ehreshold = tesserocr.image_to_text(image_2_ehreshold)
    print('2222', result_2_ehreshold.replace(' ', ''))


getUrlPic()
