# -*- coding: utf-8 -*-
# 作者  : 一蓑烟雨任平生
# 时间  : 2020/1/6 11:13
import requests
from tem import globalParam

logno = globalParam.get_orderNum()
#print(logno)
url = 'http://116.228.47.74:18280/merchant_agent/rest/fractionalTransfer/qry'
data = {
    'orgNo':'101', #机构号
    'logNo': logno  #流水号
}
reg = requests.post(url=url,json=data).json()
print(reg)