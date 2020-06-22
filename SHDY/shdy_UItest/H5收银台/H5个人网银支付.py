# -*- coding: utf-8 -*-
import time
from SHDY.Public import data_url, data,log,conf
from selenium.webdriver.common.keys import Keys
url = data_url.Url().url()
data = data.Data()
config = conf.Config()
dr = data_url.Driver().driver()
uat = 'sit'
dr.get(url[uat])

dr.implicitly_wait(5)
dr.find_element_by_id('MercId').clear()
dr.find_element_by_id('MercId').send_keys(data.Data_merchants()[uat+'商户'])
dr.find_element_by_id('MerchantCertPass').clear()
dr.find_element_by_id('MerchantCertPass').send_keys(data.Data_password()[uat])
#重置
dr.find_element_by_xpath('/html/body/center/form/table/tbody/tr[4]/td/input').click()
dr.find_element_by_xpath('/html/body/center/form/table/tbody/tr[30]/td/a').click()
#订单
orderId=dr.find_element_by_id('orderId').get_attribute('value')
conf.Config().set_param(uat+"H5个人网银支付",orderId)

dr.find_element_by_id('rcvMerchantId').clear()
dr.find_element_by_id('rcvMerchantId').send_keys(data.Data_merchants()[uat+'商户'])
dr.find_element_by_id('recEnterpriseId').clear()
dr.find_element_by_id('recEnterpriseId').send_keys(data.Data_merchants()[uat+'商户'])
#提交
dr.find_element_by_xpath\
    ('//*[@id="form1"]/center/table/tbody[3]/tr/td[2]/input[2]').click()
time.sleep(1)
dr.find_element_by_id('Submit').click()
#银联
dr.find_element_by_id('1').click()
time.sleep(1)
dr.find_element_by_id('submit').click()
#在线支付
dr.find_element_by_id('cardNumber').send_keys('6226090000000048')
dr.find_element_by_id('btnNext').click()
# dr.find_element_by_id('cellPhoneNumber').send_keys('111101')
# dr.find_element_by_id('cellPhoneNumber').send_keys(Keys.CONTROL,'a')
# dr.find_element_by_id('cellPhoneNumber').send_keys(Keys.CONTROL,'x')
# dr.find_element_by_id('cellPhoneNumber').send_keys(Keys.CONTROL,'x')
# dr.find_element_by_id('_ocx_password').send_keys(Keys.CONTROL,'v')
# dr.find_element_by_id('cellPhoneNumber').send_keys('18100000000')
# time.sleep(3)
# dr.find_element_by_id('btnGetCode').click()
time.sleep(1)
dr.find_element_by_id('realName').send_keys('张三')
dr.find_element_by_id('credentialNo').send_keys('510265790128303')
dr.find_element_by_id('btnGetCode').click()
time.sleep(1)
dr.find_element_by_id('smsCode').send_keys('111111')
dr.find_element_by_id('btnCardPay').click()
time.sleep(5)
# dr.find_element_by_id('btnBack').click()
# time.sleep(10)
dr.quit()
