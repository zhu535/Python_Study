# -*- coding: utf-8 -*-
# @Time : 2020/2/14 17:59
# @Author : zhu
# @FileName: day12_序列化pickle模块.py
# @Software: PyCharm

import pickle

l = [1, 2, 3]

# 序列化： 对象 ----> 二进制
b = pickle.dumps(l)
print(b)    # b'\x80\x03]q\x00(K\x01K\x02K\x03e.'

# 反序列化： 二进制 ----> 对象
obj = pickle.loads(b'\x80\x03]q\x00(K\x01K\x02K\x03e.')
print(obj)