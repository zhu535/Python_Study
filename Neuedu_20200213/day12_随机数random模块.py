# -*- coding: utf-8 -*-
# @Time : 2020/2/14 12:23
# @Author : zhu
# @FileName: day12_随机数random模块.py
# @Software: PyCharm

import random

# 随机一个整数
print(random.randint(1, 10))

# 随机一个浮点数(0-1区间)
print(random.random())

# 从数据集合里随机获取一个数据(列表、元组、集合、字典)
l = [1, 2, 3, 4, 5]
num = random.choice(l)
print(num)

# choices()里面加入参数权重
num2 = random.choices(l, [1, 1, 1, 1, 96])
print(num2)

# random.sample(population, k),在一个序列或者集合中选择k个随机元素,返回由K个元素组成新的列表(k的值小于population的长度)
l2 = random.sample(l, 2)
print(l2)

# random.uniform(a, b)产生一个指定范围内的随机浮点数 若a < b，随机数n范围a <= n <= b若a > b随机数n范围a<= n <= b
f2 = random.uniform(1, 10)
print(f2)

# random.randrange(start, stop=None, step=1, _int=)在rang(start, stop,step)中选择一个随机数(左闭右开区间)
# 取1-100之间的基数
num3 = random.randrange(1, 100, 2)
print(num3)

# random.shuffle(x, random=None)：将列表顺序打乱(直接在原列表中进行)
random.shuffle(l)