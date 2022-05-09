# -*- coding: utf-8 -*-
# @Time    : 2022/4/9 21:45
# @Author  : Walter
# @File    : 基于Session和Cookie的模拟爬取实战.py
# @License : (C)Copyright Walter
# @Desc    :
import time

import requests
from urllib.parse import urljoin

# 公众部分
BASE_URL = 'https://login2.scrape.center/'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

# 原始版本
# response_login = requests.post(LOGIN_URL, data.md={
#     'username': USERNAME,
#     'password': PASSWORD
# })
# response_index = requests.get(INDEX_URL)
# print('Response Status', response_index.status_code)
# print('response URL', response_index.url)

# 改进版本，增加cookies
# response_login = requests.post(LOGIN_URL, data.md={
#     'username': USERNAME,
#     'password': PASSWORD
# }, allow_redirects=False)
# cookies = response_login.cookies
# response_index = requests.get(INDEX_URL, cookies=cookies)
# print('Response Status', response_index.status_code)
# print('response URL', response_index.url)

# 改进版本，增加session
# session = requests.session()
# response_login = session.post(LOGIN_URL, data.md={
#     'username': USERNAME,
#     'password': PASSWORD
# }, allow_redirects=False)
# cookies = session.cookies
# print(cookies)
# response_index = session.get(INDEX_URL)
# print('Response Status', response_index.status_code)
# print('Response URL', response_index.url)

# 使用selenium登录获取cookies
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get(BASE_URL)
# browser.find_element_by_css_selector('input[name="username"]').send_keys(USERNAME)
browser.find_element(by=By.CSS_SELECTOR, value='input[name="username"]').send_keys(USERNAME)
browser.find_element(by=By.CSS_SELECTOR, value='input[name="password"]').send_keys(PASSWORD)
browser.find_element(by=By.CSS_SELECTOR, value='input[type="submit"]').click()
time.sleep(10)
cookies = browser.get_cookies()
print("浏览器获取cookie:", cookies)
browser.close()
session = requests.session()
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])
response_index = session.get(INDEX_URL)
print('Response Status', response_index.status_code)
print('response URL', response_index.url)
