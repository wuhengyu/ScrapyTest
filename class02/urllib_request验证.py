# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 13:14
# @Author  : Walter
# @File    : urllib_request代理.py
# @License : (C)Copyright Walter
# @Desc    :

from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

# 验证
username = 'admin'
password = 'admin'
url = 'https://ssr3.scrape.center/'
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode()
    print(html)
except URLError as e:
    print(e.reason)