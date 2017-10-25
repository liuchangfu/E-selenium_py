from selenium import webdriver
import time

driver =webdriver.Firefox()

driver.get("http://www.baidu.com")
driver.set_window_size(800,600)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(2)

#通过JS脚本设置浏览器窗口的滚动位置
js = "window.scrollTo(100,450)"
driver.execute_script(js)
time.sleep(3)
