# -*- coding: utf-8 -*-
# @Time : 2020/2/5 16:54
# @Author : zhu
# @FileName: day08_ __init__方法的使用.py
# @Software: PyCharm

class Person():

    def __init__(self, name, age):
        # 相当于java中的构造函数
        print("自动调用")
        self.name = name
        self.age = age

    def eat(self):
        print("%s在吃饭" % self.name)

    def drink(self):
        print("%s在喝水" % self.name)

    def __str__(self):
        # 相当于java中的toString
        s = "%s的年龄是%s" % (self.name, self.age)
        return s

zhangsan = Person("张三", 24) # 自动调用
print(zhangsan.name)
zhangsan.eat()
print(zhangsan)