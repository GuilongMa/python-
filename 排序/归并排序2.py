# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 18:55:24 2018

@author: qzxy
"""


# 没有适应性，有稳定性
def merge(lfrom, lto, low, mid, high):
    i, j, k = low, mid, low
    while i < mid and j < high:
        if lfrom[i] <= lfrom[j]:
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1
    while i < mid:
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:
        lto[k] = lfrom[j]
        j += 1
        k += 1


def merge_pass(lfrom, lto, llen, slen):
    i = 0
    while i + slen * 2 < llen:
        merge(lfrom, lto, i, i + slen, i + slen * 2)
        i += slen * 2
    if i + slen < llen:
        merge(lfrom, lto, i, i + slen, llen)
    else:
        for j in range(i, llen):
            lto[j] = lfrom[j]


def merge_sort(lst):
    slen, llen = 1, len(lst)
    templst = [None] * llen
    while slen < llen:
        merge_pass(lst, templst, llen, slen)
        slen *= 2
        merge_pass(templst, lst, llen, slen)
        slen *= 2
