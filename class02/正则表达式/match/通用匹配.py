# -*- coding: utf-8 -*-
# @Time    : 2022/5/9 12:43
# @Author  : Walter
# @File    : 通用匹配.py
# @License : (C)Copyright Walter
# @Desc    :
import re
# .*:.匹配任意字符，除了换行符，*匹配不限次数
# $:结尾字符串
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())
