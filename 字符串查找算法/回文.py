# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 18:59:34 2018

@author: qzxy
"""


# 递归实现回文,分治策略
def isPalindrome(s):
    """假设s是字符串
        如果是是回文字符串则返回True，否则返回False，
        忽略表达符号和空格和大小写
    """

    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))
