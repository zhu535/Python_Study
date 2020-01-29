# -*- coding: utf-8 -*-
# @Time : 2020/1/29 21:04
# @Author : zhu
# @FileName: day07_高阶函数.py
# @Software: PyCharm

# 高阶函数是至少满足下列一个条件的函数：
#       1.接收一个或多个函数作为输入输出一个函数


def func(a):
    a += 1
    return a


# 定义高阶函数
# 接收函数为参数
def g_func(a, b, f):    # a,b接收数字，f是接收函数
    return f(a) + f(b)


# 当需要以函数为参数时，只需要传入函数名 f --> func
num = g_func(1, 1, func)
print(num)
