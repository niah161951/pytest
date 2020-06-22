#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/5/7 15:35
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
#引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://m.mail.10086.cn")
#将浏览器最大化
driver.maximizewindow()
#参数数字为像素点
print ("设置浏览器宽480、高800显示")
driver.set_window_size(480, 800)
first_url= ('http://www.baidu.com')
print ("now access %s" %(first_url))
driver.get(first_url)
#返回（后退）到百度首页
print ("back to %s "%(first_url))
driver.back()
#前进到新闻页
second_url='http://news.baidu.com'
print ("forward to %s"%(second_url))
driver.forward()
#通过 submit() 来提交操
#driver.findelementbyid("dlansubmit").submit
#返回百度输入狂的宽高
size=driver.find_element_by_id("kw").size
print (size)
#返回元素的结果是否可见，返回结果为 True 或 False
result=driver.find_element_by_id("kw").is_displayed()
print (result)

#定位到要右击的元素
right =driver.find_element_by_xpath("xx")
#对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(right).perform()
#定位到要双击的元素
double =driver.find_element_by_xpath("xxx")
#对定位到的元素执行鼠标双击操作
ActionChains(driver).double_click(double).perform()

#定位元素的原位置
element = driver.find_element_by_name("xxx")
#定位元素要移动到的目标位置
target = driver.find_element_by_name("xxx")
#执行元素的移动操作
ActionChains(driver).drag_and_drop(element, target).perform()
#定位到鼠标移动到上面的元素
above = driver.find_element_by_xpath("xxx")
#对定位到的元素执行鼠标移动到上面的操作
ActionChains(driver).move_to_element(above).perform()
#定位到鼠标按下左键的元素
left=driver.find_element_by_xpath("xxx")
#对定位到的元素执行鼠标左键按下的操作
ActionChains(driver).click_and_hold(left).perform()

driver.get("http://www.baidu.com")
#输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")
sleep(3)
#删除多输入的一个 m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
sleep(3)
#输入空格键+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")
sleep(3)
#ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
#ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
#输入框重新输入内容，搜索
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
#通过回车键盘来代替点击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)
# send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
# send_keys(Keys.SPACE) 空格键(Space)
# send_keys(Keys.TAB) 制表键(Tab)
# send_keys(Keys.ESCAPE) 回退键（Esc）
# send_keys(Keys.ENTER) 回车键（Enter）
# send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
# send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
# send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
# send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
#获得前面 title，打印
title = driver.title
print (title)
#拿当前 URL 与预期 URL 做比较
if title == u"快播私有云":
   print ("title ok!")
else:
   print ("title on!")
#获得前面 URL，打印
now_url = driver.current_url
print (now_url)
#拿当前 URL 与预期 URL 做比较
if now_url == "http://webcloud.kuaibo.com/":
    print ("url ok!")
else:
    print ("url on!")
#获得登录成功的用户，打印
now_user=driver.find_element_by_xpath("//div[@id='Nav']/ul/li[4]/a[1]/span").text
print (now_user)
#添加智能等待
driver.implicitly_wait(30)
sleep(0.5)
# 选择页面上所有的 tag name 为 input 的元素
inputs = driver.find_elements_by_tag_name('input')

#然后从中过滤出 tpye 为 checkbox 的元素，单击勾选
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
      input.click()
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
#隐藏提示
opent=Options()
opent.add_argument('--disable-infobars')
#添加缓存文件
opent.add_argument('-user-data-dir=C:\\Users\\lenovo\\AppData\\Local\\Google\\Chrome\\User Data')

chomd=webdriver.Chrome()
chomd.set_window_size(400,500)#设置窗口大小
#将页面滚动条拖到底部
js="var q=document.documentElement.scrollTop=10000"
chomd.execute_script(js)
time.sleep(3)
#将滚动条移动到页面的顶部
js_="var q=document.documentElement.scrollTop=0"
chomd.execute_script(js_)
time.sleep(3)
chomd.implicitly_wait(5)#找不到元素全局等待
chomd.find_element_by_xpath("").click()#xpath
chomd.find_element_by_id('').click()#id
chomd.find_elements_by_css_selector().click()#css
#下拉框
select=Select(chomd.find_elements_by_xpath(""))
select.select_by_visible_text("")#文本
select.deselect_by_index()#下标
select.select_by_value("")#value
#告警窗
chomd.switch_to_alert().accept()#点击确认
chomd.find_to.alert.accept()#新式点击
#窗口切换
handle=chomd.window_handles#获取句柄
chomd.switch_to.window(handle[1])#新增页面
# 截图
chomd.maximize_window()

current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
time.sleep(1)
chomd.get_screenshot_as_file("E:\\图片\\"+current_time+'微信扫码'+'.png')
chomd.get_screenshot_as_file("D:\\baidu_img.png")
#嵌套
chomd.switch_to.frame(chomd.find_element_by_id(""))
chomd.find_element_by_id("").send_keys("")#输入值
chomd.switch_to.parent_frame()#退出
chomd.find_element_by_id('userid').send_keys('13467890001')
chomd.find_element_by_id('login_pasw').send_keys('123456')
chomd.find_element_by_id('submit').click()
chomd.close()#关闭当前
chomd.quit()#关闭所有

dr = webdriver.Chrome()

url = 'https://www.w3school.com.cn/tiy/t.asp?f=html_basic'
#print('now access %s'%(url))
dr.get(url)
#访问新闻页面
#now_url = 'http://fanyi.youdao.com/'
#print('now access %s'%(now_url))
#driver.get(now_url)
#返回到原页面
#print('bzck to %s'%(url))
#driver.back()
#前进到新闻页
#print('forward to %s'%(now_url))
#driver.forward()

#driver.set_window_size(400,400)#控制浏览器页面大小
size = dr.find_element_by_xpath('//*[@id="textareawrapper"]/div').size
print(size)
#定位到要右击的元素

sleep(10)
dr.refresh()#刷新当前页面

dr.implicitly_wait(5)#隐形等待
#定位到要右击的元素
right = dr.find_element_by_xpath('/html/body/div[1]/div/ul/li/a/span')
#对定位到的元素执行鼠标右键操作
ActionChains(dr).context_click(right).perform()
#定位到要悬停的元素
above = dr.find_element_by_xpath('/html/body/div[1]/div/ul/li/ul/li[1]')
#对定位到的元素执行悬停操作
ActionChains(dr).move_to_element(above).perform()
#鼠标双击操作
double_click = dr.find_element_by_xpath('')
#双击
ActionChains(dr).double_click(double_click).perform()
#定位元素的原位置
element = dr.find_element_by_id("xx")
#定位元素要移动到的目标位置
target = dr.find_element_by_id("xx")
#执行元素的拖放操作
ActionChains(dr).drag_and_drop(element,target).perform()
#浏览器多窗口处理
js = 'window.open("http://192.168.31.161:28380/test_agent/");' #新窗口
dr.execute_script(js)
#获得当前窗口
nowhandle=dr.current_window_handle
#获得所有窗口
allhandles=dr.window_handles
#回到原先的窗口
dr.switch_to_window(nowhandle)
#关闭线程
headers = {
    'Connection': 'close',
}
dr.quit()#退出


