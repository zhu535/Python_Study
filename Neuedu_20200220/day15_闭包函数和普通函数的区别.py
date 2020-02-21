# -*- coding: utf-8 -*-
# @Time : 2020/2/20 16:00
# @Author : zhu
# @FileName: day15_闭包函数和普通函数的区别.py
# @Software: PyCharm

def outter(num):
    num = num

    def inner():
        nonlocal num
        num += 1
        print(num)

    return inner

func = outter(100)
func()
func()