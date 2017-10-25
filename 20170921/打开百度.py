# 导入webdriver模块
from selenium import webdriver
# 导入时间模块
import time

# 初始化浏览器驱动
# driver  = webdriver.Ie()

# 初始Chrome化浏览器驱动
driver = webdriver.Chrome()

# 初始Firefox化浏览器驱动
# driver = webdriver.Firefox()

# 最大化浏览器窗口
driver.maximize_window()

# 打开百度
driver.get('http://www.baidu.com')

# 输入关键词
driver.find_element_by_id('kw').send_keys('selenium2')

# 点击百度一下按钮
driver.find_element_by_id('su').click()

# 休眠时间为3秒，也可以是小数，单位为秒
time.sleep(3)

# 等待3秒后，刷新页面
driver.refresh(3)

# 退出浏览器
driver.quit()

