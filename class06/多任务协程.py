# -*- coding: utf-8 -*-
# @Time    : 2022/4/27 15:22
# @Author  : Walter
# @File    : 多任务协程.py
# @License : (C)Copyright Walter
# @Desc    :

import asyncio
import requests

async def request():
    url = 'https://www.baidu.com'
    response = requests.get(url)
    return response

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
print(tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print(task.result())
