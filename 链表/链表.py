# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 17:07:53 2018

@author: qzxy
"""
"""结点"""
class LNode:
    def __init__(self,data,next_ = None):
        self._data = data
        self._next = next_

#"""空链表"""
#head = None
#
#"""表首端插入,假如head非空,head是个变量"""
#first_node = LNode('1')
#first_node._next = head
#head = first_node
#"""表首端插入,假如head非空,head是个空结点(或者存储数据data为结点数量，非空)"""
#head = LNode()
#first_node = LNode('1')
#first_node._next = head._next
#head._next = first_node
#"""一般情况的插入"""
#pre = LNode('插入位置的前一结点')
#insert = LNode('插入的结点')
#insert._next = pre._next
#pre._next = insert
#"""删除表首元素"""
#head = head._next
#"""一般情况的删除"""
#pre._next = pre._next._next
#"""扫描"""
#p = head
#while p :
#    #something
#    p = p._next
#"""创建10个结点的链表"""
#node_1 = LNode(1)
#head = node_1
#p = head
#for i in range(2,11):
#    p._next = LNode(i)
#    p = p._next
#
#p = node_1
#while p:
#    print(p._data)
#    p = p._next
    
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
     
    def for_each(self,proc):
        p = self._head 
        while p:
            proc(p._data)
            p = p._next
    
    def elements(self):
        p = self._head
        while p:
            yield p._data
            p = p._next
