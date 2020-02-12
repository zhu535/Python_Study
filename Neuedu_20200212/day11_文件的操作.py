# -*- coding: utf-8 -*-
# @Time : 2020/2/12 14:54
# @Author : zhu
# @FileName: day11_文件的操作.py
# @Software: PyCharm

"""
文件操作的步骤：
    1、打开文件 open()
    2、操作文件
    3、关闭文件 close()

    读模式：r
    写模式（使用这个模式打开文件，会立即清空文件内容 / 当文件不存在，则创建这个文件 / 只能写入字符串）：w
    追加模式（原文件的内容不删除 / 当文件不存在，则创建这个文件）：a
"""

# 1、打开文件open，打开文件的时候会返回文件的对象
f = open("data.txt", mode="r")

# 2、操作文件
text = f.read()

f.write("data")

# 3、关闭文件
f.close()