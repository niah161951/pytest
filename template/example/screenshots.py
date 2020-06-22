#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/5/19 14:16
from selenium import webdriver
import time
url = 'https://www.baidu.com'
driver = webdriver.Chrome()
driver.get(url)
try:
    driver.find_element_by_id('id').send_keys("你好")
except Exception as mc:
    print(u'异常原因:%s'%mc)
    now = time.strftime('%Y/%m/%d %H:%M:%S')
    print(now)
    t = driver.get_screenshot_as_file('%s.png'%now)
    print(u"截图结果：%s"%t)
    driver.quit()