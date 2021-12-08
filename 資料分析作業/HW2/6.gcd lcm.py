# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:05:36 2021

@author: danny
"""

def gcd(a,b):
    while b!=0 :
        r=a%b
        a=b
        b=r
    return a
def lcm(a,b):
    return a*b/gcd(a,b)
a=int(input('a='))
b=int(input('b='))
print('gcd(',a,',',b,')=',gcd(a,b))
print('lcm(',a,',',b,')=',lcm(a,b))