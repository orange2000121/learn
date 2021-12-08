# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:26:27 2020

@author: danny
"""
import random
def lotto(n,m):
    nums=[]
    for i in range(m):
        nums.append(random.randint(1,n))
    return nums