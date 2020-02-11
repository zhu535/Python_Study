# -*- coding: utf-8 -*-
# @Time : 2020/2/11 11:46
# @Author : zhu
# @FileName: day10_异常的传递.py
# @Software: PyCharm

"""
num = 0
if num == 0:
    try:
        print(1 / 0)
    except:
        print("报错")
else:
    print("随便")
"""

num = 0
try:
    if num == 0:
        print(1 / 0)
    else:
        print("随便")
except:
    print("报错")