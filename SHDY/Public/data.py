#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/4/24 13:43
import time
from faker import Faker

class Data:

      def Data_merchants(self):
          '''
          商户号
          :return:
          '''
          merchantId = {
              'sit商户':'872290479115003',
              'uat商户':"872290451115001",
              'sit门户': '93600000004',
              'sit':'92900000057',
              'uat门户': '92900000006',
              'HH快速商户':'10110348111008f',
              'HH小微商户': '101290459460002',
              'HH标准商户': '114305858120000',
              'HH池商户':'872290045110204',
              'HH池商户0':'872290476920001'
          }
          return merchantId

      def Data_password(self):
          '''
          账号密码
          :return:
          '''
          password = {
              "uat":"1234qwer",
              "sit":"555418",
              "sit张卫":"688076",
              "uat门户":"60529785"
          }
          return password


      def Username(self):
          '''
          法人姓名
          :return:
          '''
          name = {
              "马敬宾":"17638605501",
              "曹超":"18721408232"
                  }
          return name

      def Idcard(self):
          '''
          身份证号
          :return:
          '''
          idcard = {
                  "马敬宾":"412702199002184510",
                  "曹超":"310109198610051510"
          }
          return idcard

      def card_number(self):
          '''
          银行卡号
          :return:
          '''
          card = {
              "曹超":"6222031001017548210",
              "马敬宾":"6217001180034143373"
          }
          return card

      def Other(self):
          '''
          openid:公众号
          platSource:平台标识
          :return:
          '''
          other = {
              "openid":"oqz6vt5gOlGEhKd_8ofEyNYbkAEY",
              "platSource":"2019091923490001"
          }
          return other


class Mock:
    """
    address 地址
    person 人物类：性别、姓名等
    barcode 条码类
    color 颜色类
    company 公司类：公司名、公司email、公司名前缀等
    credit_card 银行卡类：卡号、有效期、类型等
    currency 货币
    date_time 时间日期类：日期、年、月等
    file 文件类：文件名、文件类型、文件扩展名等
    internet 互联网类
    job 工作
    lorem 乱数假文
    misc 杂项类
    phone_number 手机号码类：手机号、运营商号段
    python python数据
    profile 人物描述信息：姓名、性别、地址、公司等
    ssn 社会安全码(身份证号码)
    user_agent 用户代理
    """
    mc = Faker('zh_CN')

    def get_name(self):
        """
        随机姓名
        :return:
        """
        return self.mc.name()

    def get_username(self):
        """
        随机用户名
        :return:
        """
        return self.mc.user_name()

    def get_phone(self):
        """
        随机手机号
        :return:
        """
        return self.mc.phone_number()

    def get_bankCar(self):
        """
        随机银行卡
        :return:
        """
        return self.mc.credit_card_number()

    def get_barcode(self):
        """
        获取随机条码码
        :return:
        """
        return self.mc.user_name()

    def get_email(self):
        """
        获取随机邮箱号
        :return:
        """
        return self.mc.free_email()

    def get_password(self):
        """
        获取随机密码
        :return:
        """
        return self.mc.password()

    def get_time(self):
          '''
          日期订单号
          :return:
          '''
          # date = time.strftime("%Y/%m/%d %H%M%S",
          #                       time.localtime(time.time()))
          date = time.strftime("%Y%m%d%H%M%S",
                                time.localtime(time.time()))
          return date

    def get_order(self):
        """
        流水号
        :return:
        """
        random_number = self.mc.random_int(min=000000000000000,max=999999999999999)
        return random_number

    def get_card(self):
        '''
        生成身份证号
        :return:
        '''
        return self.mc.ssn()

    def get_Company(self):
        '''
        公司名字
        :return:
        '''
        return self.mc.company()

    def get_card_number(self):
        '''
        信用卡号
        :return:
        '''
        return self.mc.credit_card_number()

    def get_address(self):
        '''
         地址
        :return:
        '''
        address = self.mc.province() +  self.mc.street_address()
        return address
