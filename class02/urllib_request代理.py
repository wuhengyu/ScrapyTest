# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 13:14
# @Author  : Walter
# @File    : urllib_request代理.py
# @License : (C)Copyright Walter
# @Desc    :
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:8080',
    'https': 'https://127.0.0.1:8080'
})
opener = build_opener(proxy_handler)
url = 'https://www.baidu.com'
try:
    response = opener.open(url)
    print(response.read().decode())
except URLError as e:
    print(e.reason)

