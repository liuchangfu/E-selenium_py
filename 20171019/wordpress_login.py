from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import csv

driver  =webdriver.Firefox()
driver.get("http://localhost:10086/wordpress/wp-login.php")

def login(self,username,password):
    driver.find_element_by_id("user_login").clear()
    driver.find_element_by_id("user_login").send_keys(username)
    print(username)
    driver.find_element_by_id("user_pass").clear()
    driver.find_element_by_id("user_pass").send_keys(password)
    print(password)
    driver.find_element_by_id("wp-submit").click()

def logout():
    above= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/ul[2]/li/a/span")
    ActionChains(driver).move_to_element(above).perform()
    driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/ul[2]/li/div/ul/li[3]/a").click()


with open("user.csv","r") as f:
    # reader = csv.DictReader(f)
    reader = csv.reader(f)
    for user in reader:
        # print(user['username'],user['email'])
        # username = user[0]
        # password = user[1]
        login(driver,user[0],user[1])
        driver.implicitly_wait(5)
        logout()