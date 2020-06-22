# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/4/9 13:37

import  requests
from SHDY.Public import The_random_number
orderId = The_random_number.order_number()

url = 'http://192.168.28.79:8001/VerifySignAndSignController/Sign'
data = {
 "sourceData":"{\"head\":{\"version\":\"1.0\",\"reqTime\":\"20200325202716\",\"reqId\":\"2020032335567801763\",\"orgId\":\"127\"},\"body\":{\"tranCode\":\"AT002\",\"mercId\":\"872290453310066\",\"subMercId\":\"888888888888888\",\"trmId\":\"12345678\",\"orderId\":orderId,\"orderTime\":\"20200408221530\",\"orderDesc\":\"零食\",\"payType\":\"1\",\"crdNo\":\"6225802030041508\",\"transAmt\":\"10000\",\"mercFee\":\"10\",\"agtFeeAmt\":\"1.03\",\"subsidyAmt\":\"1.02\",\"batNo\":\"000001\",\"setDate\":\"20200327\",\"uniOrderId\":\"20190203\",\"crdFlg\":\"00\",\"transType\":\"0\",\"replay\":\"Y\",\"stationInfo\":\"MCC|MNC|LAC|CID\"}}",
 "privateKeyIndex":"08"
}

a = requests.post(url,json=data).json()
b = a["signData"]
print(b)


url = 'http://192.168.20.36:8090/trade/data/receive'
data = {
 "head": {
  "version": "1.0",
  "reqTime": "20200325202716",
  "reqId": "2020032335567801763",
  "orgId": "127"
 },
 "sign":b,
 "body": {
  "tranCode": "AT002",
  "mercId": "872290453310066",
  "subMercId": "888888888888888",
  "trmId": "12345678",
  "orderId": orderId,
  "orderTime": "20200408221530",
  "orderDesc": "零食",
  "payType": "1",
  "crdNo": "6225802030041508",
  "transAmt": "10000",
  "mercFee": "10",
  "agtFeeAmt": "1.03",
  "subsidyAmt": "1.02",
  "batNo": "000001",
  "setDate": "20200327",
  "uniOrderId": "20190203",
  "crdFlg": "00",
  "transType": "0",
  "replay": "Y",
  "stationInfo": "MCC|MNC|LAC|CID"
 }
}

res = requests.post(url,json=data).json()
print(res)