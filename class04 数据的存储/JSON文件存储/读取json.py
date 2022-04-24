# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 19:38
# @Author  : Walter
# @File    : json文件存储.py
# @License : (C)Copyright Walter
# @Desc    :
import json

str_json1 = '''
{
    "features":[
        {
            "id":1,
            "geometry":{
                "type":"Point",
                "coordinates":[
                    533958.52189999819,
                    3123489.1460000016
                ]
            }
        },
       {
            "id":1,
            "geometry":{
                "type":"Point",
                "coordinates":[
                    533958.52189999819,
                    3123489.1460000016
                ]
            }
        },
    ]
}
'''
import json

print(type(str_json1))
data1 = json.loads(json.dumps(str_json1))
print(data1)
print(type(data1))

# 符合json字符串
str_json2 = '{"name":"zhangsan","age":"17","email":"123@163.com"}'
print(type(str_json2))
data2 = json.loads(str_json2)
print(data2)
print(type(data2))

# 不符合json字符串
str_json3 = "{'name':'zhangsan','age':'17','email':'123@163.com'}"
print(type(str_json3))
data3 = json.loads(json.dumps(str_json3))
print(data3)
print(type(data3))

print(f'{"=" * 100}')

str_json2 = '''
[{
    "name":"wuhengyu1",
    "age":"18",
    "school":"Peking University",
    "birthday":"1993-10-18"
},{
    "name":"wuhengyu2",
    "age":"28",
    "school":"Tsinghua University",
    "birthday":"1995-10-18"
}]
'''
print(type(str_json2))
print(json.loads(str_json2))
print(json.loads(json.dumps(str_json2, indent=4, ensure_ascii=False)))
data4 = json.loads(str_json2)
print(data4[0]['name'])
print(data4[1].get('school'))


# # Json字符串的标识需要使用双引号，单引号报错json.decoder.JSONDecodeError
# print(f'{"=" * 100}')
# str_json3 = '''
# [{
#     'name':'wuhengyu1',
#     'age':'18',
# }]
# '''
# print(json.loads(str_json3))

print('loads:解析Json字符串，转化为Json对象')
with open('data.json', encoding='UTF-8') as file:
    str = file.read()
    print(str)
    print(type(str))
    data5 = json.loads(str)
    print(data5)
    print(type(data5))

print('load:将文件中的json的格式转化成python对象提取出来, 同样可以将文本转化Json对象')
data6 = json.load(open('data.json', encoding='UTF-8'))
print(data6)
print(type(data6))