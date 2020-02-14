# -*- coding: utf-8 -*-
# @Time : 2020/2/14 17:16
# @Author : zhu
# @FileName: day12_collections中的deque类.py
# @Software: PyCharm

"""
5.3 deque队列就是一个可以两头操作的容器，类似list但比列表速度更快
        d = deque()maxlen参数指定最大长度
        append右侧添加,appendleft左侧添加,pop右侧删除,popleft左侧删除,extend由此合并,extendleft左侧合并
"""

from collections import deque

d = deque([1, 2, 3], maxlen=9)

d.append(1)
d.appendleft(2)
d.append(3)

print(d.pop())
print(d.popleft())

l = [2, 3, 4]
d.extend(l)
print(d)