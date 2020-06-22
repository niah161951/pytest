#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/6/2 11:00
import time
from selenium import webdriver
from SHDY.Public import data_url,data,Security_controls,conf
uat = 'uat'
name = data.Data
password = Security_controls.InputPasswordUtil()
url = data_url.Url().url()
driver = data_url.Driver().dr()
driver.get(url[uat+'线下运营控台'])
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id('oper_no').send_keys('T00156')
driver.find_element_by_id('_ocx_password_str').click()
password.input_password('1234qwer')
driver.find_element_by_id('sendmsg').click()
time.sleep(15)
driver.find_element_by_xpath('//*[@id="mylogin"]/div[3]/button').click()
driver.find_element_by_xpath('/html/body/section/div[1]/div[3]/ul/li[11]/a/i').click()
driver.find_element_by_xpath('/html/body/section/div[1]/div[3]/ul/li[12]').click()
driver.quit()