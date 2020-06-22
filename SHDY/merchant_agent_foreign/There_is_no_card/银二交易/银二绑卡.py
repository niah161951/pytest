# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/10 17:26
import requests
from SHDY.Public import The_random_number as a
from SHDY.Public.conf import Config
from time import sleep
from selenium import webdriver

mercid = Config().get_param("mercid")
mercid1 = Config().get_param("id")
#_ocx_cvn2 ='123'
smsCode = '111111'
seqNo = a.order_number()
url = 'http://localhost:8080/DemoJava/cardSign/cardBind'
data =  {
        'orgNumber':'121',              #机构号
        'dyMchNo':mercid,               #电银商户号
        'seqNo':seqNo,                  #请求流水号
        'cardNo':'6221558812340013',                    #银行卡号贷记卡
        'cardPhoneNo':'13552535506',        #银行卡预留手机号
        'cardIdNo':'341126197709218366',       #身份证号码
        'cardNm':'全渠道',                    #身份证姓名
        'cardCvn2':'123',                     #贷记卡安全码
        'cardExpired':'2311',          #贷记卡过期日期
        'frontUrl':'www.baidu.com',                     #前台通知地址
        'backUrl':'www.baidu.com',                      #后台通知地址
        'sign':'e7lL0yjBgkgtFVCQE30VsJ1Gf0XjOhbFvUeJDdN6G3JVQGfH53'                          #签名

}
reg = requests.post(url,json=data).json()
#re = json.dumps(reg,sort_keys=True,indent=2)
Config().set_param('seqno',reg['seqNo'])
unionPayHtml = reg['unionPayHtml']
filename = 'card.html'
with open(filename, 'w') as file_object:
    file_object.write(str(unionPayHtml))
#print(unionPayHtml)
print(reg)

def  front_end():
     driver = webdriver.Chrome('D:\chromedriver.exe')
     #driver.refresh()
     driver.get(r'D:\PycharmProject\untitled\SHDY\merchant_agent_foreign\There_is_no_card\银二交易\card.html')
     #嵌套
     driver.implicitly_wait(5)
     sleep(5)
     #driver.switch_to_frame('cardPay')
     #driver.switch_to_frame(driver.find_element_by_id('cardPay'))
     #driver.find_element_by_id('_ocx_cvn2').send_keys(_ocx_cvn2)
     driver.find_element_by_id('smsCode').send_keys(smsCode)
     driver.find_element_by_id('isCheckAgreement').click()
     driver.find_element_by_id('expireMonth').send_keys('11')
     driver.find_element_by_id('expireYear').send_keys('23')
     sleep(5)
     driver.find_element_by_id('btnCardPay').click()
     sleep(5)
     driver.quit()
     return
if __name__ == '__main__':
    front_end()
