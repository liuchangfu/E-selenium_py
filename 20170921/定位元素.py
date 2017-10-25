from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get('https://www.baidu.com')

# 通过id定位到百度搜索输入框，并输入python关键字
driver.find_element_by_id('kw').send_keys('python')

# 通过name定位到百度搜索输入框，并输入python关键字
driver.find_element_by_name('wd').send_keys('python')

# 通过class定位到百度搜索输入框，并输入python关键字
driver.find_element_by_class_name('s_ipt').send_keys('python')

# 通过tat(标签)定位到百度搜索输入框，并输入python关键字
driver.find_element_by_tag_name('input').send_keys('python')

# 通过link(超链接)定位到hao123，并点击
driver.find_element_by_link_text('hao123').click()

# partial_link是一种模糊匹配方式，取链接文本一部分，并点击
driver.find_element_by_partial_link_text('ao123').click()

# 通过xpath定位百度搜索输入框，并输入python关键字
driver.find_element_by_xpath(".//*[@id='kw']").send_keys('python')

# 通过selector定位百度输入框
driver.find_elements_by_css_selector('#kw')