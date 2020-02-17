# -*- coding: utf-8 -*-
# @Time : 2020/2/17 14:18
# @Author : zhu
# @FileName: day14_正则表达式的编译.py
# @Software: PyCharm

import re
tel = "18922025720"
p = re.compile("^1\d{10}$")
print(p.match(tel)) # <re.Match object; span=(0, 11), match='18922025720'>

if p.match(tel):
    print("true")
else:
    print("false")      # true