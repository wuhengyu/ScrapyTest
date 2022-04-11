# -*- coding: utf-8 -*-
# @Time    : 2022/4/11 23:38
# @Author  : Walter
# @File    : 运行JS.py
# @License : (C)Copyright Walter
# @Desc    :

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(3)
browser.execute_script('alert("To Bottom")')
browser.close()