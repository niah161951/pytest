# -*- coding: utf-8 -*-
import requests
from SHDY.Public import The_random_number

seqNo = The_random_number.order_number()
mercCnm = The_random_number.get_name()

url = 'http://116.228.47.74:18280/merchant_agent/rest/merchantInfo/updateMerInfoByDyMchNo'
data = {
    'seqNo':seqNo,	               #流水号
    'mercType':'3',	               #快速、标准1 快速（秒过）2 标准（审核）3 小微（审核）
    'updType':'2',	               #类型 1基本 2结算 3费率 4状态
    'mercId':'101290148160000',	   #电银商户号
    #'unionFlg':'1',	           #是否开通云闪付
    #'mchStatus':'0',	           #商户状态0：正常 1：关闭
    #'settStatus':'0',	           #商户结算状态0 – 正常 1 – 关闭
    #'mercMbl':'13119188213',	   #商户手机号
    #'mercCnm':'后天赵人昆',	   #商户名称
    #'stlSign':'0',	               #结算账号公私标志0：对公 1：对私  2
    #'mercStlFlg':'0',	           #商户结算实时标志0：实时 1：非实时 2
    #'bankNm':'中国银行',	       #银行名称  2
    #'opnBnkProv':'01',	           #支行归属省份  2
    #'opnBnkCity':'100',	       #支行归属地市  2
    #'stlWcLbnkNo':'313100001467', #联行行号  2
    #'stlOpnBnkDesc':'中国银行股份有限公司北京分行',	#结算银行名称   2
    #'expDtD':'20201118',	                        #协议到期日
    'debitFee':'0.0068',	                        #借记费率  3
    'debitFeeLimit':'30.00',	                        #借记封顶额   3
    'creditFee':'0.0068',	                        #贷记费率   3
    'creditFeeLimit':'99999',	                    #贷记封顶额
    'dFee':'0.001',	                                #D0费率    3
    'dStlBegAmt':'100',  	                        #D0起始结算金额
    'unionCreditFee':'0.0068',	                    #银联二维码贷记费率   3
    'unionDebitFee':'0.0068',	                    #银联二维码借记费率   3
    'cloudDebitFee':'0.0068',	                    #云闪付借记费率    3
    'cloudCreditFee':'0.0068',	                    #云闪付贷记费率        3
    'limitDebitFee':'0.0068',	                    #小额双免借记费率    3
    'limitCreditFee':'0.0068',	                    #小额双免贷记费率       3
    'aliFee':'0.0068',                              #支付宝费率    3
    'wxFee':'0.0068'	                            #微信费率    3
}
res = requests.post(url,json=data).json()
print(res)