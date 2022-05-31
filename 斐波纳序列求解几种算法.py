# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 19:27:45 2018

@author: qzxy
"""


# 复杂度O（n）
def fib(n):
    f1 = f2 = 1
    for k in range(1, n):
        f1, f2 = f2, f1 + f2
    return f2


# 递归复杂度为指数
def fib1(n):
    if n < 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)
