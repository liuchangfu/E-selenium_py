import HTMLTestRunner
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
        """搜索unittest"""
        driver =self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertEqual(driver.title,"unittest_百度搜索")

    def test_02(self):
        """搜索selenium"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertEqual(driver.title, "selenium_百度搜索")

    def tearDown(self):
        self.driver.quit()

"""
 执行脚本时，不生成测试报告时，有以下两种方法解决：
1.把if __name__=="__main__"中的main改成程序文件名即可；
2.在run菜单中，选择[run]；
"""
# if __name__=="baidu_serach":
if __name__ == "__main__":
    # unittest.main()
    testunit = unittest.TestSuite()
    testunit.addTest(baidu_test("test_01"))
    testunit.addTest(baidu_test("test_02"))
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    #定义报告路径
    filename = 'E:\\selenium_py\\report\\'+now+'result.html'
    fp= open(filename,'wb')
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='百度搜索测试报告',description='用例执行情况：')
    runner.run(testunit)
    fp.close()