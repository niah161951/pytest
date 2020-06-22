#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/5/20 18:22
# -*- coding: utf-8 -*-
import time
from SHDY.Public import data_url, data,log,conf

log = log.logs()
url = data_url.Url().url()
date = data.Data()
usrNo = data.Mock().get_order()
uat = 'sit'

for  i in range(2):
    ch = data_url.Driver().driver()
    ch.implicitly_wait(10)
    ch.maximize_window()
    ch.get(url[uat])
    ch.find_element_by_id('MercId').clear()
    ch.find_element_by_id('MercId').send_keys(date.Data_merchants()[uat+'商户'])
    ch.find_element_by_id('MerchantCertPass').clear()
    ch.find_element_by_id('MerchantCertPass').send_keys(date.Data_password()[uat])
    ch.find_element_by_xpath('//html/body/center/form/table/tbody/tr[4]/td/input').click()

    #点击 快捷支付
    ch.find_element_by_xpath('//html/body/center/form/table/tbody/tr[34]/td/a').click()
    ch.find_element_by_xpath('//html/body/form/center/table/tbody/tr[4]/td[2]/input').clear()
    ch.find_element_by_xpath('//html/body/form/center/table/tbody/tr[4]/td[2]/input')\
        .send_keys(date.Other()['platSource'])#平台标识platSource
    ch.find_element_by_xpath('//html/body/form/center/table/tbody/tr[5]/td[2]/input').clear()
    ch.find_element_by_xpath('//html/body/form/center/table/tbody/tr[5]/td[2]/input')\
        .send_keys(usrNo)
    ch.find_element_by_xpath('//html/body/form/center/table/tbody/tr[7]/td[2]/input').clear()
    ch.find_element_by_xpath('//html/body/form/center/table/tbody/tr[7]/td[2]/input')\
        .send_keys('1')
    if i == 0:
        orderId=ch.find_element_by_xpath\
            ('/html/body/form/center/table/tbody/tr[3]/td[2]/input')\
              .get_attribute('value')
        conf.Config().set_param(uat+"标准借记卡快捷支付-建行",orderId)
        log.info(uat+"标准借记卡快捷支付:\n%s"%orderId)
        ch.find_element_by_id('Submit').click()  # 提交
        time.sleep(5)
        ch.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div/div[2]/div/input') \
            .send_keys(date.card_number()['马敬宾'])
        ch.find_element_by_xpath('//*[@id="app"]/div[2]/div[6]/button').click()
        time.sleep(3)
        ch.find_element_by_xpath('//div[@id="app"]/div[2]/div[2]/div[2]/div[2]/div/input') \
            .send_keys('马敬宾')
        ch.find_element_by_xpath('//div[@id="app"]/div[2]/div[2]/div[3]/div[2]/div/input') \
            .send_keys(date.Idcard()['马敬宾'])
        ch.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[4]/div[2]/div/input') \
            .send_keys(date.Username()['马敬宾'])
        time.sleep(1)
        ch.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div/div/button').click()
        time.sleep(1)
        ch.find_element_by_xpath\
            ('/html/body/div[1]/div[2]/div[3]/div/div[2]/div/input').send_keys('111111')
        ch.find_element_by_xpath\
            ('//div[@id="app"]/div[2]/div[4]/div[1]/div/div/div').click()
        ch.find_element_by_xpath('/html/body/div[1]/div[2]/div[5]/button[1]').click()
        time.sleep(8)
        ch.quit()

    else:
        orderId = ch.find_element_by_xpath \
            ('/html/body/form/center/table/tbody/tr[3]/td[2]/input').get_attribute('value')
        conf.Config().set_param(uat + 'H5标准借记卡工行', orderId)
        ch.find_element_by_id('Submit').click()
        #解绑银行卡
        ch.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div/div[2]').click()
        ch.find_element_by_xpath\
            ('/html/body/div[1]/div[2]/div[7]/div/div[1]/div[1]/div[3]/div').click()
        ch.find_element_by_xpath('/html/body/div[1]/div[2]/div[7]/div/div[2]/div').click()
        time.sleep(1)
        ch.find_element_by_xpath('/html/body/div[3]/div[3]/button[2]').click()
        # ch.refresh()
        time.sleep(2)
        ch.find_element_by_xpath \
            ('//*[@id="app"]/div[2]/div[4]/div/div[2]/div/input') \
            .send_keys(date.card_number()['曹超'])  # 银行卡
        ch.find_element_by_xpath \
            ('//*[@id="app"]/div[2]/div[6]/button').click()
        time.sleep(3)
        ch.find_element_by_xpath \
            ('//div[@id="app"]/div[2]/div[2]/div[2]/div[2]/div/input').send_keys('曹超')
        ch.find_element_by_xpath \
            ('//div[@id="app"]/div[2]/div[2]/div[3]/div[2]/div/input').send_keys(date.Idcard()['曹超'])
        ch.find_element_by_xpath \
            ('//*[@id="app"]/div[2]/div[2]/div[4]/div[2]/div/input').send_keys(date.Username()['曹超'])

        ch.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div/div/button').click()

        ch.find_element_by_xpath \
            ('/html/body/div[1]/div[2]/div[3]/div/div[2]/div/input').send_keys('111111')
        time.sleep(1)
        ch.find_element_by_xpath \
            ('//div[@id="app"]/div[2]/div[4]/div[1]/div/div/div').click()
        ch.find_element_by_xpath('/html/body/div[1]/div[2]/div[5]/button[1]').click()
        time.sleep(10)
        ch.quit()









