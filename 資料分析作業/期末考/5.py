# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:11:36 2021

@author: danny
"""

import numpy as np
import matplotlib.pyplot as plt

with open('input.csv','r') as f:
    text=f.readlines()

x=[]
y=[]
for i in text:
    print(i)
    x.append(i.split(',')[0])
    y.append(float(i.split(',')[1]))
plt.plot(x,y)
plt.show()