# -*- coding: utf-8 -*-
# @Time : 2020/2/20 10:33
# @Author : zhu
# @FileName: day15_hasattr,getattr,setattr,delattr的使用.py
# @Software: PyCharm

class A:

    name = 'zhangsan'

    def __init__(self):
        self.age = 18

a = A()
print(hasattr(a, "name"))   # True
print(hasattr(A, "name"))   # True

print(hasattr(a, "age"))    # True
print(hasattr(A, "age"))    # False

print(getattr(a, "name"))   # zhangsan
print(getattr(A, "name"))   # zhangsan

print(getattr(a, "age"))    # 18
# print(getattr(A, "age"))
# print(getattr(A, "sex"))  type object 'A' has no attribute 'sex'
print(getattr(A, "sex", "男"))   # 男 如果不存在则赋予默认值

# setattr(类，属性名，修改后的属性)
setattr(A, "name", "lisi")
print(A.__dict__)