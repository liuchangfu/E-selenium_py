from selenium import webdriver
import HTMLTestRunner
import unittest
import time

class Login(unittest.TestCase):
    def setUp(self):
        print("Test case begin!!!")
        self.br = webdriver.Firefox()
        self.br.get("http://192.168.1.113:10086/wordpress/wp-login.php")

    def test_login1(self):
        """正确的用户各和密码"""
        username = 'liuchangfu'
        passwrod = 'lcfwku1220'
        self.br.find_element_by_id("user_login").send_keys(username)
        self.br.find_element_by_id("user_pass").send_keys(passwrod)
        self.br.find_element_by_id("wp-submit").click()
        #加入断言，是否已登录成功，登录成功的网址是否包含wp-admin
        self.assertTrue('wp-admin' in self.br.current_url)
        #先定位父节点，再定位子节点
        now_lin = self.br.find_element_by_css_selector("#wp-admin-bar-my-account > a:nth-child(1)")
        # 加入断言，登录成功后，username是否包含now_lin
        self.assertTrue(username in now_lin.text)
        # 重新返回到登录页面
        self.br.back()
        # 休眠3秒
        time.sleep(3)



    def tearDown(self):
        print("Test case end!!!")
        self.br.quit()

if __name__=="__main__":
    # unittest.main()
    testunit = unittest.TestSuite()
    testunit.addTest(Login("test_login1"))
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    filename = "E:\\selenium_py\\Practice Case\\"+now_time+"_result.html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="wordpress登录测试用例",description="用例执行情况：")
    runner.run(testunit)