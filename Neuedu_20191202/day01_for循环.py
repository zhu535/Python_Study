#! \hp\PycharmProjects\Python_Workspace
# -*- coding:utf-8 -*-
# project:
# user:hp
# Author: zhu
# Date: 2019/12/25 11:29

# for循环实际上是遍历数据，遍历是将数据一个一个从集合中取出来

# 可以遍历非数字的数据类型
for i in "abcde":
    print(i)

# range(),需要接受两个参数，一个最小值一个最大值，是一种可迭代对象，不是任何数据类型
# 如果只传入一个参数，则最小值默认为0
# range()是一个左闭右开的区间
for i in range(0, 10):
    print(i)

# 练习题：输入一个数字，计算出从1到该数字之和
num = int(input("请输入一个数字"))
s = 0

for i in range(num+1):
    s += i

print("和为：%d" % s)


