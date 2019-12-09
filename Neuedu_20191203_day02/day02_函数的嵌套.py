#! \hp\PycharmProjects\Python_Workspace
# -*- coding:utf-8 -*-
# project:
# user:hp
# Author: zhu
# Date: 2019/12/3 13:59


def print_line(char, times):

    print(char * times)


def print_lines(char, times):

    row = 0

    while row < 5:

        print_line(char, times)

        row += 1


print_lines("+", 10)