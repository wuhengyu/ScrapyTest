# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 15:39
# @Author  : Walter
# @File    : urllib使用.py
# @License : (C)Copyright Walter
# @Desc    : urllib库


import urllib.parse
import urllib.request

# urlopen
# urlopen参数
# response = urllib.request.urlopen('https://www.python.org')
# # print(response.read().decode('utf-8'))
# print(response.getheaders())
# print(response.getheader('Server'))

# data参数
# bytes方法把参数转化为字节流编码格式
# data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
# response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
# print(response.read().decode())

# timeout参数
# response = urllib.request.urlopen('https://www.httpbin.org/post', timeout=0.1)
# print(response.read())

# request
# request = urllib.request.Request('https://www.python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode())

# request 6个参数
# from urllib import request
#
# url = 'https://www.httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
#     'HOST': 'www.httpbin.org'
# }
# dict = {
#     'name': 'germey'
# }
# data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
# # 案例1
# req1 = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
# response1 = request.urlopen(req1)
# print(response1.read().decode())
# # 案例2
# req2 = urllib.request.Request(url=url, data=data, method='POST')
# req2.add_header('User-Agent',
#                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36')
# response2 = request.urlopen(req2)
# print(response2.read().decode())

# 高级用法
# urllib.request.HTTPDefaultErrorHandler HTTP响应错误
# urllib.request.HTTPRedirectHandler 处理重定向
# urllib.request.HTTPCookieProcessor 处理Cookie
# urllib.request.ProxyHandler 设置代理，默认为空
# urllib.request.HTTPPasswordMgr 管理密码
# urllib.request.HTTPBasicAuthHandler 管理认证
# urllib.request.OpenerDirector 高级功能进行配置
