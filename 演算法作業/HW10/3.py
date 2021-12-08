# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 17:53:19 2020

@author: danny
"""

def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fib(num-1)+fib(num-2)
for i in range(10):
    print(fib(i))