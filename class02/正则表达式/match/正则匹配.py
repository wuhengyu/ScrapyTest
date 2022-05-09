# -*- coding: utf-8 -*-
# @Time    : 2022/5/9 12:15
# @Author  : Walter
# @File    : 正则匹配.py
# @License : (C)Copyright Walter
# @Desc    :
import re

# ^:匹配字符串开头
# \s:空格
# \d:数字
# \d{4}:4个数字
# \w{10}:10个字母和下划线

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())

print('-'*50+'resulit2'+'-'*50)
content2 = 'Hello 1234567 World_This is a Regex Demo'
result2 = re.match('^Hello\s(\d+)\s\w{10}', content2)
print(result2)
print(result2.group())
print(result2.group(1))
print(result2.span())