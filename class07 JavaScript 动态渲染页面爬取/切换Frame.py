# -*- coding: utf-8 -*-
# @Time    : 2022/4/11 23:40
# @Author  : Walter
# @File    : 切换Frame.py
# @License : (C)Copyright Walter
# @Desc    :

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element(by=By.CLASS_NAME, value="logo")
except NoSuchElementException:
    print('NO LOGO')
browser.switch_to.parent_frame()
logo2 = browser.find_element(by=By.CLASS_NAME, value="logo")
print(logo2)
print(logo2.tag_name)
browser.close()