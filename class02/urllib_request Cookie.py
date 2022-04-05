# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 13:14
# @Author  : Walter
# @File    : urllib_request代理.py
# @License : (C)Copyright Walter
# @Desc    :
import http.cookiejar, urllib.request

# 输出cookie
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
url = 'https://www.baidu.com'
response1 = opener.open(url)
for item in cookie:
    print(item.name + "=" + item.value)

# 保存cookie
filename = 'MozillaCookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
url = 'https://www.baidu.com'
response2 = opener.open(url)
cookie.save(ignore_discard=True, ignore_expires=True)

# 保存cookie
filename = 'LWPCookie.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
url = 'https://www.baidu.com'
response3 = opener.open(url)
cookie.save(ignore_discard=True, ignore_expires=True)

# 读取cookie
cookie = http.cookiejar.LWPCookieJar()
cookie.load('LWPCookie.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
url = 'https://www.baidu.com'
response4 = opener.open(url)
print(response4.read().decode())