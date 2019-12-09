#! \hp\PycharmProjects\Python_Workspace
# -*- coding:utf-8 -*-
# project:
# user:hp
# Author: zhu
# Date: 2019/12/2 15:11

# 拳头为1，布为2，剪刀为3
import random

player = int(input("你想出的拳是:"))

computer = random.randint(1, 3)
print("电脑出的拳是:%d" % computer)

if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer ==2):
    print("玩家胜利")
elif player == computer:
    print("平局")
else:
    print("电脑胜利")
