from  selenium import webdriver
import unittest
import time

class baidu_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url= 'http://www.baidu.com'

    def test_01(self):
        driver =self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertEqual(driver.title,"unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()

if __name__=="__mian__":
    unittest.main()