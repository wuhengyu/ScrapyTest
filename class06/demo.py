# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 23:02
# @Author  : Walter
# @File    : demo.py
# @License : (C)Copyright Walter
# @Desc    :

import asyncio

async def execute():
    print("11111111111111")
coroutine = execute()

loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
print(task)
loop.run_until_complete(task)
print(task)


