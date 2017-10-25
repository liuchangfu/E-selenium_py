from selenium import webdriver

driver =webdriver.Firefox()
driver.get("http://www.youdao.com")

cookie=driver.get_cookies()
print(cookie)