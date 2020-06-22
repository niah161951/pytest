# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/4/11 10:30

import requests
import glob
from aip import AipOcr


url = 'http://36.152.36.9:7072/guacamole/api/tokens?1584270478800'
tu = requests.get(url)
with open('/Users/myfkmac/PycharmProjects/人脸识别/Tp/tu.jpg', 'wb+') as a:
    g = a.write(tu.content)
    print(g)
for o in glob.glob('/Users/myfkmac/PycharmProjects/人脸识别/Tp/*'):
    # print(o)
    APP_ID = '11352343'
    API_KEY = 'Nd5Z1NkGoLDvHwBnD2bFLpCE'
    SECRET_KEY = 'A9FsnnPj1Ys2Gof70SNgYo23hKOIK8Os'

    # 初始化AipFace对象
    aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # 读取图片
    filePath = o


    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
    }

    # 调用通用文字识别接口
    result = aipOcr.basicGeneral(get_file_content(filePath), options)
    print(result)
    words_result = result['words_result']
    # for i in range(len(words_result)):
    #     print(words_result[i]['words'])

    h = words_result[0]['words']
    print(h)


from aip import AipOcr
import re

""" 读取密码 """

#path="my_password.txt"
def getPassword():
    # with open(path, "r", encoding="utf-8") as f:

    APP_ID = '19764159'
    API_KEY = 'OK8BGswm2PAwtxL8xMG3FAvc'
    SECRET_KEY = 'AvQizGMHfvhGjVkTSTt9B5HGnOp87qnA'
    return APP_ID, API_KEY, SECRET_KEY

""" 读取图片 """

def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()



""" 识别图片内容 """
def getContent(file_path=r"E:\图片\123.jpg"):
    APP_ID, API_KEY, SECRET_KEY = getPassword()
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    image = get_file_content(file_path)
    """ 调用通用文字识别, 图片参数为本地图片 """
    res = client.basicAccurate(image)
    print(type(res))
    print(res)
    return res['words_result'][0]['words']

def get_str(res):
    result = re.sub('\W+', '', res).replace("_", '')
    print(result)
    return result

if __name__ == "__main__":

    res=getContent()
    get_str(res)
