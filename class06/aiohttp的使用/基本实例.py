# -*- coding: utf-8 -*-
# @Time    : 2022/4/28 00:33
# @Author  : Walter
# @File    : 基本实例.py
# @License : (C)Copyright Walter
# @Desc    :
import aiohttp
import asyncio
from aiohttp import TCPConnector


async def get(session, url):
    async with session.get(url) as response:
        return await response.text(), response.status

async def main():
    async with aiohttp.ClientSession(connector=TCPConnector(ssl=False)) as session:
        html, status = await get(session, 'https://cuiqingcai.com')
        print(f'html:{html[:10]}...')
        print(f'status:{status}')

if __name__ == '__main__':
    # 旧版本python
    # asyncio.get_event_loop().run_until_complete(main())

    # python3.7之后
    asyncio.run(main())