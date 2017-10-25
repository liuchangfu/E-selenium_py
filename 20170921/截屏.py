from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get('https://www.baidu.com')
time.sleep(3)

# 截屏，并保存在E:\\selenium_py\\test目录中，文件名1,格式为.png
driver.get_screenshot_as_file('E:\\selenium_py\\test\\1.png')

# 退出浏览器
driver.quit()