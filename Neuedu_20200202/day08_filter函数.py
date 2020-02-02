# -*- coding: utf-8 -*-
# @Time : 2020/2/2 16:17
# @Author : zhu
# @FileName: day08_filter函数.py
# @Software: PyCharm

# filter函数用于过滤

# 创建一个函数判断传入的参数是奇数还是偶数

def func(num):
    if num % 2 == 0:
        return True
    else:
        return False

l = [156415,61,5641,564,6541,5641,56,4156,41,561,8,4,124,5]

l2 = filter(func, l)
print(list(l2))     # [564, 56, 4156, 8, 4, 124]