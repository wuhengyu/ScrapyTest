# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 23:16
# @Author  : Walter
# @File    : 基本CSS选择器.py
# @License : (C)Copyright Walter
# @Desc    :

html = '''
<div id="container">
    <ul class="list">
        <li class="item-0"><a href="link1.html"><span class="1"></span>1 item</li>
        <li class="item-1"><a href="link2.html"><span class="1"></span>2 item</li>
        <li class="item-2"><a href="link3.html"><span class="1"></span>3 item</li>
        <li class="item-3"><a href="link4.html"><span class="1"></span>4 item</li>
    </ul>
</div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
print(doc("#container .list li"))
print(type("#container .list li"))
print(doc("li"))
print(type("li"))

for item in doc("#container .list li").items():
    print(item.text())
