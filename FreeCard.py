# -*- coding: UTF-8 -*-
__author__ = 'Administrator'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def login(num,phonelist):#发放次数num,用户phone
    try:
        #time1 = time.time()
        browser = webdriver.Firefox()
        browser.get("http://operation.qtxiaoxin.com/")
        user = browser.find_element_by_css_selector("#username")
        user.send_keys("admin")
        pwd = browser.find_element_by_id("password")
        pwd.send_keys("omsqthd")
        browser.find_element_by_xpath(".//*[@id='loginForm']/div[3]/button").click()
        browser.find_element_by_xpath("html/body/div/div/div[3]/div/ul/li[2]/ul/li[3]/a").click()#进入指定用户发放
        print u'登录并进入指定用户发放成功'
        for phone in phonelist:
            print '开始发放班费卡：发放号码：%s,发放张数：%d'%phone,num
            i=0
            money = 100 #发放金额
            for i in range(0,num):
                browser.find_element_by_xpath(".//*[@id='sendSingle']").click()#单用户发放
                time.sleep(1)
                user = browser.find_elements_by_xpath(".//*[@id='cardaccount']")#发放用户
                for j in user:
                    j.clear()
                    j.send_keys(phone)
                money = money + 0.01              #金额自增0.01用于标识
                browser.find_element_by_xpath(".//*[@id='money']").send_keys(money)#金额
                browser.find_element_by_xpath(".//*[@id='activityname']").send_keys(u"自动发放")#活动名称
                browser.find_element_by_xpath(".//*[@id='dayend']").send_keys(1)#有效期
                browser.find_element_by_xpath(".//*[@id='remark']").send_keys(u"自动化发放")#备注
                browser.find_element_by_xpath(".//*[@id='configSubmit']").click() #提交
                browser.implicitly_wait(30)
                print '发放第%d张完成'%(i+1)
        #time2 = time.time()-time1
        #print time2
        print'班费卡已全部发放完成，退出浏览器！'
        browser.quit()
    except ValueError,e:
        print e
if __name__ == '__main__':
    time1 = time.time()
    #list = [12300001118,12300001119,12300001120,12300001128,13686831249,12300001165]
    phonelist = [18129830060]
    num = 50
    login(num,phonelist)
    time2 = time.time()-time1
    print time2
