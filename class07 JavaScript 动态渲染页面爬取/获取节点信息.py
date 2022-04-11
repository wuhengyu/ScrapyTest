# -*- coding: utf-8 -*-
# @Time    : 2022/4/11 23:40
# @Author  : Walter
# @File    : 获取节点信息.py
# @License : (C)Copyright Walter
# @Desc    :

# 公众部分
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://spa2.scrape.center/'
browser.get(url)

# 获取属性
logo = browser.find_element(by=By.CLASS_NAME, value="logo-image")
print(logo)
print(logo.get_attribute('src'))
browser.close()

# 获取文本值
logo2 = browser.find_element(by=By.CLASS_NAME, value="logo-title")
print(logo2.text)
browser.close()

# 获取ID/位置/标签名/大小
logo3 = browser.find_element(by=By.CLASS_NAME, value="logo-title")
print(logo3.id, logo3.location, logo3.tag_name, logo3.size)
browser.close()