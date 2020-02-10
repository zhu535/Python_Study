# -*- coding: utf-8 -*-
# @Time : 2020/2/10 10:47
# @Author : zhu
# @FileName: day09_英雄pk案例改造.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
# @Time : 2020/2/7 19:53
# @Author : zhu
# @FileName: day09_英雄PK案例.py
# @Software: PyCharm

import random

class Sprite(object):
    # 初始化实例属性
    def __init__(self, blood, attack):
        self.blood = blood
        self.attack = attack

    # 获取剩余血量
    def get_blood(self):
        return self.blood

    def get_damage(self):
        pass

    # 被攻击
    def take_damage(self, Sprite):

        damage = Sprite.get_damage()

        self.blood -= damage

        print(f"{self.name}:您被{Sprite.name}攻击了，此次受到{damage}点伤害，还剩下{self.blood}点血量")

        if self.blood <= 0:
            print("游戏结束")
            return True
        else:
            return False

class Hero(Sprite):

    def __init__(self, name, blood, attack):
        super().__init__(blood, attack)
        self.name = name

    def get_damage(self):
        return random.randint(self.attack - 5, self.attack + 5)

class Monster(Sprite):

    def __init__(self, name, blood, attack):
        super().__init__(blood, attack)
        self.name = name

    def get_damage(self):
        return random.randint(self.attack - 3, self.attack + 3)

hero = Hero("提莫", 100, 10)
monster = Monster("野怪", 100, 8)

while True:

    d = monster.take_damage(hero)
    if d:
        break
    d = hero.take_damage(monster)
    if d:
        break