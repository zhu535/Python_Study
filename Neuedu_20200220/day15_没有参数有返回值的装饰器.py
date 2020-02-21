# -*- coding: utf-8 -*-
# @Time : 2020/2/20 18:40
# @Author : zhu
# @FileName: day15_没有参数有返回值的装饰器.py
# @Software: PyCharm

def outter(func):

    def inner():
        print("验证功能")
        ret = func()
        return ret

    return inner

@outter  # func = outter(pay_func)
def pay_func():
    print("支付功能")
    return "操作成功"

ret = pay_func()
print(ret)