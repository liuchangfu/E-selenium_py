from  selenium import webdriver
driver = webdriver.Firefox()

driver.get("https://www.baidu.com")

# 获得当前窗口的句柄
h=driver.current_window_handle
print(h)