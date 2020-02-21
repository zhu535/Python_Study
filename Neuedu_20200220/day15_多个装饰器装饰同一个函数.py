# -*- coding: utf-8 -*-
# @Time : 2020/2/21 0:25
# @Author : zhu
# @FileName: day15_多个装饰器装饰同一个函数.py
# @Software: PyCharm

def outter1(func):
    print("我是outter1")
    def inner():
        print("我是inner1")
        func()
    return inner

def outter2(func):
    print("我是outter2")
    def inner():
        print("我是inner2")
        func()
    return inner

@outter1
@outter2
def func():
    print("我是方法")

func()