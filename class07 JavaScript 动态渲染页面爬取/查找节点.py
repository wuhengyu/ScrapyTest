# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 22:38
# @Author  : Walter
# @File    : 查找节点.py
# @License : (C)Copyright Walter
# @Desc    :

# 八个定位方式
# find_element_by_id()/find_elements_by_id()/find_element(by=By.ID, value="")/find_elements(by=By.ID, value="")
# find_element_by_link_text()/find_elements_by_link_text()/find_element(by=By.LINK_TEXT, value="")/find_elements(by=By.LINK_TEXT, value="")
# find_element_by_class_name()/find_elements_by_class_name()/find_element(by=By.CLASS_NAME, value="")/find_elements(by=By.CLASS_NAME, value="")
# find_element_by_css_selector()/find_elements_by_css_selector()/find_element(by=By.CSS_SELECTOR, value="")/find_elements(by=By.CSS_SELECTOR, value="")
# find_element_by_name()/find_elements_by_name()/find_element(by=By.NAME, value="")/find_elements(by=By.NAME, value="")
# find_element_by_partial_link_text()/find_elements_by_partial_link_text()/find_element(by=By.PARTIAL_LINK_TEXT, value="")/find_elements(by=By.PARTIAL_LINK_TEXT, value="")
# find_element_by_tag_name()/find_elements_by_tag_name()/find_element(by=By.TAG_NAME, value="")/find_elements(by=By.TAG_NAME, value="")
# find_element_by_xpath()/find_elements_by_xpath()/find_element(by=By.XPATH, value="")/find_elements(by=By.XPATH, value="")

from selenium import webdriver
from selenium.webdriver.common.by import By

# 公众部分
browser = webdriver.Chrome()

# 查找单个节点
browser.get('https://www.taobao.com')
input1 = browser.find_element(by=By.ID, value='q')
input2 = browser.find_element(by=By.CSS_SELECTOR, value='#q')
input3 = browser.find_element(by=By.XPATH, value='//*[@id="q"]')
print(input1)
print(input2)
print(input3)
browser.close()


