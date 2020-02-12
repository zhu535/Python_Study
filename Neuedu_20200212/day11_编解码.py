# -*- coding: utf-8 -*-
# @Time : 2020/2/12 11:49
# @Author : zhu
# @FileName: day11_编解码.py
# @Software: PyCharm

str = "东软睿道"
print(type(str))    # <class 'str'> 字符串是人类能读懂的文字，计算机不能识别，计算机只能识别二进制的文字

b = str.encode()

print(b)    # b'\xe4\xb8\x9c\xe8\xbd\xaf\xe7\x9d\xbf\xe9\x81\x93'

b2 = b'\xe4\xb8\x9c\xe8\xbd\xaf\xe7\x9d\xbf\xe9\x81\x93'

str2 = b2.decode("utf-8")
str3 = b2.decode("gbk")

print(str2) # 东软睿道
print(str3) # 涓滆蒋鐫块亾