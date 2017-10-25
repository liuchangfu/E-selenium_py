from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get('https://www.baidu.com')

# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 窗口最小化为高度为800，宽度为600
driver.set_window_size(800,600)
time.sleep(2)