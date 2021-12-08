# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:06:15 2021

@author: danny
"""
a=[]
for i in range(3):
    temp=[]
    for j in range(3):
        temp.append(int(input('a(%d,%d)='%(i,j))))
    a.append(temp)
print('max=',int(a.index((max(a)))/3),int(a.index((max(a)))%3))
print('min=',int(a.index((min(a)))/3),int(a.index((min(a)))%3))