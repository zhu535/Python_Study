#! \hp\PycharmProjects\Python_Workspace
# -*- coding:utf-8 -*-
# project:
# user:hp
# Author: zhu
# Date: 2019/12/25 12:13

name_list = ["张三", "李四", "王五"]

object_list = ["张三", 1, "李四", 5]

"""1、列表的取值和取索引操作"""

print(name_list[0])     # 张

# 知道数据内容，想确定数据在列表中的位置
print(name_list.index("张三"))    # 0

"""2、列表的修改操作 """

name_list[0] = "小猪"