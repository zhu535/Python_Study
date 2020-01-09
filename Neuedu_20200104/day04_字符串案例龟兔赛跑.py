# -*- coding: utf-8 -*-
# @Time : 2020/1/9 18:33
# @Author : zhu
# @FileName: day04_字符串案例龟兔赛跑.py
# @Software: PyCharm

import random
import time

# 兔子的位置
rpos = 0

# 乌龟的位置
tpos = 0

while True:
    time.sleep(0.5)
    # 判断是否有选手到达终点
    if rpos >= 70 or tpos >= 70:
        break
    row = "-" * 70

    # 兔子、乌龟随机数
    rr = random.randint(1, 10)
    tr = random.randint(1, 10)

    if rr == 1:
        # 大跌：向左12格
        rpos -= 12

        # 如果位置小于0，则等于0
        if rpos < 0:
            rpos = 0

    elif 2 <= rr <= 3:
        # 睡觉：原地不动
        rpos = rpos
    elif 4 <= rr <= 5:
        # 大跳：向右9格
        rpos += 9
    elif 6 <= rr <= 7:
        # 小跌：向左2格
        rpos -= 2

        # 如果位置小于0，则等于0
        if rpos < 0:
            rpos = 0
    else:
        # 小跳：向右1格
        rpos += 1

    if 1 <= tr <= 2:
        # 跌跤：向左6格
        tpos -= 6

        # 如果位置小于0，则等于0
        if tpos < 0:
            tpos = 0

    elif 3 <= tr <= 5:
        # 慢走：向右1格
        tpos += 1
    else:
        # 快走：向右3格
        tpos += 3

    if rpos == tpos:
        row = row[:rpos] + "咬" + row[tpos:]
        print(row)
    else:
        row = row[:rpos] + "兔" + row[rpos:]
        row = row[:tpos] + "龟" + row[tpos:]
        print(row)

if rpos >= 70:
    print("兔子获胜！")
else:
    print("乌龟获胜！")