# -*- coding: utf-8 -*-
# @Time : 2020/2/6 16:33
# @Author : zhu
# @FileName: day08_propert的使用.py
# @Software: PyCharm

"""
class Girl:

    def __init__(self, weight):
        self.__weight = weight

    def get_weight(self):
        print("我的体重是%s" % self.__weight)

    def set_weight(self, weight):
        self.__weight = weight

    p = property(get_weight, set_weight)

xiaohua = Girl(50)

xiaohua.p   # 我的体重是50
xiaohua.p = 40
xiaohua.p   # 我的体重是40
"""

class Girl:

    def __init__(self, weight):
        self.__weight = weight

    @ property
    def weight(self):
        print("我的体重是%s" % self.__weight)

    @ weight.setter
    def weight(self, weight):
        self.__weight = weight


xiaohua = Girl(50)

xiaohua.weight  # 我的体重是50
xiaohua.weight = 40
xiaohua.weight  # 我的体重是40
