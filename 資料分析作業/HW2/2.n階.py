# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 09:40:41 2021

@author: danny
"""

n=int(input('輸入整數'))
num=1
for i in range(1,n+1):
    num*=i
print('n!=',end='')
print(num)