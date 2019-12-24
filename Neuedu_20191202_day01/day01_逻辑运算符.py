#! \hp\PycharmProjects\Python_Workspace
# -*- coding:utf-8 -*-
# project:
# user:hp
# Author: zhu
# Date: 2019/12/24 15:14

# and: 与，两边都为真的时候才为真
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# or： 或，两边都为假的时候才为假
print(True or False)    # True
print(True or True)     # True
print(False or True)    # True
print(False or False)   # False

# not：非，反义词
print(not True)     # False
print(not False)    # True

# 下面这句话，按理论来讲由于name未定义，运行时应该报错
# and只有两边都为真的时候才为真，Python是一种解释型语言，边编译边执行，当编译到False and的时候结果已经是False，就不会再往后编译
print(False and name)   # False
# print(True and name)  报错

# 对于or也同理
print(True or name)     # True
# print(False or name)  报错

# 结果是什么？
# 如果没有优先级，从左到右执行，应该是True and False or False ---> False or False ---> False  与结果不符合
# 说明在逻辑运算中是有优先级的，and的优先级大于or
print(True or False and False or False)     # True
