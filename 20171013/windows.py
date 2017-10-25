from selenium import webdriver
import time

br=webdriver.Firefox()
br.get("http://www.qq.com")
br.implicitly_wait(10)
handle_index = br.current_window_handle
print(handle_index)

br.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/strong/a").click()

all_handles = br.window_handles
print(all_handles)

# for handle in all_handles:
#     if handle!=handle_index:
#         br.switch_to.window(handle)
#         print(br.title)
#         time.sleep(2)

br.switch_to.window(all_handles[1])
print(br.title)
