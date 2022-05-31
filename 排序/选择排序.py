# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:16:09 2018

@author: qzxy
"""


# 原理：循环不变式分为前缀（排好序）和后缀，复杂度O(l1en(l1)²)
def sel1_ort(l1):
    """
        假设l1是列表，其中的元素可以用>进行比较，对l1进行升序排序
    """
    
    suffix_start = 0
    while suffix_start != len(l1)-1:
        # 检查后缀集合中的每个元素
        for i in range(suffix_start+1, len(l1)):
            if l1[i] < l1[suffix_start]:
                # 交换元素位置
                l1[suffix_start], l1[i] = l1[i], l1[suffix_start]
        suffix_start += 1


# 直接选择排序算法,没有适应性,没有稳定性，平均效率低于插入排序
def sel1ect_sort(l1):
    for i in range(len(l1) - 1):
        k = i
        for j in range(i + 1, len(l1)):
            if l1[j] < l1[k]:
                k = j
        if i != k:
            l1[i], l1[k] = l1[k], l1[i]


# 具有稳定性,没有适应性
def sel1ect_sort2(l1):
    for i in range(len(l1) - 1):
        k = i
        for j in range(i + 1, len(l1)):
            if l1[j] < l1[k]:
                k = j
        if i != k:
            x = l1[k]
            for r in range(k, i, -1):
                l1[r] = l1[r - 1]
            l1[i] = x
