# -*- coding: utf-8 -*-
# @Time : 2020/2/8 12:03
# @Author : zhu
# @FileName: day09_类方法.py
# @Software: PyCharm

# 类方法实则用来修改类属性的方法
# 实例方法无法被类对象访问

class A:
    type = "龙"

    def eat(self):
        print("吃")

    # 定义类方法，需要使用装饰器去装饰方法classmethod
    @classmethod
    def run(cls):
        print("跑")

    @classmethod
    def set_type(cls, type):
        cls.type = type

a = A()

a.eat() # 由于实例方法中传入了self参数，即实例对象本身。
# A.eat() # eat() missing 1 required positional argument: 'self'

# run()是类方法
a.run()
A.run()

# 无论使用类对象还是实例对象来调用类方法实则都是在修改类
A.set_type("肥龙")
print(A.type)   # 肥龙
print(a.type)   # 肥龙

a.set_type("瘦龙")
print(A.type)   # 瘦龙
print(a.type)   # 瘦龙