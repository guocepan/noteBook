from  selenium import webdriver
import time
from selenium.webdriver import ActionChains
driver = webdriver.Firefox()
driver.get('https://www.jd.com')

# 获取所有的cookies
cookeis = driver.get_cookies()

#返回cookie字典
cookie = driver.get_cookie("www.jd.com")
#删除所有的 cookie
driver.delete_all_cookies()
driver.add_cookie({"NAME":"haohaohao123456","value":"haohaohao123456"})
cookeis = driver.get_cookies()

#返回cookie字典
cookie = driver.get_cookie("www.jd.com")
print(cookeis)
print(cookie)


time.sleep(30)
driver.quit()
