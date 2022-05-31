# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 16:04:05 2018

@author: qzxy
"""


# 冒泡排序,具有稳定性与适应性，最差O(n2),最好O(n),平均为O(n2),效率低于插入排序
def mao_pao_sort(l1):
    for i in range(len(l1) - 1):
        found = False
        for j in range(len(l1) - i - 1):
            if l1[j] > l1[j + 1]:
                l1[j], l1[j + 1] = l1[j + 1], l1[j]
                found = True
        if not found:
            break


# 交错冒泡排序
def jiao_cuo_mao_pao_sort(l1):
    for i in range(len(l1) - 1):
        found = False
        found1 = False
        for j in range(len(l1) - i - 1):
            if l1[j] > l1[j + 1]:
                l1[j], l1[j + 1] = l1[j + 1], l1[j]
                found = True
        if not found:
            break
        for k in range(len(l1) - i - 2, -1, -1):
            if l1[k] > l1[k + 1]:
                l1[k], l1[k + 1] = l1[k + 1], l1[k]
                found1 = True
        if not found1:
            break
