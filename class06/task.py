# -*- coding: utf-8 -*-
# @Time    : 2022/4/24 21:24
# @Author  : Walter
# @File    : task.py
# @License : (C)Copyright Walter
# @Desc    :
import asyncio


async def execute(x):
    print("Number:", x)
    return x

coroutine = execute(1)
print("coroutine:", coroutine)
# 定义loop对象
loop = asyncio.get_event_loop()
# 将协程对象转化成task对象
task = loop.create_task(coroutine)
print("task:", task)
loop.run_until_complete(task)
print("task:", task)