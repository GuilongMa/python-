# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 17:25:04 2018

@author: qzxy
"""


# 算法复杂度O(nlog(n)),原理：分治算法
# 分解阈值（又称递归基），输入规模大于阈值才进行分解求解再合并
# 合并复杂度O(len(L))
# 空间复杂度为O(len(L))
def merge(left, right, compare):
    """假设left和right书籍两个有序列表，compare定义了一种元素排序规则
        返回一个新的有序列表（按照compare定义的顺序），其中包含与（left+right）
        相同的元素。
    """

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


# 递归复杂度O(log(len(L)))
def merge_sort(L, compare=lambda x, y: x < y):
    """假设L是列表，compare定义了L中元素的排序规则
        返回一个新的具有L中元素的有序列表
    """
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)
