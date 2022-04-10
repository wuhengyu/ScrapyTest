# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 12:10
# @Author  : Walter
# @File    : 基于JWT的模拟登录爬取实战.py
# @License : (C)Copyright Walter
# @Desc    :
import requests
from urllib.parse import urljoin

# 公众部分
BASE_URL = 'https://login3.scrape.center/'
LOGIN_URL = urljoin(BASE_URL, '/api/login')
INDEX_URL = urljoin(BASE_URL, '/api/book')
USERNAME = 'admin'
PASSWORD = 'admin'

response_login = requests.post(LOGIN_URL, json={
    'username': USERNAME,
    'password': PASSWORD
})
data = response_login.json()
print('response_json:', data)
jwt = data.get('token')
print('jwt:', jwt)

headers = {
    'Authorization': f'jwt {jwt}'
}
response_index = requests.get(INDEX_URL, params={
    'limit': 18,
    'offset': 0
}, headers=headers)
print('Response Status', response_index.status_code)
print('Response URL', response_index.url)
print('Response Data', response_index.json())