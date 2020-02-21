# -*- coding: utf-8 -*-
# @Time : 2020/2/20 15:42
# @Author : zhu
# @FileName: day15_闭包.py
# @Software: PyCharm

def outter():
    num = 1
    def inner():
        print(num)
    return inner

func = outter()
func()