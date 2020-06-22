# _*_ coding: utf-8 _*_
# 作者    : 一蓑烟雨任平生 
# 创建时间 : 2019/12/30 16:41
import requests
from SHDY.Public import data_url,data
logNo = data.Mock().get_card_number()

url = 'http://116.228.47.74:18280/merchant_agent/rest/agent/profit/pay'
data = {
        'agentNo':'00199',   #代理商编号
        'orgNo':'101',       #机构号
        'txnAmt':'1',       #金额
        'logNo':logNo       #流水号
}
reg = requests.post(url=url,json=data).json()
print(reg)
