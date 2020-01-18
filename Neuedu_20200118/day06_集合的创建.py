# -*- coding: utf-8 -*-
# @Time : 2020/1/18 15:44
# @Author : zhu
# @FileName: day06_集合的创建.py
# @Software: PyCharm

# 集合set无序且元素不可重复

# 如何定义一个空集合？注意：定义空集合时不能使用大括号定义，与空字典重复
s = set()
print(type(s))  # <class 'set'>

# 如何定义一个有内容的集合？
s1 = {"张三", "李四", "李四"}
print(s1)   # {'李四', '张三'}
print(type(s))  # <class 'set'>
