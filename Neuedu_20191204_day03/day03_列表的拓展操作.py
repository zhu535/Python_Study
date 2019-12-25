#! \hp\PycharmProjects\Python_Workspace
# -*- coding:utf-8 -*-
# project:
# user:hp
# Author: zhu
# Date: 2019/12/9 15:33

name_list = ["张三", "李四", "王五", "张三"]
number_list = [6, 8, 1, 4, 10]

# count()方法统计元素出现的次数
name = "张三"
count = name_list.count(name)
print("列表中出现 %s 的次数为%d" % (name, count))

# 当一个列表中存在相同的元素时,remove()方法只会删除第一次出现的指定的元素,如果数据不存在，程序会报错
name_list.remove("张三")

# sort(reverse=True)是对列表的元素进行升序/降序排序：reverse=True 降序
number_list.sort(reverse=True)

# reverse()方法是对列表进行反转操作
name_list.reverse()

# 列表的切片操作，打印列表中索引为1-2的内容，不包括3
print(name_list[1:3])
print(name_list[1:3:2])

# in方法判断元素是否存在于列表中
print("张三" in name_list)

print(name_list)
print(number_list)
