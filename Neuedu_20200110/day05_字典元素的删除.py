# -*- coding: utf-8 -*-
# @Time : 2020/1/16 12:51
# @Author : zhu
# @FileName: day05_字典元素的删除.py
# @Software: PyCharm

dict2 = {"小明": 98, "小红": 100, "小王": 60}
# .pop()方法，在列表中也有，列表是有序的，所以列表中pop方法是移除末端或移除制定索引的值，
# 而字典是无序的，不能按索引来删除，只能按键进行删除操作，使用pop方法删除元素，只会返回值
n = dict2.pop("小王")
print(n)        # 60
print(dict2)    # {'小明': 98, '小红': 100}

# .popitem()随机删除字典中的一对键值对，实际使用中删除最后一对键值对，因为字典无序，所以称为随机删除
n1 = dict2.popitem()
print(n1)   # ('小红', 100)
print(dict2)    # {'小明': 98}

# .clear()清空字典
dict2.clear()
print(dict2)    # {}

# del 删除字典
del dict2
# print(dict2) 报错
