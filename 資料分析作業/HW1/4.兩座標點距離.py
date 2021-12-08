# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:04:07 2021

@author: danny
"""
import math;
x1=float(input('x1='));#點一
y1=float(input('y1='));#點一
x2=float(input('x2='));#點二
y2=float(input('y2='));#點二
length=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));#機算最短距離
print('最短距離:',length);#輸出答案