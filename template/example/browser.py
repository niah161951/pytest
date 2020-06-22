#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/5/19 15:31

from selenium import webdriver
def browser(browser):
    '''
    open browser 'firefox','chrome','ie'
    :return:
    '''
    try:
        if browser == 'firefox':
            driver = webdriver.Firefox()
            return driver
        elif browser == 'chrome':
            driver = webdriver.Chrome()
            return driver
        else:
            driver = webdriver.Ie()
            return driver
    except Exception as msg:
        print(u'打开结果：%s'%msg)
if __name__=="__main__":
    driver_chrome = browser('chrome')
    driver_chrome.get('https://www.baidu.com')
    driver_chrome.quit()
    print('open browser:%s'%driver_chrome.name)
