# -*- coding: utf-8 -*-
# @Time : 2020/1/27 20:16
# @Author : zhu
# @FileName: day06_国家分组案例.py
# @Software: PyCharm

import random

country = "比利时，澳大利亚，中国，韩国，美国，日本，德国，意大利，英国，新西兰，阿根廷，葡萄牙，西班牙，冰岛，荷兰，尼日利亚"
countries_list = country.split("，")
country_dict = {}

for i in range(4):
    country_list = []

    for j in range(4):
        rand = random.randint(0, len(countries_list) - 1)
        country_list.append(countries_list[rand])
        countries_list.remove(countries_list[rand])

    country_dict[i+1] = country_list

for i, j in country_dict.items():

    print("第%s组:%s" %(i, j))
