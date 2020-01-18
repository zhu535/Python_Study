# -*- coding: utf-8 -*-
# @Time : 2020/1/18 16:19
# @Author : zhu
# @FileName: day06_单词频率统计案例.py
# @Software: PyCharm

word = "I'm a boy,I'm a girl.When it is true,it is true.That's are cats,the red is red."

# 统计放入一个字典中{"单词": "次数"}

# 1.处理字符串,把标点符号替换成空格
word = word.replace(",", " ").replace(".", " ")

# 2.把处理后的字符串放入一个列表中
word_list = word.split(" ")
word_list.pop()     # 去掉最后一个空格
print(word_list)

# 3.单词频率统计
