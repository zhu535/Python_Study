# -*- coding: utf-8 -*-
# @Time : 2020/2/8 11:17
# @Author : zhu
# @FileName: day09_类属性.py
# @Software: PyCharm

class Person:
    # type是类属性
    type = "普通人"

    # name 是实例属性
    def __init__(self, name):
        self.name = name


zhangsan = Person("张三")

# 实例属性只能通过实例对象去访问
print(zhangsan.name)
# print(Person.name)  # type object 'Person' has no attribute 'name'

print(zhangsan.type)   # 普通人
print(Person.type)  # 普通人

# 如何修改类属性
Person.type = "超人"
print(zhangsan.type)   # 超人（变化）
print(Person.type)  # 超人（变化）

# 给实例对象添加了一个实例属性，当实例属性和类属性变量名相同时，会自动屏蔽类属性
zhangsan.type = "钢铁侠"
print(zhangsan.type)   # 钢铁侠（变化）
print(Person.type)  # 超人（没变化）
