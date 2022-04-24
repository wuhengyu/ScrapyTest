# -*- coding: utf-8 -*-
# @Time    : 2022/3/17 0:40
# @Author  : Walter
# @File    : 单线程循环.py
# @License : (C)Copyright Walter
# @Desc    :
import requests
import logging
import time
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
TOTAL_NUMBER = 10
URL = 'https://www.httpbin.org/delay/5'
start_time = time.time()
for _ in range(1, TOTAL_NUMBER+1):
    logging.info('请求链接：%s', URL)
    response = requests.get(URL)
end_time = time.time()
logging.info('花费时间 %s 秒', end_time - start_time)
