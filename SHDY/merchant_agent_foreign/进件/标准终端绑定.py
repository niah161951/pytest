# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/3/23 13:21

import requests

url = "http://192.168.20.171:8080/DemoJava/terminal/stdBinding"
date = {
    'orgNumber':'127',       #机构号 是 String 最长 5 位
    'tsn':'88888',       #机具编号 是 String 最长 20 位
    'dyMchNo':'872121172300009',       #电银商户号 是 String
    'snSource':'1',       #机具来源 是 String 机具来源1 – 外部代理商(默认)2 – 电银代理商（当机具来源为“电银代理商”时, 外部终端号、终端厂家、终端型号非必传）
    'dyTermNo':'88888888',       #外部终端号 是 String 最长 8 位
    'termFactory':'45',       #终端厂家 是 String 机具厂商编号
    'termModel':'545',       #终端型号 是 String 机具型号编号
    'termName':'5454',       #终端名称 是 String （门店名称）
    'termAddress':'zhogn',       #终端地址 是 String （门店地址）
}
a = requests.post(url,json=date).json()
print(a)