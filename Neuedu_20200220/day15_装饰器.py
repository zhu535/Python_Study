# -*- coding: utf-8 -*-
# @Time : 2020/2/20 16:17
# @Author : zhu
# @FileName: day15_装饰器.py
# @Software: PyCharm

def outter(func):

    def inner():
        print("验证功能")
        func()

    return inner

@outter  # func = outter(pay_func)
def pay_func():
    print("支付功能")

pay_func()