# -*- coding: utf-8 -*-
# @Time    : 2022/4/24 21:24
# @Author  : Walter
# @File    : ensure_future.py
# @License : (C)Copyright Walter
# @Desc    :

import asyncio

async def execute(x):
    print("Number:", x)
coroutine = execute(1)
print("coroutine:", coroutine)

# 直接使用asyncio，不使用loop对象
# task = loop.create_task(coroutine)
task = asyncio.ensure_future(coroutine)
# 定义loop对象
loop = asyncio.get_event_loop()
print("task:", task)
loop.run_until_complete(task)
print("task:", task)
