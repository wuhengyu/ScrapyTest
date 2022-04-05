# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 22:39
# @Author  : Walter
# @File    : pyquery使用.py
# @License : (C)Copyright Walter
# @Desc    :
import requests
from pyquery import PyQuery as pq

# 字符串初始化
# html = '''
# <div>
# <ul>
# <li class="item-0"><a href="link1.html">1 item</li>
# <li class="item-1"><a href="link2.html">2 item</li>
# <li class="item-2"><a href="link3.html">3 item</li>
# <li class="item-3"><a href="link4.html">4 item</li>
# </ul>
# </div>
# '''
# doc = pq(html)
# print(doc('li'))

# URL初始化
# doc1 = pq('https://cuiqingcai.com')
# print(doc1('title'))
# doc2 = pq(requests.get('https://cuiqingcai.com').text)
# print(doc2('title'))

# 文件初始化
# 先读取文件内容，以字符串形式传递给PyQury对象
doc1 = pq(filename='demo.html')
print(doc1('li'))
