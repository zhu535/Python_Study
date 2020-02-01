# -*- coding: utf-8 -*-
# @Time : 2020/2/1 12:49
# @Author : zhu
# @FileName: day07_匿名函数.py
# @Software: PyCharm


func = lambda n:n*n
print(func(4))  # 16

# 带条件的匿名函数
cale = lambda x,y:x*y if x > y else x/y
print(cale(4,3))    # 12