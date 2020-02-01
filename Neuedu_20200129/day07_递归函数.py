# -*- coding: utf-8 -*-
# @Time : 2020/2/1 12:21
# @Author : zhu
# @FileName: day07_递归函数.py
# @Software: PyCharm

# 递归函数就是函数自己调用自己，但是要有明确的return条件
# 输入一个数字，求1到此数字的累加和
"""
    def func(num):
        sum = 0
        for i in range(num + 1):
            sum += i
        return sum


    num = int(input("请输入一个数字:"))
    sum = func(num)
    print("结果为：%s" % sum)
"""

# 使用递归函数改进
def func(num):
    if num == 0:
        return num
    else:
        return num + func(num-1)

num = int(input("请输入一个数字:"))
sum = func(num)
print("结果为：%s" % sum)