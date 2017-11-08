from selenium import webdriver
import time

"""
获取QQ首页中，今日话题的标题和文本信息，并自动发布到wordpress中
"""
dr = webdriver.Firefox()

dr.get("http://www.qq.com/")
#获取当前链接的文本信息
title =dr.find_element_by_css_selector("#todaytop > a:nth-child(1)").text
print(title)
dr.find_element_by_css_selector("#todaytop > a:nth-child(1)").click()
time.sleep(3)
#循环遍历并判断是否是当前标签页，如果不是则切换
handles = dr.window_handles
print(handles)
for handle in handles:
    if dr.current_window_handle != handle:
        dr.switch_to.window(handle)
#获取当前窗口的正文信息
text1 = dr.find_element_by_id("articleContent").text
print(text1)

dr.get("http://192.168.1.113:10086/wordpress/wp-login.php")
dr.find_element_by_id("user_login").clear()
dr.find_element_by_id("user_login").send_keys("liuchangfu")
dr.find_element_by_id("user_pass").clear()
dr.find_element_by_id("user_pass").send_keys("lcfwku1220")
dr.find_element_by_id("wp-submit").click()
dr.get("http://192.168.1.113:10086/wordpress/wp-admin/post-new.php")
dr.maximize_window()
dr.find_element_by_name("post_title").send_keys(title)
#切换到富文本框，并把text1的文本内容发送富文本框
dr.find_element_by_id("content_ifr").send_keys(text1)
# js = "window.scrollTo(100,450)"
# dr.execute_script(js)
dr.find_element_by_name("publish").click()
time.sleep(3)
dr.get("http://192.168.1.113:10086/wordpress/wp-admin/edit.php")




