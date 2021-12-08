# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:43:17 2021

@author: danny
"""

import numpy as np

randomnum=[]
for i in range(15):
    randomnum.append(np.random.randint(5,16))
randomnum=np.array(randomnum)
x=randomnum.reshape(3,5)
print('最大值 : ',np.max(x))
print('最小值 : ',np.min(x))
print('總和 : ',np.sum(x))
print('平均 : ',np.mean(x))
print('四個角落元素 : ',x[0,0],x[0,4],x[2,0],x[2,4])
with open('EX3_2.txt','w') as f:
    f.write(str(x[0,0])+str(x[0,4])+str(x[2,0])+str(x[2,4]))
print('Y :\n',x)
print('Z :\n',x+x)