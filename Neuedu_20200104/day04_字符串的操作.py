# -*- coding: utf-8 -*-
# @Time : 2020/1/4 21:30
# @Author : zhu
# @FileName: day04_字符串的操作.py
# @Software: PyCharm

# 字符串是不可修改变量，不能直接通过下标修改

# 字符串的切片
str1 = "东软睿道"
print(str1[2:])     # 睿道
print(str1[1:2])    # 软

# 字符串转大小写,是字符串内部的方法，会返回新的字符串
str2 = "www.Baidu.com"
print(str2.upper()) # WWW.BAIDU.COM
print(str2.lower()) # www.baidu.com

# 判断是否以XX开头或以XX结尾
str3 = "张三李四"
print(str3.startswith("张三"))    # True
print(str3.endswith("李四"))  # True

# index方法查找元素第一次出现的索引,如果元素不存在会报错
print(str2.index("w"))  # 0

# find方法查找元素第一次出现的索引，如果元素不存在返回-1
print(str2.find("w"))   # 0

# strip默认去除字符串前后两端的空格，换行符，tab
str4 = "   www.baidu.com  \t \n"
print(str4.strip())     # www.baidu.com
print(str4.lstrip())    # 只去除左边
print(str4.rstrip())    # 只去除右边

# 若strip传入参数，表示去除前后两端的参数
str5 = "?www.new.com?"
str5_new = str5.strip("?")
print(str5_new)     # www.new.com

# split()方法把字符串分割成列表,默认以空格分隔
str7 = "hello world python good"
str6 = "hello;world;python;good"
list1 = str6.split(";")
list2 = str7.split()
list3 = str7.split(" ", 2)  # 指定分割两次
print(list1)    # ['hello', 'world', 'python', 'good']
print(list2)    # ['hello', 'world', 'python', 'good']
print(list3)    # ['hello', 'world', 'python good']

# join()方法把列表转化为字符串,使用字符串把列表的元素拼接
list4 = ["a", "b", "c", "d", "e"]
str8 = ",".join(list4)
print(str8)     # a,b,c,d,e

# count()方法统计字符出现的次数
number = str2.count("w")
print(number)

# replace(要替换的字符串，替换后的字符串，替换的次数)方法，替换
str9 = "XXX哈哈哈XXX呜呜呜"
str10 = str9.replace("XXX", "嘻嘻嘻")
print(str10)    # 嘻嘻嘻哈哈哈嘻嘻嘻呜呜呜

# capitalize()第一个单词首字母大写
str11 = "zhu qizhao shuai ge"
str11_new = str11.capitalize()
print(str11_new)    # Zhu qizhao shuai ge

# title()所有单词首字母大写
str12 = str11.title()
print(str12)        # Zhu Qizhao Shuai Ge