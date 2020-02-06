# -*- coding: utf-8 -*-
# @Time : 2020/2/6 15:53
# @Author : zhu
# @FileName: day08_私有属性.py
# @Software: PyCharm

class Girl:

    def __init__(self, name, age, weight):
        self.name = name
        # 私有属性就是在属性前加两个底杠
        self.__age = age
        self.__weight = weight

    def run(self):
        print("喜欢逛街")

    def eat(self):
        print("我胃特别大，吃不饱")

    def get_age(self):
        print("我的年龄是%s" % self.__age)

    def get_weight(self):
        print("我的体重是%s" % self.__weight)

    def set_weight(self, weight):
        self.__weight = weight

girl1 = Girl("小美", 18, 99)

# 设置为私有属性以后，在类的外部就不能直接访问私有属性，只能使用类内部定义的方法来访问
girl1.get_age()

girl1.set_weight(100)

girl1.get_weight()