# -*- coding: utf-8 -*-
# @Time : 2020/1/18 15:27
# @Author : zhu
# @FileName: day05_字典推导式.py
# @Software: PyCharm

d1 = {"a": 10, "b": 34, "A": 7, "Z": 3}
# 要求把字母大小写的次数计算

d2 = {}

for i in d1:
    d2[i.lower()] = d1.get(i.lower(), 0) + d1.get(i.upper(), 0)

print(d2)   # {'a': 17, 'b': 34, 'z': 3}

# 使用字典推导式
d3 = {i.lower(): d1.get(i.lower(), 0) + d1.get(i.upper(), 0) for i in d1}
print(d3)   # {'a': 17, 'b': 34, 'z': 3}
