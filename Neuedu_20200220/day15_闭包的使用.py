# -*- coding: utf-8 -*-
# @Time : 2020/2/20 16:42
# @Author : zhu
# @FileName: day15_闭包的使用.py
# @Software: PyCharm

# 已完成的功能：支付 在不修改原本的功能下新增验证功能

def pay_func():
    print("支付功能")

def outter(func):

    def inner():
        print("验证功能")
        func()

    return inner

func = outter(pay_func)
func()