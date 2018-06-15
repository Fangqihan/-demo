from selenium import webdriver
from selenium.webdriver.common.by import By  # 选择器
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


def get_img():
    browser.save_screenshot('snap.png')


browser = webdriver.Chrome()
browser.get('https://auth.geetest.com/login/')
wait_obj = WebDriverWait(browser, timeout=10)  # 产生一个等待对象，固定最大等待时间

try:
    # 1、填写用户名和密码后点击验证
    email_ele = browser.find_element(By.CSS_SELECTOR, ('[type="email"]'))
    email_ele.send_keys('qihanfang@foxmail.com')
    pwd_ele = browser.find_element(By.CSS_SELECTOR, ('[type="password"]'))
    pwd_ele.send_keys('fqh202')
    button=wait_obj.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_radar_tip')))
    button.click()
    time.sleep(2)  # 防止有延迟
    # 2、取到完整的验证图片
    get_img()
    
    
    
    time.sleep(100)
except:
    browser.close()



