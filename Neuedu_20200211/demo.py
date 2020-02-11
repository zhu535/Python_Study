# -*- coding: utf-8 -*-
# @Time : 2020/2/11 14:00
# @Author : zhu
# @FileName: demo.py
# @Software: PyCharm

print("demo开始")

__all__ = ["func1", "func2"]
# __all__ 被列表赋值，用来限制被导入的函数，只有列表内的函数才可以被导入
# __all__ 只能限制 from 模块名 import * 的使用


def func1():
    print("demo1")

def func2():
    print("demo2")

def func3():
    print("demo3")

def func4():
    print("demo4")

if __name__ == "__main__":
    print("我是demo文件")

print("demo结束")