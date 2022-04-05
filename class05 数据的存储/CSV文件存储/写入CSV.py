# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 23:38
# @Author  : Walter
# @File    : 写入CSV.py
# @License : (C)Copyright Walter
# @Desc    :
import csv
# 获得文件句柄csvfile, 调用writerow方法写入每行数据
with open('write_csv_data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1', 'wuhengyu1', '11'])
    writer.writerow(['2', 'wuhengyu2', '22'])
    writer.writerow(['3', 'wuhengyu3', '33'])
    writer.writerow(['4', 'wuhengyu4', '44'])
    # 二维列表
    writer.writerows([['1', 'wuhengyu1', '11'], ['1', 'wuhengyu1', '11'], ['1', 'wuhengyu1', '11']])

# 字典写入
with open('write_csv_data_zidian.csv', 'w') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '1', 'name': 'zidian', 'age': '111'})
    writer.writerow({'id': '1', 'name': 'zidian', 'age': '111'})
    writer.writerow({'id': '1', 'name': 'zidian', 'age': '111'})
    writer.writerow({'id': '1', 'name': 'zidian', 'age': '111'})
