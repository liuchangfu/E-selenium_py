from selenium import webdriver
import  time

driver = webdriver.Firefox()

driver.get('https://www.baidu.com')
time.sleep(1)

driver.get('http://news.baidu.com')
time.sleep(1)

# 反回到上一页
driver.back()
time.sleep(3)

# 切换到下一页
driver.forward()