# -*- coding: utf-8 -*-
# @Time    : 2022/4/6 15:03
# @Author  : Walter
# @File    : 读取CSV.py
# @License : (C)Copyright Walter
# @Desc    :
import csv

with open('write_csv_data.csv', 'r', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

print(f'{"==" * 50}')
import pandas

df = pandas.read_csv('write_csv_data.csv')
print(df)

print(f'{"==" * 50}')
# 转化列表或元组
df = pandas.read_csv('write_csv_data.csv')
data3 = df.values.tolist()
print(data3)

print(f'{"==" * 50}')
# 直接对df遍历获取列表
df = pandas.read_csv('write_csv_data.csv')
for index, row in df.iterrows():
    print(row.tolist())
