# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:16:57 2020

@author: danny
"""

n=int(input('輸入正整數:'))
ans=0
for i in range(1,n+1):
    ans=i*i+ans#計算1到n的平方和
print(ans)