#! \hp\PycharmProjects\Python_Workspace
# -*- coding:utf-8 -*-
# project:
# user:hp
# Author: zhu
# Date: 2019/12/25 12:13

name_list = ["张三", "李四", "王五"]

object_list = ["张三", 1, "李四", 5]

"""3、列表的新增操作"""

# append()方法是往列表中追加一个元素
name_list.append("小明")

# insert()方法是往列表的指定索引中插入一个元素
name_list.insert(0, "小红")

# extend()方法是往列表中追加iterable的元素
# iterable:包含有一组数据的数据类型，如列表
temp_list = ["小王", "小黄", "小橙"]
name_list.extend(temp_list)

"""4、列表的删除操作"""

# remove()方法是移除列表中指定的元素
# 当有多个相同的元素时，默认删除第一个
# 当删除的元素不存在时，报错
name_list.remove("小王")

# pop()方法是移除列表末端的一个元素，为弹出
# pop(index)方法是移除列表指定位置的元素
name_list.pop()
name_list.pop(0)

# clear()方法是清空列表
# name_list.clear()

# 以上三种删除方法是列表的方法，除此以外还可以使用python提供的del方法，表示把一个变量从内存中删除
# 不建议使用，但删除多个值时使用
del name_list[0]

print(name_list)