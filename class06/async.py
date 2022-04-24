# -*- coding: utf-8 -*-
# @Time    : 2022/3/17 0:40
# @Author  : Walter
# @File    : 单线程循环.py
# @License : (C)Copyright Walter
# @Desc    :
import asyncio

async def execute(x):
    print("Number:", x)

coroutine = execute(1)
print("coroutine:", coroutine)
print("async定义的方法是一个无法直接执行的协程对象，必须将此对象注册到事件循环中，才可以执行")
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)



