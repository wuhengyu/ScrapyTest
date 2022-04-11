# -*- coding: utf-8 -*-
# @Time    : 2022/4/11 23:37
# @Author  : Walter
# @File    : 动作链.py
# @License : (C)Copyright Walter
# @Desc    :

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

browser1 = webdriver.Chrome()
browser1.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser1.switch_to.frame('iframeResult')
source = browser1.find_element(by=By.CSS_SELECTOR, value="#draggable")
target = browser1.find_element(by=By.CSS_SELECTOR, value="#droppable")
actions = ActionChains(browser1)
actions.drag_and_drop(source, target)
actions.perform()