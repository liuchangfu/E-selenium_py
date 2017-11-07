from selenium import webdriver
import HTMLTestRunner
import unittest
import time

class Login(unittest.TestCase):

    def setUp(self):
        print("Test case begin!!!")
        self.br = webdriver.Firefox()
        self.br.get("http://192.168.1.113:10086/wordpress/wp-login.php")

    def login(self,username,password):
        self.br.find_element_by_id("user_login").clear()
        self.br.find_element_by_id("user_login").send_keys(username)
        self.br.find_element_by_id("user_pass").clear()
        self.br.find_element_by_id("user_pass").send_keys(password)
        self.br.find_element_by_id("wp-submit").click()

    def test_case01(self):
        username = "liuchangfu"
        password = "lcfwku1220"
        self.login(username,password)
        title = "测试标题 %s" % time.time()
        self.br.get("http://192.168.1.113:10086/wordpress/wp-admin/post-new.php")
        self.br.find_element_by_name("post_title").send_keys(title)
        self.set_content("content content")
        self.br.find_element_by_name("publish").click()
        self.br.get("http://192.168.1.113:10086/wordpress/wp-admin/edit.php")
        assert_text = self.br.find_element_by_css_selector(".row-title").text
        self.assertEqual(assert_text,title)

    #定位到富文本框
    def set_content(self,text):
        js = "document.getElementById('content_ifr').contentWindow.document.body.innerText = '%s'" % (text)
        self.br.execute_script(js)

    def tearDown(self):
        print("Test case end!!!")

if __name__=="__main__":
    unittest.main()

