# -*- coding: utf-8 -*-
# @Time : 2020/2/13 17:38
# @Author : zhu
# @FileName: day12_os模块.py
# @Software: PyCharm

#  导包
import os

#  getcwd()获取执行命令的位置
pa = os.getcwd()  # C:\Users\Administrator\PycharmProjects\Python_Study\Neuedu_20200213

#  path.join路径拼接
pa1 = os.path.join(pa, "demo.txt")
print(pa1)      # C:\Users\Administrator\PycharmProjects\Python_Study\Neuedu_20200213\demo.txt

with open(pa1, mode="a+") as f:
    f.write("1234")

#  path.split/path.splitext路径拆分(路径不一定真实存在，只对字符串进行操作)
pa2 = "C:\\Users\\Administrator\\PycharmProjects\\Python_Study\\Neuedu_20200213\\demo.txt"
l = os.path.split(pa2)
print(l)    # ('C:\\Users\\Administrator\\PycharmProjects\\Python_Study\\Neuedu_20200213', 'demo.txt')

l2 = os.path.splitext(pa2)
print(l2)   # ('C:\\Users\\Administrator\\PycharmProjects\\Python_Study\\Neuedu_20200213\\demo', '.txt')

#  rename(原名,更改名称)文件重命名
# os.rename("demo.txt", "suibian.txt")

#  remove删除文件
# os.remove("suibian.txt")


#  import shutil shutil.copyfile(要复制的文件,复制后的文件名)复制文件
import shutil

shutil.copyfile("demo.txt", "demo1.txt")


#  listdir()获取当前目录下的所有文件
print(os.listdir())     # ['day12_datetime模块.py', 'day12_datetime模块下的timedetla类.py', 'day12_os模块.py', 'day12_sys模块.py', 'day12_time模块.py', 'demo.txt', 'demo1.txt']

#  path.isfile判断文件是否存在
print(os.path.isfile("demo.txt"))

#  path.exists判断目录是否存在
print(os.path.exists("demo"))