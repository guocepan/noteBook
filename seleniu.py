from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#导入鼠标操作
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()     # 创建Chrome对象.
#driver = webdriver.Firefox()
# 操作这个对象.
driver.get('https://www.jd.com')     # get方式访问百度.
driver.set_window_size(800,600)
driver.implicitly_wait(4)
#time.sleep(2)
#最大化窗口
driver.implicitly_wait(4)

driver.maximize_window
#driver.get_screenshot_as_file('/Screenshots/foo.png')
driver.back()

driver.forward()

#刷新
driver.refresh()

#滚动右边的滚动条
#执行js代码
JS="window.scrollTo(400,document.body.scrollHeight)"
driver.execute_script(JS)

#保存图片？
driver.save_screenshot("save.png")

#模拟鼠标下拉

time.sleep(10)
driver.quit()   # 使用完, 记得关闭浏览器, 不然chromedriver.exe进程为一直在内存中.