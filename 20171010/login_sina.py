from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.get("https://mail.sina.com.cn/?from=mail")

print("Before login!!!")

#打印当前标题信息
title = dr.title
print(title)
#打印当前网址
now_url = dr.current_url
print(now_url)

dr.find_element_by_xpath("//input[@id='freename']").send_keys("liuchangfu0822@sina.com")
dr.find_element_by_xpath("//input[@id='freepassword']").send_keys("lcfwku1220")
dr.find_element_by_xpath("//div[@class='freeMailbox']//a[.='登录']").click()
time.sleep(3)
print("After login!!")
#再次打印当前页面标题
title1 = dr.title
print(title1)
#再次打印当前地址
now_url1 = dr.current_url
print(now_url1)

text = dr.find_element_by_xpath("//*[@id='greeting']/span").text
print("当前用户名是:",text)

#验证当前登录用户
if text=="liuchangfu0822":
    print("登录成功！！")
else:
    print("登录失败！！")