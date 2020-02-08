# -*- coding: utf-8 -*-
# @Time : 2020/2/7 19:53
# @Author : zhu
# @FileName: day09_英雄PK案例.py
# @Software: PyCharm

import random

class Hero:
    # 初始化实例属性
    def __init__(self, name, blood, attack):
        self.name = name
        self.blood = blood
        self.attack = attack

    # 获取剩余血量
    def get_blood(self):
        return self.blood

    # 被攻击
    def take_damage(self, Monster):

        damage = random.randint(Monster.attack - 5, Monster.attack + 5)

        self.blood -= damage

        print(f"{self.name}:您被{Monster.name}攻击了，此次受到{damage}点伤害，还剩下{self.blood}点血量")

        if self.blood <= 0:
            print("游戏结束")
            return True
        else:
            return False

class Monster:
    # 初始化实例属性
    def __init__(self, name, blood, attack):
        self.name = name
        self.blood = blood
        self.attack = attack

    # 获取剩余血量
    def get_blood(self):
        return self.blood

    # 被攻击
    def take_damage(self, Hero):

        damage = random.randint(Hero.attack - 5, Hero.attack + 5)

        self.blood -= damage

        print(f"{self.name}:您被{Hero.name}攻击了，此次受到{damage}点伤害，还剩下{self.blood}点血量")

        if self.blood <= 0:
            print("游戏结束")
            return True
        else:
            return False


hero = Hero("提莫", 100, 10)
monster = Monster("野怪", 100, 8)

while True:

    d = monster.take_damage(hero)
    if d:
        break
    d = hero.take_damage(monster)
    if d:
        break