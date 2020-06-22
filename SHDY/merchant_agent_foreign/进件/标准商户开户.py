# -*- coding: utf-8 -*-
import requests
from SHDY.Public.conf import Config
from SHDY.Public.data import Mock
from SHDY.Public.conf import Config

seqNo = Mock().Data_time()
mercMbl = Mock().get_phone()
mercCnm = Mock().get_Company()


url = "http://192.168.20.171:8081/DemoJava/standardMerchant/coming"
data = {
      "agentNumber": "114",
      "orgNumber": "114",
      "mercCnm":mercCnm,
      "seqNo":seqNo,
      "mercAttr": "9",  # 商户类型1 – 标准商户（个体）9- 其他（企业）
      "stlSign": "1",  # 结算账号公私标志，0:对公，1:对私 2，暂不结算
      "entAccBnkNm": "招商银行",  # 企业账户银行名称（商户性质为其他且结算账号公私标志为对私必传）
      "entAccNm": "对公企业账户名称",  # 企业账户名称（商户性质为其他且结算账号公私标志为对私必传）
      "entAccNo": "6228480899999911",  # 企业账号（商户性质为其他且结算账号公私标志为对私必传）
      "aliFee": "0.0038",
      "aliFlg": "0",
      "bnkAcnm": "测试",   # 银行开户名称
      "busAddr": "shanghai",
      "creditFee": "0.006",
      "crpExpDtD": "2099-02-22",
      "crpIdNo": "360101198501010013",
      "crpIdTyp": "0",
      "crpNm": "测试",  # 法人姓名
      "d0Fee": "0.006",
      "d0FeeQuota": "1",
      "debitFee": "0.006",
      "debitFeeLimit": "1000",
      "jsAppFee": "0.006",
      "jsAppFlg": "0",
      "mccCd": "7999",
      "mercAbbr": "shanghaizhangj",
      "mercCity": "2900",
      "mercCounty": "2904",
      "mercHotLin": "021-5169331",
      "mercMbl": "13119554119",
      "mercProv": "2900",
      "outMercId": "11111111122233",
      "pMerId": "",
      "pType": "",
      "regExpDtD": "2099-02-22",
      "regId": "564SD64DSDFT",
      "settType": "T1",
      "sign": "",
      "stlOac": "620200310480733936",
      "stlWcLbnkNo": "102290071634",
      "unionCreditFee": "0.006",
      "unionDebitFee": "0.006",
      "unionFlg": "0",
      "usrOprEmail": "0000@122.com",
      "wxFee": "0.0038",
      "wxFlg": "0"
}


res = requests.post(url, json=data).json()
Config().set_param("MER",res["mercId"])
print(res)
