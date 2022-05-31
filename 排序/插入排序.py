# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:31:14 2018

@author: qzxy
"""


# 返回新的排序序列
def insert_sort(l1):
    l11 = l1[:]
    for i in range(len(l11) - 2, -1, -1):
        x = l11[i]
        j = i
        while j < len(l11) - 1 and x > l11[j + 1]:
            l11[j] = l11[j + 1]
            j += 1
        l11[j] = x
    return l11


# 原地排序,有适应性，原序数有序，则只需O（n），稳定
def insert_sort2(l1):
    for i in range(1, len(l1)):
        x = l1[i]
        j = i
        while j > 0 and l1[j - 1] > x:
            l1[j] = l1[j - 1]
            j -= 1
        l1[j] = x

            
# 复习
def insert_sort3(l1):
    for i in range(1, len(l1)):
        temp = l1[i]
        k = None
        for j in range(i, 0, -1):
            if temp < l1[j-1]:
                l1[j] = l1[j-1]
            else:
                k = j
                break
        else:
            l1[0] = temp
        if k is not None:
            l1[k] = temp
    return l1


if __name__ == "__main__":
    print(insert_sort3([2,4,1,6,5]))