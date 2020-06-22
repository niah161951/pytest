# _*_ coding: utf-8 _*_
# 作者    : 一蓑烟雨任平生
# 创建时间 : 2019/12/25 15:45
# 创建文件 : PyCharm
from appium import webdriver
import time
desired_caps = {
                'appActivity': 'com.dyagent.MainActivity',          #Activity名字  dumpsys window windows | grep -i  current
                'appPackage': 'com.dyagent',        #应用包名
                'autoGrantPermissions': True,
                'autoLaunch': False,
                'automationName': 'UiAutomator2',
                'deviceName': 'CSX0218323000231',               #设备
                'noReset': True,
                'platformName': 'Android',
                'platformVersion': '9.0',
                'automationName' : 'Appium',    #自动化引擎
                'resetKeyboard':     True,      #是使用unicode编码方式发送字符串
                'unicodeKeyboard':   True,      #将键盘隐藏起来
                'autoAcceptAlerts':  True        #默认选择接受弹窗的条款，有些app启动的时候，会有一些权限的弹窗

}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)