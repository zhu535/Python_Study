# -*- coding: utf-8 -*-
# @Time : 2020/2/20 9:38
# @Author : zhu
# @FileName: day15_ __dict__使用.py
# @Software: PyCharm

# __dict__会返回一个字典，字典里面存放着所有的属性和键值对

class A:

    name = '张三'

    def eat(self):
        print("吃")

    @classmethod
    def run(cls):
        print("跑")

    @staticmethod
    def drink():
        print("说")

# 属性和方法归类管理，实例只是调用
a = A()
print(A.__dict__)   # {'__module__': '__main__', 'name': '张三', 'eat': <function A.eat at 0x000002857DA34378>, 'run': <classmethod object at 0x000002857DA46940>, 'drink': <staticmethod object at 0x000002857DA496A0>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
print(a.__dict__)   # {}

a.name = '李四'
print(a.__dict__)   # {'name': '李四'}

class B(A):
    pass

b = B()
print(B.__dict__)   # {'__module__': '__main__', '__doc__': None}
print(b.__dict__)   # {}