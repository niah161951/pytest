#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/5/25 17:14
import time,os
from selenium.webdriver import ActionChains
from untitled.SHDY.Public import data_url, data,log,conf

dr =  data_url.Driver().driver()
#log = log.logs()
url = data_url.Url().url()
date = data.Data()
uat = 'uat'
value = 'C99230A88E280F82C0BEDFEAA9D86434'

#92900000006
#01603117
#482291
dr.get(url[uat+'门户'])
dr.add_cookie({"name": "JSESSIONID",
                       "value": value,
                       "path": "/mweb"})
dr.get(url[uat+'门户'])
dr.implicitly_wait(10)
dr.maximize_window()
dr.find_element_by_xpath\
    ('//*[@id="isLog"]/div/div[4]/a/input').click()
move = dr.find_element_by_xpath('//*[@id="merchants"]')
time.sleep(1)
ActionChains(dr).move_to_element(move).perform()
dr.find_element_by_xpath('//*[@id="merchants_sub"]/div[2]/li[1]/a').click()
dr.find_element_by_id('fileId').send_keys(r'E:\下载\TEMPLATE_BAT_PAY1.xlsx')
dr.find_element_by_id('submit_form').click()
time.sleep(10)
dr.find_element_by_id('payButton').click()
time.sleep(10)
dr.quit()