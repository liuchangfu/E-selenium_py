from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")

driver.implicitly_wait(10)

mosue = driver.find_element_by_link_text("设置")

ActionChains(driver).move_to_element(mosue).perform()