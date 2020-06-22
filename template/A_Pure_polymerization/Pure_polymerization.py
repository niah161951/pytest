#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/4/27 15:26
import time,re,unittest,warnings
from SHDY.Public import data, data_url
from The_first_frame.conf.methods import get_str
from tem.A_Pure_polymerization.test_script import Test_Longin, driver
from SHDY.Public.MysqlDB import *
url = data_url.Url().url()
data = data.Data()
#insert = Config()
insert = MysqlDB()
test = Test_Longin()
date = time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(time.time()))

class login(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_Submit(self):
        Methods = ["微信公众号", "微信扫码", "支付宝扫码"]
        for Method in Methods:
            print(Method)

        #name = str(input(("请输入支付方式：%s ")%Method))
        name = str(input("请输入支付方式："))
        test.drop_down_box(name)

        if name == "微信公众号":
            driver.find_element_by_xpath \
                ('//html/body/form/center/table/tbody/tr[4]/td[2]/input') \
                .send_keys(data.Other()["openid"])
            orderId = driver.find_element_by_xpath\
                ('/html/body/form/center/table/tbody/tr[3]/td[2]/input')\
                .get_attribute('value')
            insert.insert_db(orderId,"SIT纯聚合支付微信公众号支付",date)
            #insert.set_param("SIT纯聚合支付微信公众号支付", orderId)
            '''提交'''
            driver.find_element_by_id('Submit').click()
            message =driver.find_element_by_xpath('//html/body/pre').text
            wcPayData =  get_str(message,"{","}")
            a = re.compile('":"')
            b = a.sub('=', wcPayData)
            c = re.compile('","')
            wcPayData = c.sub('&', b)
            time.sleep(5)
            driver.quit()
            b = url["公众号拼接地址"]
            c = b + wcPayData
            time.sleep(1)
            driver.get(url["二维码地址"])
            driver.find_element_by_xpath('//*[@id="text_text"]').send_keys(c)
            time.sleep(10)
            driver.quit()

        elif name == "微信扫码":
            driver.find_element_by_xpath \
                ('//html/body/form/center/table/tbody/tr[4]/td[2]/input')\
                .send_keys(data.Other()["openid"])
            orderId = driver.find_element_by_xpath\
                ('//html/body/form/center/table/tbody/tr[3]/td[2]/input')\
                .get_attribute('value')
            insert.set_param("SIT纯聚合支付微信扫码支付", orderId)
            '''提交'''
            driver.find_element_by_id('Submit').click()
            payInfo = driver.find_element_by_xpath('//html/body/pre').text
            payInfo = get_str(payInfo, "payInfo=", "&")
            handle = driver.window_handles
            driver.switch_to.window(handle[0])

            driver.get(url["二维码地址"])
            driver.find_element_by_id('text_text').send_keys(payInfo)
            time.sleep(15)
            driver.quit()

        elif name == "支付宝扫码":
            orderId = driver.find_element_by_xpath\
                ('//html/body/form/center/table/tbody/tr[3]/td[2]/input')\
                .get_attribute('value')
            insert.set_param("SIT纯聚合支付支付宝支付", orderId)
            '''提交'''
            driver.find_element_by_id('Submit').click()
            payInfo = driver.find_element_by_xpath('//html/body/pre').text
            time.sleep(1)

            payInfo = get_str(payInfo, "payInfo=", "&")
            handle = driver.window_handles
            driver.switch_to.window(handle[0])
            driver.get(url["二维码地址"])
            driver.find_element_by_id('text_text').send_keys(payInfo)
            time.sleep(15)
            driver.quit()

        else:
            print("支付选择：%s失败" % name)

if __name__ == "__main__":
    unittest.main()
