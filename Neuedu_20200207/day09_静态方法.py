# -*- coding: utf-8 -*-
# @Time : 2020/2/8 15:20
# @Author : zhu
# @FileName: day09_静态方法.py
# @Software: PyCharm

# 静态方法是定义的时候不想传入参数时候使用的，实际可以传参数
class A:

    @staticmethod
    def eat(name):
        print(name, "吃")

a = A()
a.eat("张三")
A.eat("李四")