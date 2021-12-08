# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 09:56:03 2021

@author: danny
"""

n=int(input('輸入整數'))
prime=[2]

for i in range(3,n):
    for num in prime:
        if(i%num==0):
            break
        if num==prime[-1]:
            prime.append(i)
print(prime)
        