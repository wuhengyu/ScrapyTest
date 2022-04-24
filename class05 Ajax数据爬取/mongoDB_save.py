# -*- coding: utf-8 -*-
# @Time    : 2022/4/24 11:13
# @Author  : Walter
# @File    : mongoDB_save.py
# @License : (C)Copyright Walter
# @Desc    :
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'movies'
MONGO_CONNECTION_NAME = 'movies'
import pymongo
client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['movies']
collection = db['movies']

def save_data(data):
    print(data.get('name'))
    collection.update_one({
        'name': data.get('name')
    },{
        '$set': data
    }, upsert=True)