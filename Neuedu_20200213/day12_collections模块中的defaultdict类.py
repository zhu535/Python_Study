# -*- coding: utf-8 -*-
# @Time : 2020/2/14 16:16
# @Author : zhu
# @FileName: day12_collections模块中的defaultdict类.py
# @Software: PyCharm

from collections import defaultdict

# defaultdict需要接收一个方法的返回值作为字典的默认值

def func():
    return "hahah"

d = defaultdict(func)

print(d["name"])    # hahah

# 简化后：
d3 = defaultdict(lambda: "hahaha")
print(d3["name"])   # hahaha

d1 = defaultdict(list)
d1["name"].append("zhangsan")
d1["name"].append("lisi")
print(d1["name"])   # ['zhangsan', 'lisi']