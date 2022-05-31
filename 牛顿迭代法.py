# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 17:48:21 2018

@author: qzxy
"""

""" 如果存在一个值guess是多项式p的根的近似值，那么guess-p（guess）/p'（guess）
    就是一个更好的近似值，其中p'为p的一次导数
"""
# 利用牛顿-拉弗森法寻找平方根,效率高于二分法
epsilon = 0.0001
k = 7
guess = k / 2.0
while (guess ** 2 - k) >= epsilon:
    guess = guess - (guess ** 2 - k) / (2 * guess)
print('Square root of', k, 'is about', guess)
