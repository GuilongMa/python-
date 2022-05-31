# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 12:28:04 2018

@author: qzxy
"""


# 串匹配算法
# ①朴素串匹配,p为匹配模式,最坏时间复杂度为O（nxm）
def native_match(t, p):
    m, n = len(t), len(p)
    i, j = 0, 0
    while i < m and j < n:
        if t[i] == p[j]:
            i += 1
            j += 1
        else:
            i, j = i - j + 1, 0
    if j == n:
        return i - j
    return -1


# KMP算法（无回溯）
def matching_KMP(t, p, pnext):
    j, i = 0, 0
    n, m = len(t), len(p)
    while i < m and j < n:
        if i == -1 or t[j] == p[i]:
            j, i = j + 1, i + 1
        else:
            i = pnext[i]
    if i == m:
        return j - i
    return -1
