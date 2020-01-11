# -*- coding: utf-8 -*-
# @Time : 2020/1/10 0:36
# @Author : zhu
# @FileName: day05_猜单词案例.py
# @Software: PyCharm

import random
words = ["apple", "banana", "orange", "tiger", "happy"]

index = random.randint(0, len(words)-1)

word = words[index]

word_bak = "-" * len(word)

word_list = list(word_bak)

guessTimes = 5

word_index = 0

# 程序主体
while True:

    for i in word_list:
        print(i, end="")

    if guessTimes <= 0:
        print("\n你失败了")
        break

    if "-" not in word_list:
        print("\n你成功了")
        break

    write = input("\n请输入一个字母：")

    # 输入正确
    if write == word[word_index]:
        word_list[word_index] = write
        word_index += 1

    # 输入错误
    else:
        guessTimes -= 1
        print("猜错了！还剩下 %d 次机会" % guessTimes)