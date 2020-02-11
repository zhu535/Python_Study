# -*- coding: utf-8 -*-
# @Time : 2020/2/11 12:04
# @Author : zhu
# @FileName: day10_自定义异常类.py
# @Software: PyCharm

class DemoError(Exception):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "输入的密码长度不正确"


try:
    obj = DemoError("张三", 18)
    raise obj
except DemoError as e:
    print(e)
    print(e.name)
    print(e.age)