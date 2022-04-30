# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 22:07
# @Author  : Walter
# @File    : crawling_data.py
# @License : (C)Copyright Walter
# @Desc    :
import asyncio
import json
import logging
import aiohttp
from aiohttp import TCPConnector
import basic_config
import data_save

semaphore = asyncio.Semaphore(basic_config.CONCURRENCY)

async def scrape_api(url, session):
    async with semaphore:
        try:

            logging.info("链接: %s", url)
            async with session.get(url) as response:
                # await session.close()
                return await response.text()

        except aiohttp.ClientError:
            logging.error("错误链接: %s", url, exc_info=True)


async def scrape_index(page, session):
    url = basic_config.INDEX_URL.format(offset=basic_config.PAGE_SIZE * (page - 1))
    return await scrape_api(url, session)


async def scrape_detail(id, session):
    url = basic_config.DETAL_URL.format(id=id)
    data = await scrape_api(url, session)
    await data_save.save_data(data)

async def main():
        session = aiohttp.ClientSession(connector=TCPConnector(ssl=False))
        list_tasks = [asyncio.ensure_future(scrape_index(page, session)) for page in range(1, basic_config.PAGE_SIZE + 1)]

        results = await asyncio.gather(*list_tasks)
        # await session.close()

        # for result in results:
            # print('type(result):', type(result))
            # print(result)
            # print('json.loads(result):', json.loads(result))
            # print('type(json.loads(result)):', type(json.loads(result)))
            # print(type(json.dumps(json.loads(result), indent=4, ensure_ascii=False)))

            # print(json.dumps(result, indent=4, ensure_ascii=False))
            # loads将Json字符串解码成python对象，字典类型,dumps再将python对象编码成Json字符串，字符串类型
            # logging.info('result:%s', json.dumps(json.loads(result), indent=4, ensure_ascii=False))

        ids = []
        for index_data in results:
            if not index_data:
                continue
            index_data = json.loads(str(index_data))
            for item in index_data.get('results'):
                ids.append(item.get('id'))
        print(ids)

        detail_tasks = [asyncio.ensure_future(scrape_detail(id, session)) for id in ids]
        await asyncio.wait(detail_tasks)
        await session.close()


if __name__ == '__main__':
    # 旧版本python
    # asyncio.get_event_loop().run_until_complete(main())

    # python3.7之后
    asyncio.run(main())
