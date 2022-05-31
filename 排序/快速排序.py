# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 19:38:38 2018

@author: qzxy
"""


# 空间复杂度O(log(n))，不稳定且没有适应性
# 期望时间复杂度O(n*log(n))，最坏O(n²):已排序，与列表中待排序的元素的相对顺序有关
# ①递归实现
def quick_sort(List):
    qsort_rec(List, 0, len(List) - 1)


def qsort_rec(List, l, r):
    if l >= r:
        return
    i = l
    j = r
    pivot = List[i]
    while i < j:
        while i < j and List[j] > pivot:
            j -= 1
        if i < j:
            List[i] = List[j]
            i += 1
        while i < j and List[i] < pivot:
            i += 1
        if i < j:
            List[j] = List[i]
            j -= 1
    List[i] = pivot
    qsort_rec(List, l, i - 1)
    qsort_rec(List, i + 1, r)


# ②另一种快速排序，思想一样，方式不同
def quick_sort2(List):
    def qsort_rec2(List, begin, end):
        if begin >= end:
            return
        pivot = List[begin]
        i = begin
        for j in range(begin + 1, end + 1):
            if List[j] < pivot:
                i += 1
                List[i], List[j] = List[j], List[i]
        List[i], List[begin] = List[begin], List[i]
        qsort_rec2(List, begin, i - 1)
        qsort_rec2(List, i + 1, end)

    qsort_rec2(List, 0, len(List) - 1)
