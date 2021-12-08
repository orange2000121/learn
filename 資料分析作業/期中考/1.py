# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 10:14:02 2021

@author: danny
"""

def factorial(n):#計算階乘
    num=1
    for i in range(2,n+1):
        num*=int            #從1乘到n
    return num
x=int(input('輸入整數x'))
n=int(input('輸入整數n'))
num=0
    
for i in range(n+1):
    num+=(x**i)/(factorial(i))#公式
print(num)