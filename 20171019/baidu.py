#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
#打开百度首页
driver.get("https://www.baidu.com")
#使用鼠标悬停定位设置
set=driver.find_element_by_xpath("//*[@id='u1']/a[8]")
time.sleep(2)
#执行鼠标操作定位到"设置"
ActionChains(driver).move_to_element(set).perform()
time.sleep(2)
#点击"搜索设置"
driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()
time.sleep(2)