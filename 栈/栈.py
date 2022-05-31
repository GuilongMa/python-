# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 19:28:04 2018

@author: qzxy
"""

class StackUnderflow(ValueError):
    pass

class SStack:
    def __init__(self):
        self._data = []
    
    def is_empty(self):
        return self._data == []
    
    def top(self):
        if self._data == []:
            raise StackUnderflow("in SStack.top()")
        return self._data[-1]
    
    def push(self,data):
        self._data.append(data)
        
    def pop(self):
        if self._data == []:
            raise StackUnderflow("in SStack.pop()")
        return self._data.pop()
    
    def depth(self):
        return len(self._data)

class LNode:
    def __init__(self,data,next_ = None):
        self._data = data
        self._next = next_

class LStack:
    def __init__(self):
        self._head = None
    
    def is_empty(self):
        return self._head is None
    
    def top(self):
        if self._head is None:
            raise StackUnderflow("in LStack.top()")
        return self._head._data
    
    def push(self,data):
        self._head = LNode(data,self._head)
        
    def pop(self):
        if self._head is None:
            raise StackUnderflow("in LStack.pop()")
        p = self._head
        self._head = p._next
        return p._data