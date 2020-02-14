# -*- coding: utf-8 -*-
# @Time : 2020/2/14 16:49
# @Author : zhu
# @FileName: day12_collections中的Counter类.py
# @Software: PyCharm

from collections import Counter

l = [1, 2, 1, 3, 5, 2, 3, 1, 5, 7, 4, 2, 1]

print(dict(Counter(l))) # {1: 4, 2: 3, 3: 2, 5: 2, 7: 1, 4: 1}

