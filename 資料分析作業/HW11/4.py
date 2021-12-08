# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:06:42 2021

@author: danny
"""

import numpy as np


with open('weatherTaipei.txt','r') as f:
    text=f.readlines()
temperature=[]
for temp in text[1:len(text)-1]:
    temperature.append(int(temp.split(',')[1]))
    temperature.append(int(temp.split(',')[2].split('\n')[0]))
print('最高溫度 : ',np.max(temperature))
print('平均溫度 : ',np.mean(temperature))
