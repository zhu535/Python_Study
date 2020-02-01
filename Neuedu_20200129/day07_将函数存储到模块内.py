# -*- coding: utf-8 -*-
# @Time : 2020/2/1 17:01
# @Author : zhu
# @FileName: day07_将函数存储到模块内.py
# @Software: PyCharm

"""
import demo
demo.demo()
"""

# 可以给方法起别名，由于导入的方法可能与自己定义的方法名重名
# 关键字 as
# 当起别名的时候，使用原始的名称无法调用该方法
from demo import demo as test
test()

# 如何给.py文件起别名
# 关键字 as


