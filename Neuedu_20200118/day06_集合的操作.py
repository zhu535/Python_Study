# -*- coding: utf-8 -*-
# @Time : 2020/1/18 16:01
# @Author : zhu
# @FileName: day06_集合的操作.py
# @Software: PyCharm

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {1, 2, 3, 4}

# 并集
s = s1 | s2
print(s)    # {1, 2, 3, 4, 5}

# 交集
s = s1 & s2
print(s)    # {3}

# 差集
s = s3 - s1
print(s)    # {4}

# 子集,True为子集，False不为子集
s = s1 < s2
print(s)    # False
