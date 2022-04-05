# -*- coding: utf-8 -*-
# @Time    : 2022/3/17 0:40
# @Author  : Walter
# @File    : 遍历100次网站.py
# @License : (C)Copyright Walter
# @Desc    :
import asyncio

# # async
# async def execute(x):
#     print("Number:", x)
#
# coroutine = execute(1)
# print("coroutine:", coroutine)
# print("async定义的方法是一个无法直接执行的协程对象，必须将此对象注册到事件循环中，才可以执行")
# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
# print("after calling loop")



# # task
# async def execute(x):
#     print("Number:", x)
#     return x
#
# coroutine = execute(1)
# print("coroutine:", coroutine)
# print("after calling execute")
# # 定义loop对象
# loop = asyncio.get_event_loop()
# # 将协程对象转化成task对象
# task = loop.create_task(coroutine)
# print("task:", task)
# loop.run_until_complete(task)
# print("task:", task)
# print("after calling loop")


# ensure_future
async def execute(x):
    print("Number:", x)
    return x

coroutine = execute(1)
print("coroutine:", coroutine)
print("after calling execute")
# 不借助loop对象loop.create_task方法，定义task对象
task = asyncio.ensure_future(coroutine)
print("task:", task)
# 定义loop对象
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print("task:", task)
print("after calling loop")


