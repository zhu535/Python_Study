# -*- coding: utf-8 -*-
# @Time : 2020/1/18 15:53
# @Author : zhu
# @FileName: day06_集合的增删改查.py
# @Software: PyCharm

s1 = {"张三", "李四", "李四"}

# .add()方法,增加相同元素集合不变
s1.add("王五")
print(s1)

# .pop()方法，随机删除集合一个元素并返回
n = s1.pop()
print(s1)
print(n)

# .remove()方法，用于删除指定元素
s1.remove("李四")
print(s1)

# .clear()清空
s1.clear()
print(s1)

