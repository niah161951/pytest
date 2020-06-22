#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/5/25 11:25
import requests
from untitled.SHDY.Public.conf import Config
mercid = Config().get_param("mercId")

url = 'http://116.228.47.74:18280/merchant_agent/rest/terminal/binding'
data = {
     "tsn":"V90T00000041",
     "dyTermNo":"08001342",
     "dyMchNo":mercid
}
req = requests.post(url,json=data).json()
print(req)