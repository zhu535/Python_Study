# -*- coding: utf-8 -*-
# @Time : 2020/2/1 16:26
# @Author : zhu
# @FileName: day07_函数案例.py
# @Software: PyCharm

"""
定义一个函数
    要求传入的参数为键盘 a-1 之间的字母
    函数接收到参数判断字母在这个范围就打印此字母在键盘上对应的上边的字母，不在此范围内就打印出输入字母错误
    例如：a --> q , s --> w , .... , l --> o
"""

dict = {"a":"q", "s":"w", "d":"e", "f":"r", "g":"t", "h":"y", "j":"u", "k":"i", "l":"o", }

def func(letter):
    if letter in dict.keys():
        print(dict[letter])
    else:
        print("输入字母错误")

letter = input("请输入一个字母：")
func(letter)