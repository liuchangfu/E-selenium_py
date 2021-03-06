from selenium import webdriver
import HTMLTestRunner
import unittest
import time

class Login(unittest.TestCase):
    def setUp(self):
        print("Test case begin!!!")
        self.br = webdriver.Chrome()
        self.br.get("http://192.168.1.113:10086/wordpress/wp-login.php")

    def test_login1(self):
        """正确的用户名和密码"""
        #初始化用户名和密码
        username = 'liuchangfu'
        password = 'lcfwku1220'
        #调用login登录方法
        self.login(username,password)
        #加入断言，是否已登录成功，登录成功的网址是否包含wp-admin
        self.assertTrue('wp-admin' in self.br.current_url)
        #先定位父节点，再定位子节点
        now_lin = self.br.find_element_by_css_selector("#wp-admin-bar-my-account > a:nth-child(1)")
        # 加入断言，登录成功后，username是否包含在now_lin
        self.assertTrue(username in now_lin.text)
        # 休眠3秒
        time.sleep(3)

    def test_login2(self):
        """正确的用户名和错误的密码"""
        # 初始化用户名和密码
        username = "liuchangfu"
        password = "123456"
        # 调用login登录方法
        self.login(username, password)
        assert_text = self.br.find_element_by_id("login_error").text
        self.assertEqual(assert_text,"错误：为用户名liuchangfu指定的密码不正确。 忘记密码？")
        time.sleep(3)

    def test_login3(self):
        """错误的用户名和正确的密码"""
        # 初始化用户名和密码
        username = "test001"
        password = "lcfwku1220"
        # 调用login登录方法
        self.login(username, password)
        assert_text = self.br.find_element_by_id("login_error").text
        self.assertEqual(assert_text,"错误：无效用户名。 忘记密码？")
        time.sleep(3)

    def test_login4(self):
        """错误的用户名和密码"""
        # 初始化用户名和密码
        username = "test001"
        password = "test001"
        # 调用login登录方法
        self.login(username,password)
        assert_text = self.br.find_element_by_id("login_error").text
        self.assertEqual(assert_text, "错误：无效用户名。 忘记密码？")
        time.sleep(3)

    def test_login5(self):
        """用户名不为空，密码为空"""
        # 初始化用户名和密码
        username = "liuchangfu"
        passwrod = ""
        # 调用login登录方法
        self.login(username,passwrod)
        assert_text = self.br.find_element_by_id("login_error").text
        self.assertEqual(assert_text, "错误：密码一栏为空。")
        time.sleep(3)

    def test_login6(self):
        """用户名为空，密码不为空"""
        # 初始化用户名和密码
        username = ""
        password= "123456"
        # 调用login登录方法
        self.login(username,password)
        assert_text = self.br.find_element_by_id("login_error").text
        self.assertEqual(assert_text, "错误：用户名一栏为空。")
        time.sleep(3)

    def test_login7(self):
        """用户名和密码都为空"""
        # 初始化用户名和密码
        username = ""
        password = ""
        # 调用login登录方法
        self.login(username, password)
        try:
            self.br.find_element_by_id("wp-submit").is_displayed()
            print("Test pass")
        except  Exception as e:
            print('Test fail', format(e))

    #登录写成login函数
    def login(self,username,password):
        self.br.find_element_by_id("user_login").clear()
        self.br.find_element_by_id("user_login").send_keys(username)
        self.br.find_element_by_id("user_pass").clear()
        self.br.find_element_by_id("user_pass").send_keys(password)
        self.br.find_element_by_id("wp-submit").click()

    def tearDown(self):
        print("Test case end!!!")
        self.br.quit()

if __name__=="__main__":
    # unittest.main()
    testunit = unittest.TestSuite()
    testunit.addTest(Login("test_login1"))
    testunit.addTest(Login("test_login2"))
    testunit.addTest(Login("test_login3"))
    testunit.addTest(Login("test_login4"))
    testunit.addTest(Login("test_login5"))
    testunit.addTest(Login("test_login6"))
    testunit.addTest(Login("test_login7"))
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    filename = "E:\\selenium_py\\Practice Case\\第一节\\"+now_time+"_result.html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="wordpress登录测试用例",description="用例执行情况：")
    runner.run(testunit)