#! \hp\PycharmProjects\Python_Workspace
# -*- coding:utf-8 -*-
# project:
# user:hp
# Author: zhu
# Date: 2019/12/24 14:10

Name = "张三"
Sex = "男"

print(Name + "的性别是" + Sex)

print(Name, "的性别是", Sex)

# 格式化输出(%s表示字符串占位)
print("%s的性别是%s" % (Name, Sex))

# %d表示整数占位 ---> %0(个数)d 表示用0填充至与个数相等
Age = 18
print("%s的收入是%03d" % (Name, Age))   # 张三的收入是018

Weight = 96.52
print("%s的体重是%d" % (Name, Weight))  # 张三的体重是96

# %f表示浮点型数据占位 ---> %.(小数点后面位数)f 表示取小数点后面多少位

print("%s的体重是%f" % (Name, Weight))  # 张三的体重是96.520000 ---> 默认保留小数点后6位

print("%s的体重是%.2f" % (Name, Weight))  # 张三的体重是96.52

"""
第二种格式化输出的方法：{}
"""

print("{}的性别是{}".format(Name, Sex))  # 张三的性别是男

# 使用位置编号
print("{0}的性别是{0}".format(Name, Sex))  # 张三的性别是张三

print("{0}{0}的性别是{1}".format(Name, Sex))  # 张三张三的性别是男

print("{0}的年龄是{1}".format(Name, Age))   # 张三的年龄是18

"""
第三种格式化输出的方法：f处理字符串
"""
print("{Name}的性别是{Sex}")    # {Name}的性别是{Sex} ---> 错误的

print(f"{Name}的性别是{Sex}")   # 张三的性别是男

print(f"{Name}的年龄是{Age}")   # 张三的年龄是18