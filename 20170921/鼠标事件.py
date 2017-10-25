from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://testerhorde.com/")

driver.implicitly_wait(10)

driver.find_element_by_id("search-button").click()

driver.find_element_by_id("search-term").clear()

driver.find_element_by_id("search-term").send_keys("selenium")