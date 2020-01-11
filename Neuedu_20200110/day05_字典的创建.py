# -*- coding: utf-8 -*-
# @Time : 2020/1/11 19:34
# @Author : zhu
# @FileName: day05_字典的创建.py
# @Software: PyCharm

"""
字典：包含若干 "键 "："值 "对的无序可变序列。字典的键是不可变元素，如：整数，实数，字符串，元组等。
"""

# 创建一个空字典
dict1 = {}
print(type(dict1))  # <class 'dict'>

# 创建一个有数据的字典
dict2 = {"小明": 98, "小红": 100, "小王": 60}
print(dict2)        # {'小明': 98, '小红': 100, '小王': 60}

# fromkeys方法
dict3 = {}
dict3 = dict3.fromkeys(["name", "sex", "score"])
print(dict3)        # {'name': None, 'sex': None, 'score': None}
