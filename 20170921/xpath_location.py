from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")

# 用xpath中的id属性定位
driver.find_element_by_xpath("//*[@id='kw']").send_keys('python')

# 用xpath中的name属性定位
driver.find_element_by_xpath("//*[@name='wd']").send_keys('python')

# 用xpath中的class属性定位
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys('python')

# 用xpath其它属性定位
driver.find_element_by_xpath("//*[@autocomplete='off' ]").send_keys('python')

# 通过xpath标签+id定位
driver.find_element_by_xpath("//input[@id='kw']").send_keys('python')

# 通过xpath标签+name定位
driver.find_element_by_xpath("//input[@name='kw']").send_keys('python')

# 通过xpath中的层级来定位,老爸定位到input输入框
driver.find_element_by_xpath("//span[@id='s_kw_wrap']/input").send_keys('python')

# 通过xpath中的层级来定位,爷爷定位到input输入框
driver.find_element_by_xpath("//from[@id='from']/span/input").send_keys('python')

# 用xpath定位老大
driver.find_element_by_xpath("//select[@id='nr']/option[1]").click()

# 用xpath定位老二
driver.find_element_by_xpath("//select[@id='nr']/option[2]").click()

# 用xpath定位老三
driver.find_element_by_xpath("//select[@id='nr']/option[3]").click()

# xpath逻辑运算定位
driver.find_element_by_xpath("//*[id='kw] and @autocomplete='off'").click()

# xpath模糊匹配功能
driver.find_element_by_xpath("//*[contains(text(),'hao123')]").click()

# xpath模糊匹配某个属性
driver.find_element_by_xpath("//*[contains(@id,'kw')]").click()

# xpath模糊匹配以什么开头
driver.find_element_by_xpath("//*[starts-with(@id,'s_kw_')]").click()

# xpath模糊匹配以什么结尾
driver.find_element_by_xpath("//*[ends-with(@id,'s_kw_')]").click()

# xpath正则表达式
driver.find_element_by_xpath("//*[matchs(text(),'hao13')]").click()