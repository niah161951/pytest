# -*- coding: utf-8 -*-
import requests
from SHDY.Public.conf import Config
from SHDY.Public.data import Mock

seqNo = Mock().Data_time()
mercMbl = Mock().get_phone()
mercAbbr = Mock().get_Company()


url = 'http://192.168.20.171:8081/microMerchant/atInComing'
data = {
       "orgNumber": "114",
       "agentNumber": "114",
       "seqNo": seqNo,
       "mercMbl": mercMbl,  # 商户手机号
       "mercCnm": "商户hahh",
       "mercAbbr": mercAbbr,
       "mccCd": "7999",
       "mercProv": "2900",
       "mercCity": "2900",
       "mercCounty": "2904",
       "busAddr": "上海小卖部",
       "crpIdNo": "360101198501010013",#身份证
       "crpExpDtD": "2099-02-22",
       "stlWcLbnkNo": "102290071634",  #联行号
       "stlOac": "620200310480733936", #银行卡
       "bnkAcnm": "测试",      #姓名
       "stlOacType": "",   # 账户类型标识
       "stlWcLbnkNo2": "",
       "stlOac2": "",
       "bnkAcnm2": "",
       "debitFee": "0.006",
       "debitFeeLimit": "100",
       "creditFee": "0.006",
       "d0Fee": "0.006",
       "d0FeeQuota": "1",
       "unionCreditFee": "0.006",
       "unionDebitFee": "0.006",
       "aliFee": "0.0038",
       "wxFee": "0.0038",
       "outMercId": "11111111122233",
       "settType": "T1",  #结算标识
       "pMerId": "",
       "pType": "",
       "stockFlag":"",
       "jsAppFlg": "",
       "jsAppFee": "",
       "sign": "",
       "SFZ1": "data2/upload/20190819/215839200669466624.zip",
       "SFZ2": "data2/upload/20190819/215839200669466624.zip",
       "SCZP": "",
       "YHK": "data2/upload/20190819/215839200669466624.zip",
       "CDMT1": "data2/upload/20190819/215839200669466624.zip",
       "XY1": ""
}


res = requests.post(url=url, json=data).json()
Config().set_param("ME",res["mercId"])
print(res)

