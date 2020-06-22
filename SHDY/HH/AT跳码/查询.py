#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/6/9 14:25
import requests
from SHDY.Public import data,conf
out_order_no = data.Mock().get_time()

url = 'http://192.168.31.161:18380/transaction_agent/scan/trans'
date = {
    "head": {
        "merc_id": "114305858120000",
        "trm_id": "08231257",
        "org_id": "101",
        "sign":"iJsiOwlvt0tclkkTlhEqQN1OtgOVnRlFOzfrIaJ44Bn2dDOdJapUvv8stnuXVvh+oznESu0P10yHjC8momjEjocYFqL16JVw0AH3w/VsJfXpfAV4vE9a8UQFVUIjtOJRpivCWttqF098kyb8nA8heYJsXij7HHKvH6JAyXKSBhE=",
        "dev_typ": "3",
        "ios_typ": "IOS",
        "ios_ver": "ios9.0",
        "dev_id": "868145017549928",
        "dev_bra_nm": "iPhone",
        "dev_mod_nm": "iPhone 11",
        "mac": "AA:BB:AA:DD:CC:FF",
        "ip_ver": "ipv4",
        "ip": "180.164.182.174",
        "pick_mer_id": "872290045110204",
        "pick_term_no": "08000181"
    },
    "body": {
        "mer_order_no": "5566383951532032",
        "out_order_no": out_order_no,
        "trancde": "PF0",
        "bar_code": "280537938517502605",
        "pay_amount": "1",
        "order_name": "扫码交易",
        "order_desc": ""
    }
}
rea = requests.post(url,json=date).json()
print(rea)