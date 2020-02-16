# -*- coding: utf-8 -*-
# @Time : 2020/2/15 13:21
# @Author : zhu
# @FileName: day13_日志的使用.py
# @Software: PyCharm


from Neuedu_20200215.demo import logger

try:
    print(1/0)

except:
    logger.error("分母不能为0")