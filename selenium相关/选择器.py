from selenium import webdriver
from selenium.webdriver.common.by import By  # 选择器
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


browser = webdriver.Chrome()
wait_obj = WebDriverWait(browser, timeout=5)  # 产生一个等待对象，固定最大等待时间

try:
    browser.get('https://www.taobao.com')    
    input_ele = browser.find_element_by_id('q')
    input_ele.send_keys('macpro')
    
    # 定位标签
    # 方式1
    # btn_ele = browser.find_elements_by_class_name('btn-search')[0]
    # 方式2
    btn_ele = browser.find_element(By.CSS_SELECTOR, '.btn-search')
    
    btn_ele.click()
    
    # 等待目标区域标签们加载完成
    wait_obj.until(EC.presence_of_element_located((By.CLASS_NAME, 'next')))
    next_ele = browser.find_element(By.CSS_SELECTOR,'.next a')
    next_ele.click()
    
    ele = browser.find_element(By.ID, 'J_Itemlist_PLink_15348329368')
    # 获取标签属性
    print(ele.get_attribute('href'))
    
    time.sleep(100)
    browser.close()
except:
    browser.close()
    
    