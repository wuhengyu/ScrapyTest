# -*- coding: utf-8 -*-
# @Time    : 2022/4/30 12:34
# @Author  : Walter
# @File    : data_save.py
# @License : (C)Copyright Walter
# @Desc    :
import asyncio
import json
import logging
import crawling_data
import basic_config

from motor.motor_asyncio import AsyncIOMotorClient

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'books'
MONGO_CONNECTION_NAME = 'books'

client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_CONNECTION_NAME]

async def save_data(data):
    logging.info('保存数据 %s', data)
    data = json.loads(str(data))
    if data:
        return await collection.update_one({
            'id': data.get('id')
        },{
            '$set': data
        }, upsert=True)



