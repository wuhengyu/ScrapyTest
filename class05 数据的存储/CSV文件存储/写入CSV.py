# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 23:38
# @Author  : Walter
# @File    : 写入CSV.py
# @License : (C)Copyright Walter
# @Desc    :
import csv

# 获得文件句柄csvfile, 调用writerow方法写入每行数据
import pandas as pd

with open('write_csv_data.csv', 'w', newline='') as csvfile:
    # 取消分隔符
    # writer = csv.writer(csvfile, delimiter=' ')
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1', 'wuhengyu1', '11'])
    writer.writerow(['2', 'wuhengyu2', '22'])
    writer.writerow(['3', 'wuhengyu3', '33'])
    writer.writerow(['4', 'wuhengyu4', '44'])
    # 二维列表
    writer.writerows([['1', 'wuhengyu1', '11'], ['1', 'wuhengyu1', '11'], ['1', 'wuhengyu1', '11']])

# 字典写入
# with open('write_csv_data_zidian.csv', 'w') as csvfile:
# 追加写入
with open('write_csv_data_zidian.csv', 'a', encoding='utf8', newline='') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '1', 'name': '测试名称1', 'age': '111'})
    writer.writerow({'id': '1', 'name': '测试名称2', 'age': '111'})
    writer.writerow({'id': '1', 'name': '测试名称3', 'age': '111'})
    writer.writerow({'id': '1', 'name': '测试名称4', 'age': '111'})

import pandas

data = [
    {'id': '1', 'name': '测试名称1', 'age': '111'},
    {'id': '2', 'name': '测试名称2', 'age': '111'},
    {'id': '3', 'name': '测试名称3', 'age': '111'},
    {'id': '4', 'name': '测试名称4', 'age': '111'},
]
# 新建DataFrame对象
df = pandas.DataFrame(data)
# index=0不保存行索引
df.to_csv('pandas_csv_data.csv', index=False)
