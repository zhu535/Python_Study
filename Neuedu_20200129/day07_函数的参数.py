# -*- coding: utf-8 -*-
# @Time : 2020/1/29 15:39
# @Author : zhu
# @FileName: day07_函数的参数.py
# @Software: PyCharm


# 1、必须参数（在调用时必须一一对应的关系传入）
def func(a):
    a += 1
    return a


# 1代表调用时传入的参数，统称为实参（实际存在的参数）
num = func(1)
print(num)

# 2.默认参数（次参数自身有默认值，如果在调用时不传入参数则使用默认值）
#            ,如果传入参数，则使用传入的值）默认参数在定义时给形参赋值


def func1(name, age, sex="男"):
    print("姓名：", name)
    print("年龄：", age)
    print("性别：", sex)


func1("zhu", 18)

# 关键字形式传入，Ctrl + p 可以查看函数需要的参数
func1(name="zhu", age=18, sex="男")

# 3.不定长参数（接受的参数的顺序不确定）
# 3.1 接收所有位置参数（非关键字参数）


# *args需要定义在必须参数之后，默认参数之前
def func2(a, *args, b=5):
    print(args)


func2(1, 2, 3, 4)   # (2, 3, 4) 封装成元组

# 3.2 接收所有关键字参数
# **变量名(kwargs)


# 定义函数时的参数顺序（必须参数，不定长参数（位置参数），默认参数，不定长参数（关键字参数））
def func3(**kwargs):
    print(kwargs)


func3(name="zhangsan", sex="lisi")  # {'name': 'zhangsan', 'sex': 'lisi'} 以字典的形式返回

