from selenium import webdriver
import os
import time

br = webdriver.Firefox()
file_path ="file:///"+ os.path.abspath("frame.html")
print(file_path)
br.get(file_path)

#切换frame，根据frame的ID定位
br.switch_to.frame("if")

br.find_element_by_id("kw").send_keys("selenium")
br.find_element_by_id("su").click()
time.sleep(3)