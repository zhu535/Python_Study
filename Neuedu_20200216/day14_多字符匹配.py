# -*- coding: utf-8 -*-
# @Time : 2020/2/17 13:34
# @Author : zhu
# @FileName: day14_多字符匹配.py
# @Software: PyCharm
import re

s = "我的电话是18922025720"
# * 指定字符匹配0 - 无限次
ret = re.search("是\d*", s)
print(ret)      # <re.Match object; span=(4, 16), match='是18922025720'>

# + 指定字符匹配1 - 无限次
ret1 = re.search("\d+", s)
print(ret1)     # <re.Match object; span=(5, 16), match='18922025720'>

# ? 指定字符出现0 或 1次
ret2 = re.search("\d?", s)
print(ret2)     # <re.Match object; span=(0, 0), match=''>

ret3 = re.search("是\d?", s)
print(ret3)     # <re.Match object; span=(4, 6), match='是1'>

# {m} 指定字符出现m次 ----- {n, m} 指定字符出现 n - m 次
s1 = "0750-88888888"
s2 = "020-88888888"

ret4 = re.search("0\d{2,3}-\d{8}", s1)
ret5 = re.search("0\d{2,3}-\d{8}", s2)
print(ret4)     # <re.Match object; span=(0, 13), match='0750-88888888'>
print(ret5)     # <re.Match object; span=(0, 12), match='020-88888888'>