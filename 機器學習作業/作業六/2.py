# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:53:38 2020

@author: danny
"""

def sensor(x1,x2,b):
    if x1+x2+b<=0:
        return 0
    else:
        return 1

x1=[0,0,1,1]
x2=[0,1,0,1]
for i in range(4):
    h1=sensor(x1[i],x2[i],-0.5)
    h2=sensor(x1[i],x2[i],-1.5)
    o1=sensor(h1,-h2,-0.5)
    print('(%d,%d)->%d'%(x1[i],x2[i],o1))
