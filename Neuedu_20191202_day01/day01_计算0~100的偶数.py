#! \hp\PycharmProjects\Python_Workspace
# -*- coding:utf-8 -*-
# project:
# user:hp
# Author: zhu
# Date: 2019/12/2 15:20

i = 0

result = 0

while i <= 100:

    if i % 2 == 0:
        result += i

    i += 1

print("0~100之间的偶数相加的结果是：%d" % result)