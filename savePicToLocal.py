import requests
import json
import urllib
import urllib.request
import requests


# 图片地址
def getUrlImage(url, imgPath):
    img = requests.get(url)
    f = open(imgPath, 'ab')  # 存储图片，多媒体文件需要参数b（二进制文件）
    f.write(img.content)  # 多媒体存储content
    f.close()
    print('URL Download complete!')


def getAPIImage(category, length, path):
    n = length
    cate = category
    imgs = requests.get(
        'http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=' + cate + '&tag=%E5%85%A8%E9%83%A8&start=0&len=' + str(
            n))
    jd = json.loads(imgs.text)
    jd = jd['all_items']
    imgs_url = []
    for j in jd:
        imgs_url.append(j['bthumbUrl'])
    m = 0
    for img_url in imgs_url:
        print('***** ' + str(m) + '.jpg *****' + '   Downloading...')
        urllib.request.urlretrieve(img_url, path + str(m) + '.jpg')
        m = m + 1
    print('API Download complete!')


# 保存jsp_aspx后缀的图片到jsp_aspx文件夹下
def get_image_jsp_aspx(imageUrl, imgPath):
    u = urllib.request.urlopen(imageUrl)
    data = u.read()
    f = open(imgPath, 'wb')
    f.write(data)
    f.close()
    print('_jsp_aspx Download complete!')
