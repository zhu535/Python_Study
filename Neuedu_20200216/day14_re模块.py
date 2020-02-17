# -*- coding: utf-8 -*-
# @Time : 2020/2/16 17:50
# @Author : zhu
# @FileName: day14_re模块.py
# @Software: PyCharm

import re

s = "我喜欢吃火锅我喜欢吃火锅"

# match方法:从开头匹配，如果存在相同的字符串则返回一个match对象，没有则返回None
ret = re.match("我喜欢", s)
print(ret)   # <re.Match object; span=(0, 3), match='我喜欢'>
print(ret.group())  # 我喜欢


# search方法:如果存在相同的字符串则返回一个match对象，没有则返回None
ret1 = re.search("火锅", s)
print(ret1)  # <re.Match object; span=(4, 6), match='火锅'>
print(ret.group())  # 我喜欢


# findall:匹配全部符合规则的，返回一个列表，列表内部放着全部符合规则的字符串
ret2 = re.findall("火锅", s)
print(ret2)    # ['火锅', '火锅']


# findall:匹配全部符合规则的，返回一个迭代器，迭代器里面装着符合规则的match对象
ret3 = re.finditer("火锅", s)
for i in ret3:
    print(i)    # <re.Match object; span=(4, 6), match='火锅'> <re.Match object; span=(10, 12), match='火锅'>


# 正则表达式
s1 = "asdf zxcv,  afed; fjek,  foo"
ret4 = re.split("[\s,;]\s*", s1)
print(ret4)

s2 = "我吃饭吃了100次，喝汤喝了50次"
def func(match):
    return str(int(match.group()) + 1)
ret4 = re.sub("\d+", func, s2)
print(ret4)