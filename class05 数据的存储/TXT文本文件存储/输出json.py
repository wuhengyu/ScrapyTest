# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 23:27
# @Author  : Walter
# @File    : 输出json.py
# @License : (C)Copyright Walter
# @Desc    :

import json

data = [{
    "name": "wuhengyu1",
    "age": "18",
    "school": "Peking University",
    "birthday": "1993-10-18"
}, {
    "name": "wuhengyu2",
    "age": "28",
    "school": "Tsinghua University",
    "birthday": "1995-10-18"
}]
# dumps:将json对象转化成字符串，并写入
with open('write_json_data_dumps.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))

# dump:直接将json对象写入文本
json.dump(data, open('write_json_data_dump.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
