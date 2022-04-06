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
