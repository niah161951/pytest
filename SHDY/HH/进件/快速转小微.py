# -*- coding: utf-8 -*-
import requests
from SHDY.Public.data import Mock
from SHDY.Public.conf import Config

seqNO = Mock().get_time()
mercCnm = Mock().get_Company()
mercid = Config().get_param("mercId")
ip = 'http://116.228.47.74:18280/merchant_agent/rest/'

url = ip+'microMerAppend/inComing'
data = {
        'seqNo':seqNO,	#请求流水号
        'mercId': mercid,	#电银商户ID
        'mercCnm':mercCnm,	#商户名称
        'mercAbbr':mercCnm,        	#商户简称
        'crpExpDtD':'20991020',    	#法人证件过期日期
        'busAddr':'上海浦东小卖部',	#营业地址
        'aliFee':'0.0038',          	#支付宝费率
        'wxFee':'0.0038',           	#微信费率
        'aliFlg':'1',          	#是否开通支付宝 0 开通，1 不开通　
        'aliItem':'0',         	#支付宝类目
        'wxFlg':'1',           	#是否开通微信 0 开通，1 不开通　
        'wxItem':'0',         	#微信类目
        'mccCd':'5331',           	#MCC码
        'zipFilePath':'data2/upload/20190730/208605112376098816.zip'	#附件名
    }
res = requests.post(url,json=data).json()
print(res)