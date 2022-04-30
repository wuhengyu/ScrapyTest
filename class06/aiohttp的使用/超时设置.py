# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 13:45
# @Author  : Walter
# @File    : 超时设置.py
# @License : (C)Copyright Walter
# @Desc    :
import aiohttp
import asyncio

from aiohttp import TCPConnector

async def main():
    timeout = aiohttp.ClientTimeout(total=1)
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession(timeout=timeout, connector=TCPConnector(ssl=False)) as session:
        async with session.post('https://www.httpbin.org/post', data=data) as response:
            print('status:', response.status)
            print('header:', response.headers)
            print('body:', await response.text())
            print('byte:', await response.read())
            print('json:', await response.json())

if __name__ == '__main__':
    # 旧版本python
    # asyncio.get_event_loop().run_until_complete(main())

    # python3.7之后
    asyncio.run(main())