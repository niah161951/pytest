#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/6/4 10:12
import requests
from SHDY.Public import data,conf

seqo = data.Mock().get_time()
print(seqo)
# merid = data.Data().Data_merchants()['HH快速商户']
# merid = data.Data().Data_merchants()['HH小微商户']
merid = data.Data().Data_merchants()['HH标准商户']

bar_code = '287569781775576805'
pay_amount = '1'
#以一下字段确认跳码
pick_mer_id = data.Data().Data_merchants()['HH池商户']
pick_term_no = '08000181'
# pick_mer_id = "872103658120708"     #872103658120708  872290476920001
# pick_term_no = '08231616'           #08231616  08000493
conf.Config().set_param('外部订单号',str(seqo))

url = 'http://192.168.31.161:18380/transaction_agent/scan/trans'
date = {
    "head": {
        "merc_id": merid,
        "pick_mer_id": pick_mer_id,
        "pick_term_no": pick_term_no,
        "station_info":"116.231280,40.220770&上海市浦东新区",#跳码商户
        "trm_id": "08231257",
        "org_id": "101",
        "sign":"Pkb9ZbxckUGvCU6BKafhBFm5U8hM5EWqRe6Ys09SSn2LkHYZpLmcJCchNfgAT8Gi0/aweZ8peSDu2BziNrLuj5HE6dgnbIsKPXy5jjduzzHv5oqAU7aXarDdBxcDRSrKPZOpZGTG80zgHJKMkRkpjpEMHr53A/nw79pbqVkwSf4=",
        "dev_typ": "3",
        "ios_typ": "IOS",
        "ios_ver": "ios9.0",
        "dev_id": "868145017549928",
        "dev_bra_nm": "iPhone",
        "dev_mod_nm": "iPhone 8s",
        "mac": "AA:BB:AA:DD:CC:FF",
        "ip_ver": "ipv4",
        "ip": "180.164.182.174"
        # "mchFlag":"121.601768", #经纬度
        # "lonLat":"31.18486",    #经纬度
        # "address":"上海金科路",
    },
    "body": {
        "mer_order_no": seqo,
        "out_order_no": "",
        "trancde": "P00",  # P00：默认值，支持微信、支付宝、云闪付 交易码
        "bar_code": bar_code,  #付款码
        "pay_amount": pay_amount, #金额
        "undiscountable_amount": "",
        "order_name": "扫码交易",
        "order_desc": ""
    }
}
req = requests.post(url,json=date).json()
print(req)













