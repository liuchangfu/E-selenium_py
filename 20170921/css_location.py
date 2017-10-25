from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")

# 通过CSS中的ID属性定位
driver.find_elements_by_css_selector("#kw").send_keys("python")

# 通过CSS中的class属性定位
driver.find_elements_by_css_selector(".s_ipt).send_keys("python")

# 通过CSS中的标签属性定位
driver.find_elements_by_css_selector("input").send_keys("python")

# 通过CSS中的name属性定位
driver.find_elements_by_css_selector("[name='wd']").send_keys("python")

# 通过CSS中的type属性定位
driver.find_elements_by_css_selector("[type='text']").send_keys("python")

# 通过CSS中的标签与class属性定位
driver.find_elements_by_css_selector("input.s_ipt").send_keys("python")

# 通过CSS中的标签与id属性定位
driver.find_elements_by_css_selector("input#kw").send_keys("python")

# 通过CSS中的标签与其它属性组合定位
driver.find_elements_by_css_selector("input[id='kw']").send_keys("python")