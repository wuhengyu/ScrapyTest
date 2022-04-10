# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 19:34
# @Author  : Walter
# @File    : Selenium的使用.py
# @License : (C)Copyright Walter
# @Desc    :
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
try:
    browser.get('https://www.cantonfair.org.cn/')
    input = browser.find_element(by=By.CSS_SELECTOR, value='input[type="search"]')
    input.send_keys('包')
    input.send_keys(Keys.ENTER)
    # 显式等待
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'app')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()

