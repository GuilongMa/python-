# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 14:27:43 2018

@author: qzxy
"""
import re,collections

with open('a.txt','r') as f:
    d = collections.Counter([])
    while True:
        line = f.readline().lower()
        if not line:
            break
        words = re.findall(r'\w+[-\']?\w*',line)
        print(words)
#        d = {}
#        for w in words:
#            if w in d:
#                d[w]+=1
#            else:
#                d[w]=1
#        d1 = d
        d1=collections.Counter(words)
        d +=d1
    print(d)
    print(d.most_common(3))
        
        
        
        
    
