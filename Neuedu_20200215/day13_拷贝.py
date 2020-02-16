# -*- coding: utf-8 -*-
# @Time : 2020/2/15 15:48
# @Author : zhu
# @FileName: day13_拷贝.py
# @Software: PyCharm

import copy

a = [1, 2, [3]]
# 浅拷贝：顶层拷贝
b = copy.copy(a)
print(id(a))    # 2212362228168
print(id(b))    # 2212362384840

print(id(a[2]))     # 2212362307528
print(id(b[2]))     # 2212362307528


print("-" * 50)
# 深拷贝：递归拷贝

c = copy.deepcopy(a)
print(id(a))    # 2116190900616
print(id(c))    # 2116191069256

print(id(a[2]))     # 2116190979912
print(id(c[2]))     # 2116191069576