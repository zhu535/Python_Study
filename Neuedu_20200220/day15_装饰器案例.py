# -*- coding: utf-8 -*-
# @Time : 2020/2/21 11:02
# @Author : zhu
# @FileName: day15_装饰器案例.py
# @Software: PyCharm
import time

def outter(func):

    def inner(num):
        time1 = time.time()
        ret = func(num)
        time2 = time.time()
        t = time2 - time1
        print("程序耗时：%.2f秒" %t)
        return ret
    return inner

@outter   # func = outter(func)
def func(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum

result = func(1000000)
print(result)