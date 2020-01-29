# -*- coding: utf-8 -*-
# @Time : 2020/1/29 21:00
# @Author : zhu
# @FileName: day07_函数返回值的进阶.py
# @Software: PyCharm


def func():
    return "张三", "李四", [1, 2, 3]


name = func()
print(name)     # ('张三', '李四', [1, 2, 3])
print(type(name))   # <class 'tuple'>
# return 后面返回多个值，用 , 分隔。函数返回元组,可进行拆包、遍历等操作

a, b, c = name
print(a, b, c)  # 张三 李四 [1, 2, 3]