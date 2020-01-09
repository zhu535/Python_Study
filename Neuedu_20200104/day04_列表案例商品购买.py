# -*- coding: utf-8 -*-
# @Time : 2020/1/9 16:36
# @Author : zhu
# @FileName: day04_列表案例商品购买.py
# @Software: PyCharm

"""
写一个循环，不断地问用户想买什么，用户选择一个编号，就把对应的商品添加到购物车里，最终用户输入q退出，打印购物车里的商品列表
"""

# 创建商品列表
goods = [["红米K30", 1899], ["荣耀20", 2399], ["华为P30", 3599], ["魅族", 1899]]

# 创建购物车列表
cart = []

# 计算价格
price = 0

print("***********商品列表***********")
# 展示商品，对商品列表进行遍历，由于需要用到索引，使用枚举遍历
for index, i in enumerate(goods):
    print("商品编号:%s\t%s\t\t%s" % (index, i[0], i[1]))

while True:
    # 输入指令操作
    operation = input("\n请输入选择的商品编号，或输入q退出：")

    # 判断是否为数字，如果为数字判断编号是否存在，存在则进行加入购物车操作，不存在则返回错误信息
    if operation.isdigit():
        num = int(operation)
        if 0 <= num <= len(goods):
            cart.append(goods[num])
            price += goods[num][1]
            print("已将 %s 添加至购物车" % goods[num][0])
        else:
            print("商品不存在，请重新输入")

    # 判断是否为"q"或"Q"，是则进行退出操作并打印购物车清单
    elif operation.lower() == "q":
        print("\n购物车:")
        for index, i in enumerate(cart):
            print("商品编号:%s\t%s\t\t%s" % (index, i[0], i[1]))
        print("总价：%s" % price)
        break

    # 以上都不是则表示指令输入错误，返回错误信息
    else:
        print("输入错误，请重新输入")