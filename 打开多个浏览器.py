from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.jd.com")
js = 'window.open("https://www.jd.com");'
js2= 'window.open("https://www.taobao.com");'
driver.execute_script(js)
driver.execute_script(js2)
driver.execute_script(js2)
driver.execute_script(js2)
driver.execute_script(js2)
