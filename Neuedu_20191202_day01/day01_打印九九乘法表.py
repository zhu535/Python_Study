#! \hp\PycharmProjects\Python_Workspace
# -*- coding:utf-8 -*-
# project:
# user:hp
# Author: zhu
# Date: 2019/12/2 15:42

row = 1

while row < 10:

    col = 1

    while col <= row:
        print("%d x %d = %d" % (row, col, row * col), end="\t")
        col += 1

    print("")
    row += 1
