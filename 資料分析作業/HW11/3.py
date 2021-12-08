# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 16:58:38 2021

@author: danny
"""

import numpy as np

a=np.array([[2,2],[2,2],[2,2]])
b=np.array([[1,4],[2,5],[3,6]])
print('加法 :\n',a+b)
print('減法 :\n',a-b)
print('乘法 :\n',a*b)
print('除法 :\n',a/b)
print('餘數 :\n',a%b)
print('A轉至矩陣 :\n',np.transpose(a))
print('B轉至矩陣 :\n',np.transpose(b))