# -*- coding: utf-8 -*-
# @Time : 2020/2/15 16:37
# @Author : zhu
# @FileName: day13_浅拷贝.py
# @Software: PyCharm

from copy import copy

# 1.顶层可变，子元素全部不可变
a = [1, 'zhangsan', 3]
a1 = copy(a)

print(id(a))
print(id(a1))

print('-' * 50)

a[1] = 10
print(a)
print(a1)

# 2.顶层可变，子元素存在可变元素
b = [1, 2, [3]]
b1 = copy(b)

print(id(b))
print(id(b1))

b[2] = 1
print(b)
print(b1)

