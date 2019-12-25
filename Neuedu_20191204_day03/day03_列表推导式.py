#! \hp\PycharmProjects\Python_Workspace
# -*- coding:utf-8 -*-
# project:
# user:hp
# Author: zhu
# Date: 2019/12/25 14:38

# 列表推导式：[元素 元素的表达式 (条件判断)]

# 1、生成一个1-9的列表
aList = []
for i in range(1, 10):
    aList.append(i)
print("aList:", aList)

# 列表推导式-------->

bList = [i for i in range(1, 10)]
print("bList:", bList)

# 2、现有列表[[1, 2, 3], [4, 5, 6], [7, 8, 9]]如果拆解成为1-9的列表？
cList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
dList = []
for i in cList:
    for j in i:
        dList.append(j)
print("dList:", dList)

# 列表推导式-------->

eList = [j for i in cList for j in i]
print("eList:", eList)

# 3、列表中有正数和负数，现在只想要取其中的正数，如果过滤掉负数？
a_list = [-1, -4, 5, 10, -7, 9, -11]
b_list = []
for i in a_list:
    if i >= 0:
        b_list.append(i)
print("b_list:", b_list)

# 列表推导式-------->

c_list = [i for i in a_list if i >= 0]
print("c_list:", c_list)
