# -*- coding: utf-8 -*-
# @Time    : 2022/4/14 00:30
# @Author  : Walter
# @File    : 前进和后退.py
# @License : (C)Copyright Walter
# @Desc    :
import time

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
time.sleep(1)
browser.get('https://www.taobao.com')
time.sleep(1)
browser.get('https://www.qq.com')
time.sleep(1)
browser.back()
time.sleep(1)
browser.forward()
browser.close()