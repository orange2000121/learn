# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 09:47:41 2021

@author: danny
"""

num=[]
for i in range(10):
    num.append(int(input('輸入整數')))
odd=0
even=0
for i in num:
    if i%2:
        odd+=1
    else:
        even+=1
print('偶數個數:',even)
print('奇數個數:',odd)