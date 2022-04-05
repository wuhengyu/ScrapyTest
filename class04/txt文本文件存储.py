# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 22:35
# @Author  : Walter
# @File    : txt文本文件存储.py
# @License : (C)Copyright Walter
# @Desc    :
import requests
from pyquery import PyQuery as pq

url = 'https://ssr1.scrape.center/'
html = requests.get(url).text
doc = pq(html)