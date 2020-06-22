#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/5/22 15:01
import time,unittest,json,requests
from SHDY.Public import data_url, data,conf
from SHDY.Public.log import logs

url = data_url.Url().url()
mer_order_no = data.Mock().get_card_number()
bar_code = '2885640096846523193'                     #付款码
pay_type = '02'                       #支付方式  01 微信   02支付宝
merc_id = '872112378410001'            #商户号
org_id = '125'                         #机构号
pay_amount = '1'                       #金额（分）
log = logs()
#conf.Config().set_param("mer_order_no",str(mer_order_no))

class Be_Swept(unittest.TestCase):
    '''被扫'''
    def setUp(self):
        self.url = url['标准版扫码加签']
        self.url1 = url['标准版扫码验签']
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_beisao(self):
        data = {
            "body": {
                "trancde": "P00",
                "mer_order_no": mer_order_no,
                "pay_amount": pay_amount,
                "order_name": "testName",
                "pay_type": pay_type,
                "bar_code": bar_code
            },
            "head": {
                "trm_sn": "061310000003",
                "imei": "061310000003",
                "merc_id": merc_id,
                "trm_id": "08001435",
                "org_id": org_id,
                "send_time": "20190813195059",
                "station_info": "460|00|6334|20504",
                "sign": "ThisIsSignPleasePressButton"
            }
        }
        sing = requests.post(self.url, json=data).text
        data = {
            "body": {
                "trancde": "P00",
                "mer_order_no": mer_order_no,
                "pay_amount": pay_amount,
                "order_name": "testName",
                "pay_type": pay_type,
                "bar_code": bar_code
            },
            "head": {
                "trm_sn": "061310000003",
                "imei": "061310000003",
                "merc_id": merc_id,
                "trm_id": "08001435",
                "org_id": org_id,
                "send_time": "20190813195059",
                "station_info": "460|00|6334|20504",
                "sign": sing
            }
        }

        req = requests.post(self.url1, json=data).json()
        rea = json.dumps(req, indent=2, sort_keys=True)
        log.info('被扫：%s'%rea)
        print(rea)

    def test_query(self):
        data = {
            "body": {
                "trancde": "PF0",
                "mer_order_no": mer_order_no
            },
            "head": {
                "trm_sn": "061310000003",
                "imei": "061310000003",
                "merc_id": merc_id,
                "trm_id": "08001435",
                "org_id": org_id,
                "send_time": "20200305152633 ",
                "station_info": "460|00|6334|20504",
                "sign": "ThisIsSignPleasePressButton"
            }
        }
        sign = requests.post(self.url, json=data).text

        data = {
            "body": {
                "trancde": "PF0",
                "mer_order_no": mer_order_no
            },
            "head": {
                "trm_sn": "061310000003",
                "imei": "061310000003",
                "merc_id": merc_id,
                "trm_id": "08001435",
                "org_id": org_id,
                "send_time": "20200305154957 ",
                "station_info": "460|00|6334|20504",
                "sign": sign
            }
        }
        reg = requests.post(self.url1, json=data).json()
        rea = json.dumps(reg, indent=2, sort_keys=True)
        log.info('查询：%s'%rea)
        print(rea)

    def test_refund(self):
        data = {
            "body": {
                "trancde": "P01",
                "mer_order_no": mer_order_no
            },
            "head": {
                "trm_sn": "061310000003",
                "imei": "061310000003",
                "merc_id": merc_id,
                "trm_id": "08001435",
                "org_id": org_id,
                "send_time": "20190813195059",
                "station_info": "460|00|6334|20504",
                "sign": "ThisIsSignPleasePressButton"
            }
        }
        sing = requests.post(self.url, json=data).text

        data = {
            "body": {
                "trancde": "P01",
                "mer_order_no": mer_order_no
            },
            "head": {
                "trm_sn": "061310000003",
                "imei": "061310000003",
                "merc_id": merc_id,
                "trm_id": "08001435",
                "org_id": org_id,
                "send_time": "20190813195059",
                "station_info": "460|00|6334|20504",
                "sign": sing
            }
        }
        reg = requests.post(self.url1, json=data).json()
        rea = json.dumps(reg, indent=2, sort_keys=True)
        log.info('退款：%s'%rea)
        print(rea)

