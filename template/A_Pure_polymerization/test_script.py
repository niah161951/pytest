#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/4/24 21:50
from time import sleep
from selenium.webdriver.support.select import Select
from SHDY.Public import data, data_url

driver = data_url.Driver().driver()
url = data_url.Url().url()
data = data.Data()

class Test_Longin():
    '''商户重置'''
    def case_longin(self):
        driver.get(url["sit环境地址"])
        driver.implicitly_wait(5)
        driver.find_element_by_id('MercId').clear()
        driver.find_element_by_id('MercId')\
            .send_keys(data.Data_merchants()["sit商户"])
        driver.find_element_by_id('MerchantCertPass').clear()
        driver.find_element_by_id('MerchantCertPass')\
            .send_keys(data.Data_password()["sit商户"])
        driver.find_element_by_xpath\
            ('//html/body/center/form/table/tbody/tr[4]/td/input').click()
        sleep(1)

    '''交易方式 （纯聚合支付）'''
    def Trade_portal(self,digital):
        self.case_longin()
        driver.find_element_by_xpath\
            ('//html/body/center/form/table/tbody/tr[{}]/td/a'
                                     .format(digital)).click()
        sleep(1)
    '''支付方式(微信公众号 微信扫码 支付宝扫码)'''
    def drop_down_box(self,name):
        self.Trade_portal(11)
        slect = Select(driver.find_element_by_xpath
                       ('/html/body/form/center/table/tbody/tr[2]/td[2]/select'))
        slect.select_by_visible_text(name)
        sleep(2)


# if  __name__=="__main__":
#     quer = Test_Longin()
