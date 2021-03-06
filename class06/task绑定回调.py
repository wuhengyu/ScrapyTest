# -*- coding: utf-8 -*-
# @Time    : 2022/4/25 22:11
# @Author  : Walter
# @File    : task绑定回调.py
# @License : (C)Copyright Walter
# @Desc    :
import asyncio
import logging

import requests
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

start_time = time.time()
async def request():
    URL = 'https://www.httpbin.org/delay/5'
    print('请求链接：', URL)
    response = requests.get(URL)
    # print('响应数据:', response)
    return response


def callback(tasks):
    print('结果:', tasks.result())


coroutine = request()
tasks = asyncio.ensure_future(coroutine)
tasks.add_done_callback(callback)
print(tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)
print(tasks)

end_time = time.time()
logging.info('花费时间 %s 秒', end_time - start_time)