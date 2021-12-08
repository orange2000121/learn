# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:14:17 2021

@author: danny
"""

def compute(a,b,c):
    if b**2-4*a*c<0:
        return '無解'
    elif b**2-4*a*c==0:
        return (-b+(b**2-4*a*c)**0.5)/(2*a)
    else:
        root1=(-b+(b**2-4*a*c)**0.5)/(2*a)
        root2=(-b-(b**2-4*a*c)**0.5)/(2*a)
        return [root1,root2]
a=int(input('輸入整數'))
b=int(input('輸入整數'))
c=int(input('輸入整數'))
print('解:',compute(a,b,c))