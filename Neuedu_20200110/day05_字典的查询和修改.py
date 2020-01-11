# -*- coding: utf-8 -*-
# @Time : 2020/1/11 19:53
# @Author : zhu
# @FileName: day05_字典的查询和修改.py
# @Software: PyCharm

# 字典可以通过 dict["键"] 来进行查询操作,键不存在则报错
dict2 = {"小明": 98, "小红": 100, "小王": 60}
print(dict2["小明"])      # 98

# 也可以通过.get(键，默认值)来进行查询操作，键不存在时显示默认值
etc = dict2.get("小花", "不存在")
print(etc)      # 不存在

# 修改操作
dict2["小明"] = 96
print(dict2)        # {'小明': 96, '小红': 100, '小王': 60}