#! \hp\PycharmProjects\Python_Workspace
# -*- coding:utf-8 -*-
# project:
# user:hp
# Author: zhu
# Date: 2019/12/2 16:08

row = 1

while row <= 5:

    col = 1

    while col <= row:
        print("*", end="")
        col += 1

    row += 1
    print("")