#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/6/4 16:23
import requests,time
from SHDY.Public import data,conf,data_url

seqo = data.Mock().get_order()
merid = '10110348111008f'  # 快速商户
merid1 = '101290459460002' # 小微商户
merid2 = '114305858120000' # 标准商户

#以一下字段确认跳码
pick_mer_id = "872290045110204"
pick_term_no = '08000181'
# pick_mer_id = "872290476920001"
# pick_term_no = '08000493'
conf.Config().set_param('外部订单号',str(seqo))

url = 'http://192.168.31.161:18380/transaction_agent/scan/trans'
date = {
    "head": {
        "merc_id": merid2,
        "station_info":"",#格式：LAT,LON|地理位置经纬度信息格式：LAT,LON
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
        "ip": "180.164.182.174",
        "mchFlag":"121.601768",
        "lonLat":"31.18486",
        "address":"上海金科路",
        "pick_mer_id":  pick_mer_id,
        "pick_term_no": pick_term_no
    },
    "body": {
        "pay_amount": "1",#金额
        "trancde": "P05",  # P03 微信动态码  P04 云闪付二维码  P05 支付宝动态码
        "mer_order_no":seqo ,
        "notify_url": "http://192.168.31.161:28380/test_agent/notify/async"
    }
}

req = requests.post(url,json=date).json()
print(req)
url = req['body']['code_url']
dr = data_url.Driver().dr()
dr.get('https://cli.im/')
dr.find_element_by_id('text-content').send_keys(url)
dr.find_element_by_id('click-create').click()
time.sleep(15)
dr.quit()













