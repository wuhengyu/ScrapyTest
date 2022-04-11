# -*- coding: utf-8 -*-
# @Time    : 2022/4/11 23:35
# @Author  : Walter
# @File    : 多个节点.py
# @License : (C)Copyright Walter
# @Desc    :

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
products_list = browser.find_elements(by=By.CSS_SELECTOR, value='.service-bd li')
print(products_list)
browser.close()