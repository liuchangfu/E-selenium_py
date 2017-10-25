from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import csv,time

driver  =webdriver.Firefox()
driver.get("http://192.168.1.113:10086/wordpress/wp-login.php")

driver.find_element_by_id("user_login").clear()
driver.find_element_by_id("user_login").send_keys("liuchangfu")
driver.find_element_by_id("user_pass").clear()
driver.find_element_by_id("user_pass").send_keys("lcfwku1220")
driver.find_element_by_id("wp-submit").click()

# # driver.find_element_by_xpath("//ul[2]/li/div/ul/li[3]/a").click()
# driver.implicitly_wait(2)
#
# above = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/ul[2]/li/a/img")
# click_ele= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/ul[2]/li/div/ul/li[3]/a")
#
# ActionChains(driver).move_to_element(above).click(click_ele).perform()

btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul[2]/li/a/img')
driver.execute_script('$(arguments[0]).click()',btn)


# menu = driver.find_element_by_css_selector(".nav")
# hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")
# ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

# chain =ActionChains(driver)
# aaa=driver.find_element_by_xpath("//div[@id='hd']/div/div/div/ul/li[4]")
# b=aaa.find_element_by_css_selector("a")          ----------一直没有定位到图中a这个元素，而是一直定位
#                                                                       到a上一层--li，导致脚本一直跑不通过，后来加上这句就成功了
# chain.move_to_element(b).perform()
# driver.find_element_by_xpath("//div[@id='hd']/div/div/div/ul/li[4]/div/div/div[2]").click()