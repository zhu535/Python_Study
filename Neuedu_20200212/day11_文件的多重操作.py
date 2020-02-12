# -*- coding: utf-8 -*-
# @Time : 2020/2/12 16:21
# @Author : zhu
# @FileName: day11_文件的多重操作.py
# @Software: PyCharm

# r+ 可读可写，文件不存在的时候会报错
"""
with open("data.txt", mode="r+", encoding="utf-8") as f:
    print("1", f.read())
    f.write("zhu")
    print("2", f.read())
"""

# w+ 可读可写，文件存在的时候清空，不存在的时候创建文件
"""
with open("data.txt", mode="w+", encoding="utf-8") as f:
    print("1", f.read())
    f.write("zhu")
    # f.seek(0, 0) 光标回到开始位置
    # 第一个参数控制光标偏移量，正数右移动，负数左移动(只有在b模式下可以使用)
    # 第二个参数控制光标的位置，0就是开始位置，1就是光标现在的位置，2就是结束的位置
    f.seek(0, 0)
    print("2", f.read())
"""

# a+ 可读可追加，文件存在的时候就打开文件追加，不存在的时候创建文件
# a模式打开光标所在的位置在末尾
# 追加模式可以先读取全部文件，再进行追加
with open("data.txt", mode="a+", encoding="utf-8") as f:
    f.seek(0, 0)
    text = f.read()
    print(text)
    f.write("170535")