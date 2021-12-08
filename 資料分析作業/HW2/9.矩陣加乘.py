# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:24:30 2021

@author: danny
"""

import numpy as np
def array(a):
    a=np.array(a)
    a=a.reshape((3,3))
    return a
a=[1,2,3,4,2,3,4,2,3]
b=[1,2,3,4,8,3,5,2,4]
print('矩陣a')
for i in range(9):
    a.append(int(input('輸入整數')))
print('矩陣b')
for i in range(9):
    b.append(int(input('輸入整數')))
a=array(a)
b=array(b)
print('a=\n',a)
print('b=\n',b)
print('a+b=\n',a+b)
print('a*b=\n',a*b)