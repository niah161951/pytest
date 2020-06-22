# _*_ coding: utf-8 _*_
# 作者    : 一蓑烟雨任平生
# 创建时间 : 2020/1/2 17:28
import requests
from SHDY.Public import The_random_number
rodNo = The_random_number.order_number()
from SHDY.Public.conf import Config

url = 'http://116.228.47.74:18280/merchant_agent/rest/agent/sett/req'
data = {
    "orgNo":"101",       #机构号
    "agentNo":"00005",   #代理商编号
    "amt":"5",           #提现金额
    "ordNo":rodNo        #商户订单号
}
req = requests.post(url=url,json=data).json()
sett = req['settOrdNo']
Config().set_param('settOrdNo',str(sett))
print(req)
