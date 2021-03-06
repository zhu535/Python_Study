# -*- coding: utf-8 -*-
# @Time : 2020/2/2 16:25
# @Author : zhu
# @FileName: day08_sorted函数.py
# @Software: PyCharm

# sorted函数默认升序排序
l = [156415,61,5641,564,6541,5641,56,4156,41,561,8,4,124,5]

l1 = sorted(l)
print(l1)   # [4, 5, 8, 41, 56, 61, 124, 561, 564, 4156, 5641, 5641, 6541, 156415]

l2 = sorted(l, reverse=True)
print(l2)   # [156415, 6541, 5641, 5641, 4156, 564, 561, 124, 61, 56, 41, 8, 5, 4] 降序


# 对成绩排序
l3 = [("张三", 60), ("李四", 100), ("王五", 70), ("赵六", 80)]
# key接收的就是每一个元素。sorted是按照key接收的值去排序的
# 让key去接收60,100,70,80
# key还可以接收一个函数，然后sorted按照函数的返回值进行排序\
def func(a):
    b = a[1]
    return b

l4 = sorted(l3, key=func, reverse=True)
print(l4)   # [('李四', 100), ('赵六', 80), ('王五', 70), ('张三', 60)]