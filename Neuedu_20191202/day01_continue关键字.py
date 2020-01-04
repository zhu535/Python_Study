#! \hp\PycharmProjects\Python_Workspace
# -*- coding:utf-8 -*-
# project:
# user:hp
# Author: zhu
# Date: 2019/12/2 15:37

i = 0

while i < 10:

    if i == 5:
        i += 1
        continue   # continue关键字的作用是跳过本次循环

    print(i)

    i += 1