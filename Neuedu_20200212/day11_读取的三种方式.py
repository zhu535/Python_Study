# -*- coding: utf-8 -*-
# @Time : 2020/2/12 15:18
# @Author : zhu
# @FileName: day11_读取的三种方式.py
# @Software: PyCharm

# read() 默认全部读取，可以传入数字参数
f = open("data.txt", mode="r", encoding="utf-8")
print(f.read(4))    # data
f.close()

# readline() 默认读取一行
f = open("data.txt", mode="r", encoding="utf-8")
print(f.readline())    # data
f.close()

# readlines() 默认读取全部文本，但是会将每一行封装为一个元素，把全部元素封装为一个列表
f = open("data.txt", mode="r", encoding="utf-8")
print(f.readlines())    # ['data\n', '哈哈哈']
f.close()