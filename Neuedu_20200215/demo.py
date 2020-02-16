# -*- coding: utf-8 -*-
# @Time : 2020/2/15 13:21
# @Author : zhu
# @FileName: demo.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
# @Time : 2020/2/15 11:47
# @Author : zhu
# @FileName: day13_将日志在控制台输出以及存入文件.py
# @Software: PyCharm

import logging
# 1.生成一个logger对象，并对其设置最低权限
logger = logging.getLogger("sample")

logger.setLevel(logging.DEBUG)

# 2.获取格式化输出对象
formatter = logging.Formatter("%(name)s : %(asctime)s -- %(filename)s -- %(lineno)s -- %(message)s")

# 3.获取handler对象
sh = logging.StreamHandler()
fh = logging.FileHandler("handler.log", encoding="utf-8")

# 4.向hanler添加格式化对象
sh.setFormatter(formatter)
fh.setFormatter(formatter)

# 4.1 设置输出等级
sh.setLevel(logging.DEBUG)
fh.setLevel(logging.WARNING)

# 5.向logger添加handler
logger.addHandler(sh)
logger.addHandler(fh)

# 6.输出日志
# logger.debug("我是debug")
# logger.info("我是info")
# logger.warning("我是warning")
# logger.error("我是error")
# logger.critical("我是critical")