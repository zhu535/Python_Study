# -*- coding: utf-8 -*-
# @Time : 2020/1/18 12:41
# @Author : zhu
# @FileName: day05_字典的遍历.py
# @Software: PyCharm

dict2 = {"小明": 98, "小红": 100, "小王": 60}
# 使用in方法判断是否在字典内部
# 如果单独使用字典的变量名去判断，相当于使用.keys()方法判断键是否存在
# 如果想要判断值是否存在于字典，要使用.values()方法
for i in dict2:
    print(i)    # 小明  小红  小王

for i in dict2.values():
    print(i)    # 98  100  60

for i in dict2.items():
    print(i)    # ('小明', 98)  ('小红', 100)  ('小王', 60)

# 元组的拆包
tup = (1, 2, 3, 4)
a, b, c, d = tup
print(a, b, c, d)   # 1 2 3 4

# 所以在遍历字典的时候可以加入元组的拆包操作
for key, value in dict2.items():
    print(key, value)   # 小明 98 小红 100  小王 60