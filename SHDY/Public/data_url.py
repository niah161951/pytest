# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/4/24 10:04
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver

class Driver:
    def dr(self):
        '''
        本地连接
        :return:
        '''
        dr = webdriver.Chrome()
        return dr

    def driver(self):
        '''
        远程连接
        :return:
        '''
        driver = webdriver.Remote(command_executor='http://192.168.18.51:4444/wd/hub',
                              desired_capabilities=DesiredCapabilities.CHROME)
        return driver

class  Url:
    '''
    url地址
    '''
    def url(self):
        url = {
            "sit":"http://192.168.20.149:8103/mercStandard/",
            'uat':"http://dev.chinaebi.cn:19080/mercStandard/index.jsp",
            "回调":"www.baidu.com",
            "拼接":"http://dev.chinaebi.com:5280/mrpos/dogwdirectpay_wxjsapi.jsp?",
            "二维码":"https://www.liantu.com/",
            "草料":"https://cli.im/",
            'sit门户':"http://192.168.20.149:8090/mweb/",
            'uat门户': "http://pay.uat.chinaebi.com:50080/mweb/",
            "标准版扫码加签": "http://192.168.31.161:28380/test_agent/testScan/getSign",
            "标准版扫码验签":"http://192.168.31.161:28380/transaction_agent/scan/trans",
            "uat线下运营控台":"http://pos.uat.sh.dy:50088/mrbui/module/login/jsp/login.jsp"
        }
        return url
