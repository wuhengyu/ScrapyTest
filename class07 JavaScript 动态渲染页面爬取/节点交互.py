# -*- coding: utf-8 -*-
# @Time    : 2022/4/11 23:36
# @Author  : Walter
# @File    : 节点交互.py
# @License : (C)Copyright Walter
# @Desc    :

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element(by=By.ID, value='q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element(by=By.CLASS_NAME, value='btn-search')
button.click()
browser.close()