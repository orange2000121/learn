# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 09:43:30 2021

@author: danny
"""

n=int(input('輸入整數'))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end='  ')
    print()
