from selenium import webdriver
from selenium.webdriver import ActionChains  # 滑动验证
from selenium.webdriver.common.by import By  # 选择器
from selenium.webdriver.common.keys import Keys  # 模拟键盘的按键
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Chrome()
wait_obj = WebDriverWait(browser,timeout=5)  # 产生一个等待对象，固定最大等待时间
browser.get('https://www.taobao.com')


'''1、基本使用               '''

# 获取标签并填写信息
ele_input = browser.find_element_by_id('kw')
ele_input.send_keys('方淇韩')

#  获取按钮并点击提交
ele_btn = browser.find_element_by_id('su')

# 方式1
ele_btn.click()
# 方式2
ele_btn.send_keys(Keys.ENTER)


# 在设定的等待时间内若加载出来继续执行，反之，后面的代码不会执行
wait_obj.until(EC.presence_of_element_located((By.ID, 'content_left')))

# 获取源码
# ret = browser.page_source
# with open('save.txt', 'w',encoding='utf8') as f:
#     for line in ret:
#         f.write(line)

# 获取相应内容
print(browser.current_url)
print(browser.get_cookies())  

















time.sleep(10)
browser.close()


