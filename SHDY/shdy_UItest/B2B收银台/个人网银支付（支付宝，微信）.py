# -*- coding: utf-8 -*-
import time,unittest
from SHDY.Public import data_url, data,log,conf

url = data_url.Url().url()
data = data.Data()
config = conf.Config()
uat = 'sit'


for  i in range(3):
    dr = data_url.Driver().driver()
    dr.get(url[uat])
    dr.implicitly_wait(5)
    dr.find_element_by_id('MercId').clear()
    dr.find_element_by_id('MercId').send_keys(data.Data_merchants()[uat+'商户'])
    dr.find_element_by_id('MerchantCertPass').clear()
    dr.find_element_by_id('MerchantCertPass').send_keys(data.Data_password()[uat])
    dr.find_element_by_xpath('//html/body/center/form/table/tbody/tr[4]/td/input').click()
    #点击  商户btb收款
    dr.find_element_by_xpath('//html/body/center/form/table/tbody/tr[24]/td/a').click()
    time.sleep(1)
    dr.find_element_by_id('rcvMerchantId')\
        .send_keys(data.Data_merchants()[uat+'商户'])
    dr.find_element_by_id('totalAmount').clear()
    dr.find_element_by_id('totalAmount').send_keys('1')
    dr.find_element_by_id('payAmount').clear()
    dr.find_element_by_id('payAmount').send_keys('1')
    dr.find_element_by_id('orderAmt').clear()
    dr.find_element_by_id('orderAmt').send_keys('1')
    dr.find_element_by_id('payAmt').clear()
    dr.find_element_by_id('payAmt').send_keys('1')
    dr.find_element_by_id('recEnterpriseId').clear()
    dr.find_element_by_id('recEnterpriseId')\
        .send_keys(data.Data_merchants()[uat+'商户'])
    dr.find_element_by_id('payMerchantId')\
        .send_keys(data.Data_merchants()[uat+'商户'])
    if i == 0:
        orderId=dr.find_element_by_id('orderId').get_attribute('value')
        config.set_param(uat+"B2B个人网银支付",orderId)
    elif i == 1:
        orderId=dr.find_element_by_id('orderId').get_attribute('value')
        config.set_param(uat+"B2B微信扫码支付",orderId)
    else:
        orderId=dr.find_element_by_id('orderId').get_attribute('value')
        config.set_param(uat+"B2B支付宝扫码支付",orderId)

    dr.find_element_by_xpath('/html/body/form/center/table/tbody[2]/tr[11]/td[2]/input')\
        .send_keys(url['回调'])
    dr.find_element_by_xpath('/html/body/form/center/table/tbody[2]/tr[12]/td[2]/input')\
        .send_keys(url['回调'])
    dr.find_element_by_xpath('//*[@id="form1"]/center/table/tbody[3]/tr/td[2]/input[2]').click()

    time.sleep(3)
    #提交
    dr.find_element_by_id('Submit').click()
    #个人网银
    dr.find_element_by_xpath\
        ('/html/body/jspfile/div[2]/div[2]/div/div/div/form/ul/li[6]/div/div[3]/ul/li[2]/a').click()
    '''网银支付0，微信1，支付宝'''
    if i == 0:
        dr.find_element_by_xpath('//*[@id="bk_show_tit1"]/div/ul/li/img').click()
        dr.find_element_by_id('ensure_psw').click()
        time.sleep(15)
        dr.quit()
    elif i ==1:
        dr.find_element_by_xpath('//*[@id="scanPayWX"]').click()
        dr.find_element_by_id('ensure_psw').click()
        time.sleep(15)
        dr.quit()
    else:
        dr.find_element_by_xpath('//*[@id="scanPayAli"]').click()
        dr.find_element_by_id('ensure_psw').click()
        time.sleep(15)
        dr.quit()











