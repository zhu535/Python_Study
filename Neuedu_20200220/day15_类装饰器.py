# -*- coding: utf-8 -*-
# @Time : 2020/2/21 10:50
# @Author : zhu
# @FileName: day15_类装饰器.py
# @Software: PyCharm

class A():

    def __init__(self,func):
        print("我是装饰的过程")
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func()

@A              # func = A(func)
def func():
    print("我是被装饰的函数")

func()