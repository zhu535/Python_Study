# -*- coding: utf-8 -*-
# @Time : 2020/2/17 13:05
# @Author : zhu
# @FileName: day14_正则语法.py
# @Software: PyCharm

import re

s = "我是好人，你是坏人，他不是\n人"

# 单字符匹配: . 可以代表任何字符，除了\n换行符
ret = re.findall("是.人", s)
print(ret)


# 匹配所有的数字 \d
s1 = "我吃饭吃了100次"
ret1 = re.search("\d+次", s1)
print(ret1)     # <re.Match object; span=(5, 9), match='100次'>


# 匹配所有的非数字 \D
s2 = "我吃饭吃了n次"
ret2 = re.search("\D次", s2)
print(ret2)     # <re.Match object; span=(5, 7), match='n次'>


# 匹配一个单词字符，即所有的字母，数字和下划线(python3中汉字也是单词字符)
ret3 = re.search("\w次", s2)
print(ret3)     # <re.Match object; span=(5, 7), match='n次'>

# 匹配非单词字符， \W
s3 = "我吃饭吃了#次"
ret4 = re.search("\W次", s3)
print(ret4)     # <re.Match object; span=(5, 7), match='#次'>

# 匹配所有的空白符 \s


# []是匹配中括号内随意一个,^放在前面是非的意思
name = "我叫朱a钊"

ret5 = re.search("朱[a-zA-Z0-9]钊", name)
print(ret5)