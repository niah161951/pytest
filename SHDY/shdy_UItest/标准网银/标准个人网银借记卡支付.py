# -*- coding: utf-8 -*-
import time
from SHDY.Public import data_url, data,log,conf

url = data_url.Url().url()
mock = data.Mock()
data = data.Data()
ch = data_url.Driver().driver()

uat = "sit"
ch.implicitly_wait(5)
ch.get(url[uat])
ch.find_element_by_id('MercId').clear()
ch.find_element_by_id('MercId').send_keys(data.Data_merchants()[uat+'商户'])
ch.find_element_by_id('MerchantCertPass').clear()
ch.find_element_by_id('MerchantCertPass').send_keys(data.Data_password()[uat])
ch.find_element_by_xpath('//html/body/center/form/table/tbody/tr[4]/td/input').click()
'''标准支付接口'''
ch.find_element_by_xpath('//html/body/center/form/table/tbody/tr[45]/td/a').click()
time.sleep(1)
ch.find_element_by_xpath\
    ('/html/body/form/center/table/tbody/tr[6]/td[2]/input').clear()
ch.find_element_by_xpath\
    ('/html/body/form/center/table/tbody/tr[6]/td[2]/input').send_keys('1')

orderId = ch.find_element_by_xpath\
    ('/html/body/form/center/table/tbody/tr[4]/td[2]/input').get_attribute('value')
conf.Config().set_param(uat+'标准个人网银借记卡支付',orderId)

#提交
ch.find_element_by_xpath('//*[@id="Submit"]').click()
time.sleep(3)
ch.find_element_by_xpath('/html/body/jspfile/div[5]/div[2]/div/div[1]/ul/li[2]/a').click()
ch.find_element_by_xpath('//*[@id="personalPayment"]/li[2]/img').click()
ch.find_element_by_xpath('//*[@id="personalPayment"]/li[2]/div/a[1]').click()
#00  对应借记卡 01贷记卡 05企业网银
#个人网银
ch.switch_to_window(ch.window_handles[1])
time.sleep(2)
# ch.switch_to_frame(ch.find_element_by_id('form-242'))

ch.find_element_by_id('pyerAcctTp').send_keys(00)
ch.find_element_by_id('pyerAcctId').send_keys(mock.get_bankCar())
ch.find_element_by_id('pyerAcctNm').send_keys(mock.get_name())
ch.find_element_by_id('button-242').click()
time.sleep(30)
ch.quit()

