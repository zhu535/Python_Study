# -*- coding: utf-8 -*-
# @Time : 2020/2/20 18:38
# @Author : zhu
# @FileName: day15_带参数没返回值的装饰器.py
# @Software: PyCharm

def outter(func):

    def inner(num):
        print("验证功能")
        func(num)

    return inner

@outter  # func = outter(pay_func)
def pay_func(num):
    print("支付功能%s" %num)

pay_func(10)