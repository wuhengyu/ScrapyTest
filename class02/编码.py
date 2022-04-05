# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 20:01
# @Author  : Walter
# @File    : 编码.py
# @License : (C)Copyright Walter
# @Desc    :

# 在 Python 中，有 2 种常用的字符串类型，分别为 str 和 bytes 类型，其中 str 用来表示 Unicode 字符，bytes 用来表示二进制数据。
# str 类型和 bytes 类型之间就需要使用 encode() 和 decode() 方法进行转换。

print("encode()方法")
# 将 str 类型字符串“德尔塔”转换成 bytes 类型,默认采用 UTF-8 编码，也可以手动指定其它编码格式
str1 = "德尔塔"
print(str1.encode())
print(str1.encode('GBK'))

print("decode()方法")
str2 = "奥密克戎"
# bytes 类型，UTF-8 编码
bytes1 = str2.encode()
print(bytes1.decode())

print("错误解码")
str3 = "奥密克戎和德尔塔"
bytes2 = str3.encode('GBK')
print(bytes2.decode('GBK'))
