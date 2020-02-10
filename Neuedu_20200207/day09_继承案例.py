# -*- coding: utf-8 -*-
# @Time : 2020/2/9 20:35
# @Author : zhu
# @FileName: day09_继承案例.py
# @Software: PyCharm

import math

class Shape(object):

    def __init__(self, color):
        self.color = color

    # 获取颜色的方法
    def get_color(self):
        return self.color

class Circle(Shape):

    def __init__(self, color, r):
        super().__init__(color)
        self.r = r

    # 获取颜色的方法
    def get_color(self):
        return self.color

    # 获取面积的方法
    def get_area(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):

    def __init__(self, color, width, length):
        super().__init__(color)
        self.width = width
        self.length = length

    # 获取颜色的方法
    def get_color(self):
        return self.color

    # 获取面积的方法
    def get_area(self):
        return self.width * self.length


circle = Circle("yellow", 10)
rectangle = Rectangle("red", 5, 10)

print(circle.get_area())
print(rectangle.get_area())