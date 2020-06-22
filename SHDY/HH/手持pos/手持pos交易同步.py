# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/3 13:58
import requests
import time
from SHDY.Public import   The_random_number
from SHDY.Public.conf import Config
mercId = Config().get_param('mercIdshouchi')
orderId = The_random_number.order_number()
tradeDate = time.strftime("%Y%m%d", time.localtime())
orderTime = (time.strftime("%Y%m%d", time.localtime()))+'124433'
#print(orderTime)
url = 'https://116.228.47.74:6443/transaction_agent/tel/pos'
data = {
 "crdNo": "620522003352912750",        #交易卡号
 "mercId": mercId,             #商户号DYF801000317  DYF801000326
 "orderId": orderId,                     #外部订单号
 "orderTime": "20200310124433",        #时间  当前时间昨天和今天
 "orgId": "113",                       #机构号
 "payType": "0",                        #0：银行卡1：支付宝2：微信3：银联二维码
 "seqNo": orderId,                       #流水号
 "setDate": "0110",                     #清算日期
 "trmNo":"133",                            #终端号
 "isFirst":"0",                        #0非首刷 1首刷
 "baseStation":"460|00|6334|20504",                         #基站信息
 "sign": "A/xX/MmqZtdBiPpDA0UBV88VZnlpRKVNMtXHf+XArCXMc2fRYjEkEc+GGomMyhk7juTJBftfBua4Spun3fqdNqRMNN5pV94gWo8S0wBf/rVmeH0MX2Vq/FnvGTgXCYHje89urf546Cj7DkjWDwMZhQt9GOq6+IDe++RgBds39c8=",
 "tranCode": "MP001",             #交易码
 "transAmt": "10",              #金额
 "transFee": "2",                #手续费
 "uniMercId": "872290453110002",  #银联商户号
 "uniSeqNo": "123456"            #系统跟踪号
}
res = requests.post(url,json=data,verify=False).json()
tradeNo = res['seqNo']
# Config().set_param('tradeNo',res['seqNo'])
print(res)

url = 'http://localhost:8080/DemoJava/settle/posMer/pay'
data = {
          "fee": "2",            #代付手续费
          "mercId": mercId,    #快速商户号  DYF801000326
          "orgNumber": "113",  #机构号
          "settAmt": "6",       #代付金额
          "tradeDate": tradeDate,
          "tradeNo": tradeNo,
          "tradeTime": "124433"
}
reg = requests.post(url, json=data).json()
print(reg)