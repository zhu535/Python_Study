# -*- coding: utf-8 -*-
# @Time : 2020/2/2 15:47
# @Author : zhu
# @FileName: day08_map函数.py
# @Software: PyCharm

def func(num):
    num += 1
    return num

l = [1, 2, 3, 4, 5]

"""
ll = []

for i in l:
    ll.append(func(i))

print(ll)   # [2, 3, 4, 5, 6]
"""

ll = map(func, l)
print(list(ll))  # [2, 3, 4, 5, 6]

# map返回可迭代对象
for i in ll:
    print(i)


# 求列表[1, 2, 3, 4, 5, 6, 7, 8, 9],返回一个n*n的列表
def mult(num):
    num = num * num
    return num

l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

l3 = map(mult, l2)
print(list(l3))