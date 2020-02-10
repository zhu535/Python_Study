# -*- coding: utf-8 -*-
# @Time : 2020/2/9 12:52
# @Author : zhu
# @FileName: day09_继承.py
# @Software: PyCharm

class A(object):
    type = "人"

    def __init__(self, name):
        self.__name = name

    @property
    def Name(self):
        print(self.__name)

    @Name.setter
    def Name(self, name):
        self.name = name

    @classmethod
    def flow(cls):
        print("classMethod")

    @staticmethod
    def eat():
        print("吃")

    def drink(self):
        print("Staticmethod")


class B(A):

    def drink(self):
        super().drink()
        print("Staticmethod2")

a = A("zhangsan")
b = B("lisi")

print(a.type)
print(b.type)
a.Name
a.eat()
b.eat()
b.flow()
b.drink()