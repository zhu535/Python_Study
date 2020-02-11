# -*- coding: utf-8 -*-
# @Time : 2020/2/11 10:59
# @Author : zhu
# @FileName: day10_异常.py
# @Software: PyCharm

# 异常：程序出现了错误，导致程序停止执行，并且提示错误

"""
try:
    print(1 / 1)
except ZeroDivisionError:
    print("分母不能为0")
except NameError:
    print("变量名错误")
else:
    print("没报错我就执行")
finally:
    print("我不管你报不报错，程序都会执行")
"""

try:
    print(1 / 0)
except Exception as e:
    print(e)    # division by zero  # e 保存异常的错误详细信息