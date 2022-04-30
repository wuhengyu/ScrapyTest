# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 14:16
# @Author  : Walter
# @File    : 并发限制.py
# @License : (C)Copyright Walter
# @Desc    :
import aiohttp
import asyncio

from aiohttp import TCPConnector

numbers = 10
url = 'https://www.luochu.com'
semaphore = asyncio.Semaphore(numbers)
session = None

async def scrape_api(session):
    async with semaphore:
        print(url)
        async with session.get(url) as response:
            # await asyncio.sleep(1)
            return await response.text()


async def main():
    # global session
    session = aiohttp.ClientSession(connector=TCPConnector(ssl=False))
    tasks = [asyncio.ensure_future(scrape_api(session)) for _ in range(100)]
    await asyncio.gather(*tasks)
    await session.close()


if __name__ == '__main__':
    # 旧版本python
    # asyncio.get_event_loop().run_until_complete(main())

    # python3.7之后
    asyncio.run(main())
