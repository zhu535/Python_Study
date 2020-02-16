# -*- coding: utf-8 -*-
# @Time : 2020/2/15 10:21
# @Author : zhu
# @FileName: day13_日志的全局配置.py
# @Software: PyCharm

# 控制台输出日志
# Logging.日志的级别(日志的信息)
# debug --> info --> warning --> error --> critical
# root是默认的日志名称，只会输出warning级别以上的日志
import logging
# 配置默认的root日志
# 格式化输出format = 字符串
logging.basicConfig(level= logging.WARNING, format="%(name)s - %(filename)s - %(asctime)s - %(lineno)s - %(message)s")


logging.debug("我是debug")    # WARNING:root:我是warning
logging.info("我是info")
logging.warning("我是warning")
logging.error("我是error")
logging.critical("我是critical")