# -*- coding: utf-8 -*-
# @Time : 2020/2/12 16:04
# @Author : zhu
# @FileName: day11_二进制文件的操作.py
# @Software: PyCharm

# rb 只读的形式打开二进制文件
# wb 只写的形式打开二进制文件
# ab 追加的形式打开二进制文件

with open("demo.png", mode="rb") as f:
    b = f.read()

with open("随便.png", mode="wb") as f:
    f.write(b)