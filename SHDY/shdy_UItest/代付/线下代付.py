# -*- coding: utf-8 -*-
import time
from selenium.webdriver.support.select import Select
from untitled.SHDY.Public import data_url, data,log,conf

url = data_url.Url().url()
data = data.Data()
config = conf.Config()
uat = 'sit'

ch = data_url.Driver().driver()
ch.implicitly_wait(5)
ch.get(url[uat])
ch.find_element_by_id('MercId').clear()
ch.find_element_by_id('MercId').send_keys(data.Data_merchants()[uat+'商户'])
ch.find_element_by_id("MerchantCertPass").clear()
ch.find_element_by_id('MerchantCertPass').send_keys(data.Data_password()[uat])
#重置
ch.find_element_by_xpath('//html/body/center/form/table/tbody/tr[4]/td/input').click()
#点击提交  RePay-代付demo
ch.find_element_by_xpath('//html/body/center/form/table/tbody/tr[38]/td/a').click()
time.sleep(1)
select=Select(ch.find_element_by_xpath
              ('//*[@id="form1"]/center/table/tbody/tr[8]/td[2]/select'))
select.select_by_visible_text('线下代付')
ch.find_element_by_id('userName').send_keys('马敬宾')
ch.find_element_by_id('cardNo').send_keys(data.card_number()['马敬宾'])
ch.find_element_by_id('userNo').send_keys(data.Idcard()['马敬宾'])
selecs =Select(ch.find_element_by_xpath('/html/body/form/center/table/tbody/tr[10]/td[2]/select'))
selecs.select_by_visible_text('对私')
orderId=ch.find_element_by_id('orderId').get_attribute('value')
conf.Config().set_param(uat+'线下代付',orderId)
#提交
ch.find_element_by_id('Submit').click()
time.sleep(1)
ch.find_element_by_id('Submit').click()
time.sleep(30)
ch.quit()

