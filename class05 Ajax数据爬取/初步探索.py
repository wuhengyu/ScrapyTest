# -*- coding: utf-8 -*-
# @Time    : 2022/4/23 23:15
# @Author  : Walter
# @File    : 初步探索.py
# @License : (C)Copyright Walter
# @Desc    :
import json

import requests
import logging
import mongoDB_save

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')
INDEX_URL = 'https://spa1.scrape.center/api/movie?limit={limit}&offset={offset}'
url = 'https://spa1.scrape.center/'
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'

def scrape_api(url):
    logging.info('正在抓取网页链接：%s', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error('错误状态码 %s 和链接 %s', response.status_code, url)
    except requests.RequestException:
        logging.error("错误URL %s", url, exc_info=True)


def scrape_index(page):
    LIMIT = 10
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)

def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)

def main(page):
    for page in range(1, page + 1):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data: %s', detail_data)
            mongoDB_save.save_data(detail_data)
            logging.info('数据写入成功')

if __name__ == '__main__':
    main(10)