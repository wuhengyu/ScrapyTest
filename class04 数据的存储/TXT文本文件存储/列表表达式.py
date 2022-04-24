# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 19:10
# @Author  : Walter
# @File    : 列表表达式.py
# @License : (C)Copyright Walter
# @Desc    :

x = []

# for i in range(5):
#     if (i * i) % 2:
#         x.append(i * i)
# print(x)

print([i * i for i in range(5) if ((i * i) % 2)])