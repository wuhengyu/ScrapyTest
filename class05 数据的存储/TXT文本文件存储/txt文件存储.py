# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 23:40
# @Author  : Walter
# @File    : txt文件存储.py
# @License : (C)Copyright Walter
# @Desc    :
import requests
from pyquery import PyQuery as pq
import re

url = 'https://ssr1.scrape.center/'
html = requests.get(url).text
doc = pq(html)
items = doc('.el-card').items()
file = open('movies.txt', 'w', encoding='utf-8')
for item in items:
    # 电影名称
    name = item.find('a > h2').text()
    file.write(f'名称:{name}\n')
    # 类别
    categories = [item.text() for item in item.find('.categories button span').items()]
    file.write(f'类别:{categories}\n')
    # 上映时间
    published_at = item.find('.info:contains(上映)').text()
    # published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
    # if published_at and re.search('(\d{4}-\d{2}-\d{2})', published_at) else None
    # 或
    published_rex = re.compile("([0-9]*)(-*)([0-9]*)(-*)([0-9]*)")
    published_at = published_rex.search(published_at).group()
    file.write(f'上映时间:{published_at}\n')
    # 评分
    score = item.find('p.score').text()
    file.write(f'评分:{score}\n')
    # 时间
    movie_time = item.find('.info span:nth-child(3)').text()
    file.write(f'电影时长:{movie_time}\n')
    # 国家
    nation = [item.text() for item in item.find('.info span:nth-child(1)').items()][0]
    file.write(f'上映国家:{nation}\n')
    file.write(f'{"=" * 50}\n')
file.close()
