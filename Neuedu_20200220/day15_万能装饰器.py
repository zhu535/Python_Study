# -*- coding: utf-8 -*-
# @Time : 2020/2/21 0:01
# @Author : zhu
# @FileName: day15_万能装饰器.py
# @Software: PyCharm

def outter(func):
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        return ret
    return inner

@outter
def func(a,b,c=4,d=5):
    print(a)
    print(b)
    print(c)
    print(d)

func(1,2,c=5,d=6)

