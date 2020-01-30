# -*- coding: utf-8 -*-
# @Time : 2020/1/30 22:34
# @Author : zhu
# @FileName: day07_作用域.py
# @Software: PyCharm

# a,x 存在于全局作用域
a = 2
x = 5

a
# 局部作用域是函数或者类生成的
def func():
    a = a + 1  # 局部作用域不能修改全局作用域的变量


print(a)

