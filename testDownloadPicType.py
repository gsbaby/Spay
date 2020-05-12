import sys
from savePicToLocal import getAPIImage
from savePicToLocal import getUrlImage
from savePicToLocal import get_image_jsp_aspx

# 保存从对方请求接口中获取图片
getAPIImage('壁纸', 15, './download/API/')

# 保存直接从网页中已有的图片
url = "http://imglf0.nosdn.127.net/img/RWppUi92Wk1nQzFtTUtCdUdwY2Vkd1pPekVqZ1RhT0VRZVJkeFhRanc0d2Vwa2dVUmUrR25RPT0.jpg?imageView&thumbnail=500x0&quality=96&stripmeta=0&type=jpg"
imgPathUrl = './download/URL/pic_URL.png'
getUrlImage(url, imgPathUrl)

# 保存jsp或aspx这类的动态变化图片
url_jsp_aspx = 'http://my.cnki.net/elibregister/CheckCode.aspx'
imgPath_jsp_aspx = './download/jsp_aspx/pic_jsp_aspx.png'
get_image_jsp_aspx(url_jsp_aspx, imgPath_jsp_aspx)


