# -*- coding: utf-8 -*-
# @Time : 2020/2/2 16:10
# @Author : zhu
# @FileName: day08_reduce函数.py
# @Software: PyCharm

from functools import reduce

# 定义一个函数接收两个参数，求和

def func(a, b):
    c = a + b
    return c

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num = reduce(func, l)
print(num)