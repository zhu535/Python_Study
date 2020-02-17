# -*- coding: utf-8 -*-
# @Time : 2020/2/17 14:21
# @Author : zhu
# @FileName: day14_正则表达式分组.py
# @Software: PyCharm

import re

s = "我喜欢吃小面，我喜欢吃糖果，我喜欢吃面包，我喜欢吃油条，我喜欢吃火锅"

p = re.compile("(我喜欢吃)(小面|火锅)")

ret = p.search(s)

print(ret.group(0))     # 我喜欢吃小面
print(ret.group(1))     # 我喜欢吃
print(ret.group(2))     # 小面

print(ret)

s1 = "<h1>这是个标题</h1>"
ret = re.match(r"<(\w+)>.*</\1>", s1)
print(ret)      # <re.Match object; span=(0, 14), match='<h1>这是个标题</h1>'>


s2 = "<body><h1>这是个标题</h1></body>"
ret1 = re.match(r"<(\w+)><(\w+)>.*</\2></\1>", s2)
print(ret1)     # <re.Match object; span=(0, 27), match='<body><h1>这是个标题</h1></body>'>

ret2 = re.match(r"<(?P<body>\w+)><(?P<h1>\w+)>.*</(?P=h1)></(?P=body)>", s2)
print(ret2)     # <re.Match object; span=(0, 27), match='<body><h1>这是个标题</h1></body>'>

# 忽略大小写的正则表达式
s4 = "UPPER PYTHON,lower python,Mixed Python"

ret3 = re.findall("python", s4, re.IGNORECASE)
print(ret3)