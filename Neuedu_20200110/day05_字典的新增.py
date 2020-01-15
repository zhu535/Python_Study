# -*- coding: utf-8 -*-
# @Time : 2020/1/15 23:27
# @Author : zhu
# @FileName: day05_字典的新增.py
# @Software: PyCharm

dict2 = {"小明": 98, "小红": 100, "小王": 60}

# .setdefault()方法，通过键获取值，如果键不存在，则为列表新增一个键值对
exm = dict2.setdefault("小明", 90)
print(exm)  # 96

exm1 = dict2.setdefault("小猪", 100)
print(dict2)    # {'小明': 96, '小红': 100, '小王': 60, '小猪': 100}

# 增加一组键值对，如果键存在则是修改键对应的值
dict2["小明"] = 97
dict2["小李"] = 57
print(dict2)    # {'小明': 97, '小红': 100, '小王': 60, '小猪': 100, '小李': 57}

# 字典的合并
dict3 = {"小黄": 50, "小欧": 60}
dict2.update(dict3)
print(dict2)    # {'小明': 97, '小红': 100, '小王': 60, '小猪': 100, '小李': 57, '小黄': 50, '小欧': 60}