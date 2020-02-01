# -*- coding: utf-8 -*-
# @Time : 2020/2/1 12:12
# @Author : zhu
# @FileName: day07_父级作用域变量的修改.py
# @Software: PyCharm


def func():
    a = 1
    print("父级", a)  # 父级 1

    def func1():
        # 子级作用域可以使用父级作用域的变量
        # 子级优先级 > 父级
        nonlocal a  # 声明后去父级作用域中找a
        a = a + 1
        print("子级", a)  # 子级 2

    return func1()


func()
