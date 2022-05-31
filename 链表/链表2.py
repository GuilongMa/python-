# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:37:29 2018

@author: qzxy
"""

class LNode:
    def __init__(self,data,next_ = None):
        self._data = data
        self._next = next_

class LinkedListUnderflow(ValueError):
    pass

"""链表类"""
class LList:
    def __init__(self,head = None):
        self._head = head 
    
    def is_empty(self):
        return self._head is None
    
    #从开头加入元素结点
    def prepend(self,data):
        self._head = LNode(data,self._head)
    
    #删除首头元素结点，因为后进先出
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.data
        
        self._head = self._head._next
        return e
    #后端插入
    def append(self,data):
        if self._head is None:
            self._head = LNode(data)
            return
        p = self._head
        while p._next:
            p = p._next
        p._next = LNode(data)
    
    #后端删除
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if not p._next:
            e = p._data
            self._head = None
            return e
        while p._next._next:
            p = p._next
        e = p._next._data
        p._next = None
        return e
    #查找满足给定条件的第一个元素，可以改为生成器函数（return改为yield），
    #再用for循环迭代输出
    def find(self,pred):
        p = self._head
        while p:
            if pred(p._data):
                return p._data
            p = p._next
            
    #查看被操作表的情况
    def printall(self):
        p = self._head
        while p:
            print(p._data,end='')
            if p._next:
                print(', ',end='')
            p = p._next
        print('')
     
#    def for_each(self,proc):
#        p = self._head 
#        while p:
#            proc(p._data)
#            p = p._next
#    
#    def elements(self):
#        p = self._head
#        while p:
#            yield p._data
#            p = p._next

class LList1(LList):
    def __init__(self,head):
        super().__init__(head)
        self._rear = None
    
        #从开头加入元素结点
    def prepend(self,data):
        self._head = LNode(data,self._head)
        if self._rear is None:
            self._rear = self._head
            
    def append(self,data):
        if self._head is None:
            self._head = LNode(data)
            self._rear = self._head
        else:
            self._rear._next = LNode(data)
            self._rear = self._rear._next
    
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if not p._next:
            e = p._data
            self._head = None
            return e
        while p._next._next:
            p = p._next
        e = p._next._data
        p._next = None
        self._rear = p
        return e

class LLNode(LNode):
    def __init__(self,data,prev = None,next_ = None):
        super().__init__(data,next_)
        self._prev = prev

class SLList(LList1):
    def __init__(self,head):
        super().__init__(head)

        #从开头加入元素结点
    def prepend(self,data):
        self._head = LLNode(data,self._prev,self._head)
        if self._rear is None:
            self._rear = self._head
        self._head._next._prev = self._head
             
    
    def append(self,data):
        if self._head is None:
            self._head = LNode(data)
            self._rear = self._head
        else:
            self._rear._next = LNode(data)
            self._rear = self._rear._next
    