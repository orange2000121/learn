# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:29:17 2020

@author: danny
"""

import numpy as np
A=np.ones((3,2))*2
B=np.array([[1,4],[2,5],[3,6]])
print('A:\n',A)
print('B:\n',B)
print('A+B:\n',A+B)
print('A-B:\n',A-B)
print('A*B:\n',A*B)
print('A/B:\n',A/B)
print('A轉至:\n',A.transpose())
print('B轉至:\n',B.transpose())