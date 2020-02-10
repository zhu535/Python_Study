# -*- coding: utf-8 -*-
# @Time : 2020/2/10 10:52
# @Author : zhu
# @FileName: day09_ __new__方法实现单例模式.py
# @Software: PyCharm

"""
class A(object):

    def __new__(cls, *args, **kwargs):
        print("new")
        return super().__new__(cls)

    def __init__(self, name):
        print("init")
        self.name = name

a = A("张三")
b = A("李四")

print("a的id为：", id(a))  # 2345646516544
print("b的id为：", id(b))  # 2345646516600
"""

class A(object):

    id1 = None

    def __new__(cls, *args, **kwargs):
        if A.id1 is None:
            A.id1 = super().__new__(cls)
            return A.id1
        else:
            return A.id1

    def __init__(self, name):
        self.name = name

a = A("张三")
b = A("李四")

print("a的id为：", id(a))  # 1857829235064
print("b的id为：", id(b))  # 1857829235064