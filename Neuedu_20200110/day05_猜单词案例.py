# -*- coding: utf-8 -*-
# @Time : 2020/1/10 0:36
# @Author : zhu
# @FileName: day05_猜单词案例.py
# @Software: PyCharm

import random
words = ["apple", "banana", "orange", "tiger", "happy"]

index = random.randint(0, len(words)-1)

word = words[index]
print(word)

word_bak = "-" * len(word)
print(word_bak)

guessTime = 5
