import time
import unittest
import HTMLTestRunner
from untitled.SHDY.Public import data_url, data
from untitled.SHDY.Public.log import logs

log = logs()
url = data_url.Url().url()
date = data.Data()
usrNo = data.Mock().get_order()
uat = 'sit'

class   KuaiJie(unittest.TestCase):

     def setUp(self):
         self.driver = data_url.Driver().driver()
         self.driver.implicitly_wait(10)
         self.base_url = url[uat]
         self.verificationErrors = []
         self.accept_next_alert = True

     def test_kuaijie(self):
         driver = self.driver
         driver.get(self.base_url)
         driver.find_element_by_id('MercId').clear()
         driver.find_element_by_id('MercId').send_keys(date.Data_merchants()[uat + '商户'])
         log.info(uat + '环境商户号：%s' % (date.Data_merchants()[uat + '商户']))
         driver.find_element_by_id('MerchantCertPass').clear()
         driver.find_element_by_id('MerchantCertPass').send_keys(date.Data_password()[uat])
         log.info(uat+'环境密码：%s'%(date.Data_password()[uat]))
         driver.find_element_by_xpath\
             ('//html/body/center/form/table/tbody/tr[4]/td/input').click()

     def tearDown(self):
         self.driver.quit()
         self.assertEqual([],self.verificationErrors)

if __name__=="__main__":
    tests = unittest.TestSuite()
    tests.addTest(KuaiJie("test_kuaijie"))
    timefree = time.strftime("%Y-%m-%d-%H-%M",time.localtime(time.time()))
    fp = open('%s.html'%timefree,'wb')
    run = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'借记卡支付',
        description=u'用例执行情况：'
    )
    run.run(tests)
