# -*- coding: utf-8 -*-
# @Time : 2020/2/8 11:39
# @Author : zhu
# @FileName: day09_类属性的应用场景.py
# @Software: PyCharm

class Class:
    num = 0

    def __init__(self):
        # 使用类名.类属性可以访问类属性
        Class.num += 1
        print(f"我是python{self.num}班")

for i in range(10):
    cls = Class()
