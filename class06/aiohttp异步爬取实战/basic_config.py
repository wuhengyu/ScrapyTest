# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 21:52
# @Author  : Walter
# @File    : basic_config.py
# @License : (C)Copyright Walter
# @Desc    :
import logging

import aiohttp
from aiohttp import TCPConnector

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://spa5.scrape.center/api/book?limit=18&offset={offset}'
DETAL_URL = 'https://spa5.scrape.center/api/book/{id}'
PAGE_SIZE = 2
PAGE_NUMBER = 100
CONCURRENCY = 1