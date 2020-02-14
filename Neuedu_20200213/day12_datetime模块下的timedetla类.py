# -*- coding: utf-8 -*-
# @Time : 2020/2/13 16:38
# @Author : zhu
# @FileName: day12_datetime模块下的timedetla类.py
# @Software: PyCharm

import datetime

# 用来定义一个时间，用来做对时间的处理
dat = datetime.timedelta(1)

dat1 = datetime.datetime.now()
print(dat1)         # 2020-02-13 17:13:31.405518
print(dat1 - dat)   # 2020-02-12 17:13:31.405518