# -*- coding: utf-8 -*-
# @Time : 2020/2/15 11:21
# @Author : zhu
# @FileName: day13_日志的全局配置参数解析.py
# @Software: PyCharm

import logging

# 改变日期输出datefmt
# filename 将日志输出到文件外部
logging.basicConfig(filename= "日志.log", datefmt= "%Y-%m-%d %H:%M:%S", level= logging.WARNING, format="%(name)s - %(filename)s - %(asctime)s - %(lineno)s - %(message)s")

logging.debug("我是debug")    # WARNING:root:我是warning
logging.info("我是info")
logging.warning("我是warning")
logging.error("我是error")
logging.critical("我是critical")