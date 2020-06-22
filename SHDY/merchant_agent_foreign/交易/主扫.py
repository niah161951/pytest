#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/6/9 17:08
import time,unittest,json,requests
from SHDY.Public import data_url, data,conf

mer_order_no = data.Mock().get_card_number()
print(mer_order_no)
bar_code = '134535568753825819'                      #付款码
pay_type = '01'                       #支付方式  01 微信   02支付宝
merc_id = '872112378410001'            #商户号
org_id = '125'                         #机构号
pay_amount = '1'                       #金额（分）

url = 'http://192.168.31.161:28380/test_agent/testScan/getSign'
date = {
        "body": {
            "trancde": "P03",
            "mer_order_no": mer_order_no,
            "pay_amount": pay_amount,
            "notify_url": "http://gggggggg.com"
        },
        "head": {
            "trm_sn": "061310000003",
            "imei": "061310000003",
            "merc_id": merc_id,
            "trm_id": "08001435",
            "org_id": org_id,
            "send_time": "20200609171347",
            "station_info": "460|00|6334|20504",
            "sign": "ThisIsSignPleasePressButton"
        }
    }
sign = requests.post(url,json=date).text
# print(sign)

url = 'http://192.168.31.161:28380/transaction_agent/scan/trans'
date = {
            "body": {
                "trancde": "P03",
                "mer_order_no": mer_order_no,
                "pay_amount": pay_amount,
                "notify_url": "http://gggggggg.com"
            },
            "head": {
                "trm_sn": "061310000003",
                "imei": "061310000003",
                "merc_id": merc_id,
                "trm_id": "08001435",
                "org_id": org_id,
                "send_time": "20200609171347",
                "station_info": "460|00|6334|20504",
                "sign": sign
            }
        }
res = requests.post(url,json=date).json()
datas = res['body']['code_url']

dr = data_url.Driver().driver()
dr.maximize_window()
dr.get('https://cli.im/')
dr.find_element_by_id('text-content').send_keys(datas)
dr.find_element_by_id('click-create').click()
time.sleep(15)
dr.quit()