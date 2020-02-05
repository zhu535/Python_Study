# -*- coding: utf-8 -*-
# @Time : 2020/2/3 17:52
# @Author : zhu
# @FileName: day08_定义类.py
# @Software: PyCharm

class Person:

    def eat(self):
        print("吃")

    def print_name(self):
        print(self.name)

zhangsan = Person()
zhangsan.eat()

lisi = Person()
lisi.eat()

zhangsan.name = "张三"
lisi.name = "李四"

zhangsan.print_name()
lisi.print_name()