# -*- coding: utf-8 -*-
# @Time : 2020/2/20 16:11
# @Author : zhu
# @FileName: day15_函数内部函数不可以使用外部循环变量.py
# @Software: PyCharm

def outter():

    fs = []

    for i in range(1, 4):
        def inner():
            return i * i

        fs.append(inner)

    return fs


func = outter()
f1,f2,f3 = func
print(f1())     # 9
print(f2())     # 9
print(f3())     # 9


def outter():

    fs = []

    def inner(j):
        return lambda :j * j

    for i in range(1, 4):
        fs.append(inner(i))

    return fs

func = outter()
f1,f2,f3 = func
print(f1())     # 1
print(f2())     # 4
print(f3())     # 9