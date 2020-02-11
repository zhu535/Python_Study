# -*- coding: utf-8 -*-
# @Time : 2020/2/10 11:28
# @Author : zhu
# @FileName: day09_扑克牌案例.py
# @Software: PyCharm

color_list = ["黑桃", "红桃", "梅花", "方块"]

class Card(object):

    def __init__(self, color, num):
        self.color = color
        self.num = num

    def __str__(self):
        if self.num == 1:
            self.num = "A"
        elif self.num == 11:
            self.num = "J"
        elif self.num == 12:
            self.num = "Q"
        elif self.num == 13:
            self.num = "K"
        else:
            self.num = self.num

        return f"{self.color}{self.num}"

class Poker(object):

    poker_list = []

    def get_Poker(self):
        for color in color_list:
            for num in range(1, 14):
                card = Card(color, num)
                Poker.poker_list.append(card)
        return Poker.poker_list

poker = Poker()
poker_list = poker.get_Poker()
for i in poker_list:
    print(i)