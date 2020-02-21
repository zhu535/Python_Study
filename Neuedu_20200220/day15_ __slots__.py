# -*- coding: utf-8 -*-
# @Time : 2020/2/20 10:27
# @Author : zhu
# @FileName: day15_ __slots__.py
# @Software: PyCharm

# __slots__用来限制实例的属性，即不允许自己添加属性
class A:

    __slots__ = ("name", "age", "sex")

    def __init__(self):
        self.name = '张三'
        self.age = 18

a = A()
print(a.name)
print(a.age)
a.sex = "男"
print(a.sex)

# a.num = 10  error

# 继承不会继承__slots__
class B(A):
    pass

b = B()
b.num = 5
print(b.num)    # 5