from selenium import webdriver
import HTMLTestRunner
import unittest
import time

dr = webdriver.Chrome()
dr.get("http://192.168.1.113:10086/wordpress/wp-login.php")

dr.find_element_by_id("user_login").send_keys("")
dr.find_element_by_id("user_pass").send_keys("")
dr.find_element_by_id("wp-submit").click()

try:
    dr.find_element_by_id("wp-submit").is_displayed()
    print("Test pass")
except  Exception as e:
    print('Test fail',format(e))
