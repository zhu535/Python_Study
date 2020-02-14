# -*- coding: utf-8 -*-
# @Time : 2020/2/12 21:12
# @Author : zhu
# @FileName: day12_datetime模块.py
# @Software: PyCharm

import datetime

# datetime下面有五个类

""" date类此类获取日期信息(通过此方法实例日期对象时必须传入年月日)"""
dat = datetime.date(year=2020, month=2, day=13)
print(type(dat))    # <class 'datetime.date'>

"""time()类此类获取时间信息(时分秒有默认值为0)"""
t = datetime.time(hour= 23, minute= 12, second=46)
print(type(t))  # <class 'datetime.time'>
print(t.hour)   # 23
print(t.minute) # 12
print(t.second) # 46

"""
    datetime.datetime()类
    1、类方法:
                today()获取今天的日期+时间
                now()获取当前的时间,和today()获取结果相同
                fromtimestamp()将时间戳转换为日期
                strptime()将字符串转化为时间对象
                注意 : 格式一定要对应
            
    2、实例方法:
                date()获取日期
                time()获取时间
                replace()替换时间日期信息
                timestamp()将日期信息转换为时间戳
                weekday()获取星期,0代表星期一以此类推
                strftime()由datetime转换成字符串,参数是格式化方式
"""
dat1 = datetime.datetime.today()
print(type(dat1))   # <class 'datetime.datetime'>
print(dat1)         # 2020-02-13 16:10:47.798099

# now(）方法可以指定特定的时区
dat2 = datetime.datetime.now()
print(type(dat2))   # <class 'datetime.datetime'>
print(dat2)         # 2020-02-13 16:12:14.317190

dat3 = datetime.datetime.fromtimestamp(152641561)
print(type(dat3))   # <class 'datetime.datetime'>
print(dat3)         # 1974-11-03 00:26:01

str = "2015-06-29 12:56:40"
print(type(str))    # <class 'str'>
print(str)      # 2015-06-29 12:56:40

dat4 = datetime.datetime.strptime("2015-06-29 12:56:40", "%Y-%m-%d %H:%M:%S")
print(type(dat4))   # <class 'datetime.datetime'>
print(dat4)     # 2015-06-29 12:56:40