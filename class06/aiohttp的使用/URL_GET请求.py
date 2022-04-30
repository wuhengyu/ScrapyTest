# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 12:22
# @Author  : Walter
# @File    : URL_GET请求.py
# @License : (C)Copyright Walter
# @Desc    :

import aiohttp
import asyncio

from aiohttp import TCPConnector

async def main():
    params = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession(connector=TCPConnector(ssl=False)) as session:
        async with session.get('https://www.httpbin.org/get', params=params) as response:
            print(await response.text())

if __name__ == '__main__':
    # 旧版本python
    # asyncio.get_event_loop().run_until_complete(main())

    # python3.7之后
    asyncio.run(main())