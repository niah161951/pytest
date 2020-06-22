# -*- coding: utf-8 -*-
import requests
from SHDY.Public.data import Mock
from SHDY.Public.conf import Config
seqNo = Mock().Data_time()
mercMbl = Mock().get_phone()
mercAbbr = Mock().get_Company()
mercId = Config().get_param("ME")



url = 'http://192.168.20.171:8080/DemoJava/microMerchant/atUpdate'
data = {
    'orgNumber': '147',  # 机构代码
    'seqNo': seqNo,  # 请求流水号
    'updType': '2',  # 类型  1基本  2结算  3费率
    'mercId': mercId,  # 电银商户号
    'mercMbl': '17690151611',  # 商户手机号  1
    'mercAbbr': '前玄赵之',  # 商户简称    1
    'busAddr': '上海市浦东新区',  # 营业地址    1
    'stlWcLbnkNo': '310290098625',  # 联行行号     2
    'stlOac': '6217920175986368',  # 银行账号     2
    'bnkAcnm': '测试二',  # 银行开户名称 2
    'debitFee': '0.005',  # 借记费率        3
    'debitFeeLimit': '25',  # 借记封顶额      3
    'creditFee': '0.005',  # 贷记费率        3
    'd0Fee': '0.005',  # D0额外手续费费率3
    'd0FeeQuota': '0.005',  # D0额外定额手续费3
    'unionCreditFee': '0.005',  # 云闪付贷记费率  3
    'unionDebitFee': '0.005',  # 云闪付借记费率  3
    'aliFee': '0.005',  # 支付宝费率      3
    'wxFee': '0.005',  # 微信费率        3
    'sign': '0',  # 签名
    'YHK': '',  # 银行卡正面
    'QT1': '',  # 其他1
    'QT2': ''  # 其他2
}
# print(data)
a = requests.post(url=url, json=data).json()
print(a)
