# -*- coding: utf-8 -*-
import time
from SHDY.Public import data,data_url,conf

url = data_url.Url().url()
date = data.Data()
uat = 'sit'

def refund(orderId):
    ch = data_url.Driver().driver()
    ch.get(url[uat])
    ch.implicitly_wait(10)
    ch.find_element_by_id('MercId').clear()
    ch.find_element_by_id('MercId').send_keys('872558279975000')
    # ch.find_element_by_id('MercId').send_keys(date.Data_merchants()[uat+'商户'])
    ch.find_element_by_id('MerchantCertPass').clear()
    ch.find_element_by_id('MerchantCertPass').send_keys('688076')
    #ch.find_element_by_id('MerchantCertPass').send_keys(date.Data_password()[uat])
    ch.find_element_by_xpath('//html/body/center/form/table/tbody/tr[4]/td/input').click()
    '''统一退款demo'''
    ch.find_element_by_xpath('//html/body/center/form/table/tbody/tr[36]/td/a').click()
    time.sleep(3)
    ch.find_element_by_id('orderId').clear()
    ch.find_element_by_id('orderId').send_keys(orderId)
    ch.find_element_by_xpath\
        ('/html/body/form/center/table/tbody/tr[10]/td[2]/input').clear()
    time.sleep(3)
    ch.find_element_by_id('Submit').click()
    time.sleep(3)
    ch.find_element_by_id('Submit').click()
    time.sleep(1)
    txt = ch.find_element_by_xpath('//html/body/pre').text
    i = conf.get_str(txt,'returnMessage=','&')
    if i == '交易成功':
        time.sleep(5)
        ch.quit()
    else:
        ch.quit()
        print(i)
    return

file_path = r'D:\PycharmProject\untitled\SHDY\Public\orderId.txt'
with open(file_path, encoding='gbk')as f:
        con = f.readlines()
        print(con.pop())
        for i in range(len(con)):
            if '=' in con[i]:
                orderId = con[i].split('=')[-1].replace(' ', '').strip()
                refund(orderId)

