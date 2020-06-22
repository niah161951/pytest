#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/5/21 14:37
import time,re
from selenium.webdriver.support.select import Select
from SHDY.Public import data_url, data,conf
date = data.Data()
url = data_url.Url().url()
config = conf.Config()
uat = 'sit'

for i in range(3):
    ch = data_url.Driver().driver()
    ch.get(url[uat])
    ch.implicitly_wait(5)
    ch.find_element_by_id('MercId').clear()
    ch.find_element_by_id('MercId').send_keys(date.Data_merchants()[uat+'商户'])
    ch.find_element_by_id('MerchantCertPass').clear()
    ch.find_element_by_id('MerchantCertPass').send_keys(date.Data_password()[uat+'张卫'])

    ch.find_element_by_xpath('//html/body/center/form/table/tbody/tr[4]/td/input').click()
    #交易
    ch.find_element_by_xpath('//html/body/center/form/table/tbody/tr[11]/td/a').click()
    time.sleep(1)
    select =Select(ch.find_element_by_xpath
                  ('/html/body/form/center/table/tbody/tr[2]/td[2]/select'))
    if i == 0:
        select.select_by_visible_text('微信公众号')
        ch.find_element_by_xpath\
            ('//html/body/form/center/table/tbody/tr[4]/td[2]/input')\
            .send_keys(date.Other()['openid'])
        orderId=ch.find_element_by_xpath\
            ('/html/body/form/center/table/tbody/tr[3]/td[2]/input')\
            .get_attribute('value')
        config.set_param(uat+"纯聚合支付微信公众号支付", orderId)
        ch.find_element_by_xpath('//*[@id="Submit"]').click()
        a=ch.find_element_by_xpath('//html/body/pre').text
        time.sleep(1)
        wcPayData = conf.get_str(a,'{"','"}')
        c=re.compile('":"')
        d=c.sub('=',wcPayData)
        e=re.compile('","')
        f=e.sub('&',d)
        time.sleep(5)
        ch.quit()
        b=url['拼接']
        c=b+f
        time.sleep(1)
        dr = data_url.Driver().driver()
        dr.maximize_window()
        dr.get(url['草料'])
        dr.find_element_by_id('text-content').send_keys(c)
        dr.find_element_by_id('click-create').click()
        time.sleep(20)
        dr.quit()

    elif i == 1:
        select.select_by_visible_text('微信扫码')
        ch.find_element_by_xpath \
            ('//html/body/form/center/table/tbody/tr[4]/td[2]/input').send_keys(date.Other()['openid'])
        orderId = ch.find_element_by_xpath \
            ('/html/body/form/center/table/tbody/tr[3]/td[2]/input').get_attribute('value')
        conf.Config().set_param(uat + "微信扫码", orderId)
        ch.find_element_by_id('Submit').click()
        payInfo = ch.find_element_by_xpath('//html/body/pre').text
        payInfo = conf.get_str(payInfo, "payInfo=", "&")
        time.sleep(1)
        handle = ch.window_handles
        ch.switch_to.window(handle[0])
        ch.get(url['草料'])
        ch.maximize_window()
        ch.find_element_by_id('text-content').send_keys(payInfo)
        ch.find_element_by_id('click-create').click()
        time.sleep(20)
        ch.quit()
    else:
        select.select_by_visible_text('支付宝扫码')
        orderId = ch.find_element_by_xpath \
            ('/html/body/form/center/table/tbody/tr[3]/td[2]/input').get_attribute('value')
        conf.Config().set_param(uat + "标准支付宝扫码", orderId)
        # 提交
        ch.find_element_by_id('Submit').click()

        payInfo = ch.find_element_by_xpath('//html/body/pre').text
        time.sleep(1)

        payInfo = conf.get_str(payInfo, "payInfo=", "&")
        handle = ch.window_handles
        ch.switch_to.window(handle[0])
        ch.get(url['草料'])
        ch.maximize_window()
        ch.find_element_by_id('text-content').send_keys(payInfo)
        ch.find_element_by_id('click-create').click()
        time.sleep(20)
        ch.quit()






