# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:21:22 2020

@author: danny
"""
#相加
def add(a,b):
    c=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            c[i][j]=a[i][j]+b[i][j]
    return c
#內積
def dot(a,b):
    c=0
    for i in range(2):
        for j in range(2):
            c+=a[i][j]*b[i][j]
    return c
#外積
def cross(a,b):
    c=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            c[i][j]=a[0][j]*b[i][0]+a[1][j]*b[i][1]
    return c
a=[[0,0],[0,0]]
b=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        a[i][j]=int(input('a.輸入整數:'))
for i in range(2):
    for j in range(2):
        b[i][j]=int(input('b.輸入整數:'))
print('相加:',add(a,b))
print('內積:',dot(a,b))
print('外積:',cross(a,b))