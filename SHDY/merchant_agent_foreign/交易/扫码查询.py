# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/3/5 15:25
import requests
from   untitled.SHDY.Public import conf,data
import json

mer_order_no = conf.Config().get_param('mer_order_no')
merc_id = '872112378410001'#商户号
org_id = '125'  #机构号
url = 'http://192.168.31.161:28380/test_agent/testScan/getSign'
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
sign = requests.post(url,json=data).text

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

reg = requests.post(url,json=data).json()
rea = json.dumps(reg,indent=2,sort_keys=True)
print(rea)