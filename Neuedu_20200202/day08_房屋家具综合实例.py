# -*- coding: utf-8 -*-
# @Time : 2020/2/6 17:21
# @Author : zhu
# @FileName: day08_房屋家具综合实例.py
# @Software: PyCharm

"""
房子（ House）有 户型、总面积和家具名称列表
新房子没有任何的家具
家具（HouseItem）有名字 和 占地面积
其中：
    床（bed） 占地 4 平米
    衣柜（chest） 占地 2 平米
    餐桌（table） 占地 1.5 平米
将以上三件 家具添加到房子中
打印房子时，要求输出：户型、总面积、剩余面积、以及家具列表
"""
class House:

    def __init__(self, type, area):
        self.type = type
        self.area = area
        self.lessArea = area
        self.itemList = []

    def __str__(self):
        return "房子的户型是%s，总面积为%.2f，剩余面积为%.2f，里面有家具：%s" %(self.type, self.area, self.lessArea, self.itemList)

    def add_item(self, HouseItem):
        if self.lessArea >= HouseItem.area:
            self.itemList.append(HouseItem.name)
            self.lessArea -= HouseItem.area
        else:
            print("房子空间不足")


class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s的占地面积是%.2f" %(self.name, self.area)

bed = HouseItem("床", 4)
print(bed)
chest = HouseItem("衣柜", 2)
print(chest)
table = HouseItem("餐桌", 1.5)
print(table)

house1 = House("两房一厅", 100)
house1.add_item(bed)
house1.add_item(chest)
house1.add_item(table)

print(house1)