# -*- coding: utf-8 -*-
# @Time : 2020/2/11 12:00
# @Author : zhu
# @FileName: day10_手动抛出异常.py
# @Software: PyCharm

ex = Exception("输入的密码长度不正确")

try:
    password = input("请输入不低于8位数的密码:")
    if len(password) < 8:
        raise ex
except Exception as e:
    print(e)