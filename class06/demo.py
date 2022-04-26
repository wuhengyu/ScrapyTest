# -*- coding: utf-8 -*-
# @Time    : 2022/4/26 09:45
# @Author  : Walter
# @File    : demo.py
# @License : (C)Copyright Walter
# @Desc    :
import asyncio
import requests
from bs4 import BeautifulSoup
import pdfkit


async def set_after(delay, value):
    await asyncio.sleep(delay)
    print(value)


async def main():
    loop = asyncio.get_running_loop()
    # 在事件循环中创建任务
    task1 = loop.create_task(set_after(2, '... Hello'))
    task2 = loop.create_task(set_after(3, '... world'))
    # 执行任务
    await task1
    await task2

if __name__ == '__main__':
    # asyncio.run(main())

    response = requests.get("http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000")
    soup = BeautifulSoup(response.content, 'html5lib')
    print(soup)
    menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
    urls = []
    for li in menu_tag.find_all("li"):
        url = "http://www.liaoxuefeng.com" + li.a.get('href')
        urls.append(url)
    print(urls)

