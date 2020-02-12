# -*- coding: utf-8 -*-
# @Time : 2020/2/12 17:38
# @Author : zhu
# @FileName: day11_文件操作案例.py
# @Software: PyCharm

"""
写一个十万行的文件，每行写一个随机数，随机范围为 1 - 100
data.txt 文件名字
"""
"""
import random

with open("data.txt", mode="a", encoding="utf-8") as f:
    for i in range(100000):
        f.write(str(random.randint(1, 100)) + "\n")
        """


"""
写mostNum.txt目的是提取出data.txt中出现频率最高的10个单词
"""

with open("data.txt", mode="r", encoding="utf-8") as f:
    l = f.readlines()

    dict = {}

    for s in l:
        num = int(s.strip())
        dict[num] = dict.get(num, 0) + 1

    li = list(dict.items())
    li.sort(key= lambda x : x[1],reverse= True)

    print(li)