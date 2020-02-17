# -*- coding: utf-8 -*-
# @Time : 2020/2/17 23:19
# @Author : zhu
# @FileName: day14_贪婪与非贪婪.py
# @Software: PyCharm

import re

url = 'url = https://rpic.douyucdn.cn/asrpic/200217/12821_2316.png/dy1","rs1":"https://rpic.douyucdn.cn/asrpic/200217/12821_2316.png/dy2""'

ret = re.search("https.*png", url)
print(ret.group())

# 非贪婪就是在原本贪婪的符合后加一个问号

"""
* 匹配0-无限个
*? 匹配0个-最少次数个

? 匹配0-1个
?? 匹配0个

+ 匹配1-无穷个
+? 匹配1个-最少次数个

{n,m} 匹配n-m个
{n,m}? 匹配n个

"""