# -*- coding: utf-8 -*-
# @Time : 2020/1/4 18:04
# @Author : zhu
# @FileName: day04_元组的创建.py
# @Software: PyCharm

# 元组属于不可变的有序序列，可以存储不同类型的元素。一旦创建，用任何方法都不能修改其元素

# 元组的创建
x = (1, 2, 3, "张三")
print(x)

# 由于元组是有序的序列，所以可以使用索引来访问元素
print(x[3])     # 张三

# 如何定义一个元素的元组?
tup1 = (1)
print(type(tup1))   # <class 'int'>

tup = (1,)
print(type(tup))    # <class 'tuple'>

# 变量名使用大写，证明此变量为常量，不可被修改
RED = (255, 0, 0)

# 元组里面存放列表，元组虽然不能作修改，但是列表中的元素还能作修改
tup2 = (1, 2, 3, ["张三"])
tup2[3][0] = "王五"
print(tup2)     # (1, 2, 3, ['王五'])

