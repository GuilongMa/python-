# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 15:07:34 2018

@author: qzxy
"""


class PrioQueueError(ValueError):
    pass


class PrioQue:
    def __init__(self, elist=[]):
        """拷贝形参，防止共享，形参最好为不可变对象，
        list转化使形参可为可迭代对象"""
        self._datas = list(elist)
        # 定义数值小的优先级大
        self._datas.sort(reverse=True)

    def is_empty(self):
        return self._datas == []

    def enqueue(self, data):
        i = len(self._datas) - 1
        while i > 0:
            if self._datas[i] <= data:
                i -= 1
            else:
                break
        self._datas.insert(i + 1, data)

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in top')
        return self._datas[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in pop')
        return self._datas.pop()


# 基于堆的优先队列类
class ProQueue:
    def __init__(self, elist=[]):
        """拷贝形参，防止共享，形参最好为不可变对象，
        list转化使形参可为可迭代对象"""
        self._datas = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return self._datas == []

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in peek')
        return self._datas[0]

    def enqueue(self, data):
        self._datas.append(None)
        self.siftup(data, len(self._datas) - 1)

    def siftup(self, e, last):
        datas, i, j = self._datas, last, (last - 1) // 2
        while i > 0 and e < datas[j]:
            datas[i] = datas[j]
            i, j = j, (j - 1) // 2
        self._datas[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in pop')
        data = self._datas[0]
        e = self._datas.pop()
        if len(self._datas) > 0:
            self.siftdown(e, 0, len(self._datas))
        return data

    def _siftdown(self, e, begin, end):
        datas, i, j = self._datas, begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and datas[j + 1] < datas[j]:
                j += 1
            if e < datas[j]:
                break
            datas[i] = datas[j]
            i, j = j, 2 * j + 1
        datas[i] = e

    def buildheap(self):
        end = len(self._datas)
        for i in range(end // 2, -1, -1):
            self._siftdown(self._datas[i], i, end)
