# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:19:00 2020

@author: danny
"""

m=int(input('輸入整數m:'))#輸入一個整數m行
n=int(input('輸入整數n:'))#輸入一個整數n行
ch=input('要顯示的字元:')#詩入藥顯示的字元
for i in range(n):
    for j in range(m):
        print(ch,end='')
    print()#每m個跳行