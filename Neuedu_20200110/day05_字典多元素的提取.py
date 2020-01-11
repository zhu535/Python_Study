# -*- coding: utf-8 -*-
# @Time : 2020/1/11 23:20
# @Author : zhu
# @FileName: day05_字典多元素的提取.py
# @Software: PyCharm

dict2 = {"小明": 98, "小红": 100, "小王": 60}

# .items()提取所有的键值对，每组键值对封装为元组
print(list(dict2.items()))      # [('小明', 98), ('小红', 100), ('小王', 60)]

# .keys()提取所有的键,封装为列表
print(list(dict2.keys()))     # ['小明', '小红', '小王']

# .values()提取所有的值，封装为列表
print(list(dict2.values()))     # [98, 100, 60]