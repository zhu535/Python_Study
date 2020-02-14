# -*- coding: utf-8 -*-
# @Time : 2020/2/14 17:42
# @Author : zhu
# @FileName: day_collections中的namedtuple类.py
# @Software: PyCharm

from collections import namedtuple

Person = namedtuple("Person", "name age sex")

p = Person("张三", 18 , "男")

print(type(p))  # <class '__main__.Person'>
print(p)    # Person(name='张三', age=18, sex='男')
print(p.name)   # 张三