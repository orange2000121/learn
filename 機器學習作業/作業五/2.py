# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:24:00 2020

@author: danny
"""

x1=[0,0,1,1]
x2=[0,1,0,1]
out=[]
w1=1
w2=1
b=-0.5
for i in range(4):
    if w1*x1[i]+b+w2*x2[i]+b<=0:
        out.append(1)
    else:
        out.append(0)
print(out)