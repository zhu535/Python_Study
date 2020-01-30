# -*- coding: utf-8 -*-
# @Time : 2020/1/30 22:50
# @Author : zhu
# @FileName: day07_局部作用域修改全局变量.py
# @Software: PyCharm

a = 1


# 在局部作用域内进行声明，提前说好，局部作用域可以去修改全局变量
# global 变量名(是要被修改的全局变量)
def func():
    global a
    a += 1
    print("内部a:", a)


func()
print("外部a:", a)