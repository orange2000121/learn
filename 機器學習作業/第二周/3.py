# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:22:03 2020

@author: danny
"""

a=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        a[i][j]=int(input('a.輸入整數:'))
max=a[0][0]#最大值
min=a[0][0]#最小值
maxseat=[0,0]#最大值的位置
minseat=[0,0]#最小值的位置
for i in range(3):
    for j in range(3):
        if(max<a[i][j]):
            max=a[i][j]
            maxseat=[i,j]
        if(min>a[i][j]):
            min=a[i][j]
            minseat=[i,j]
print('max:',maxseat)
print('min:',minseat)