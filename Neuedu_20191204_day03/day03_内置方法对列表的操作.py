#! \hp\PycharmProjects\Python_Workspace
# -*- coding:utf-8 -*-
# project:
# user:hp
# Author: zhu
# Date: 2019/12/25 14:22

name_list = ["张三", "李四", "王五", "张三"]
number_list = [6, 8, 1, 4, 10]

# len()方法获取列表的长度哈哈
list_len = len(name_list)
print("列表的长度为%d" % list_len)

# 内置方法sorted（过去式），不会修改原列表
new_numberList = sorted(number_list)

# 内置方法reversed（过去式），不会修改原列表
new_nameList = reversed(name_list)

# max()、min()、sum()方法
print(max(number_list))  # 10
print(min(number_list))  # 1
print(sum(number_list))  # 29

# zip()方法返回可迭代的zip对象(观察结果生成元组，可发现使用zip方法两列表的个数必须相同)
aList = [1, 2, 3, 4]
bList = [5, 6, 7, 8]
cList = zip(aList, bList)
print(list(cList))  # [(1, 5), (2, 6), (3, 7), (4, 8)]

# enumerate()：枚举列表返回元组，第一个元素是索引，第二个元素是列表内的元素
for item in enumerate(name_list):
    print(item)
