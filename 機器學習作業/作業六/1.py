# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:20:53 2020

@author: danny
"""

import matplotlib.pyplot as plt 
import numpy as np 
  
x = np.linspace(-6, 6, 100) 
S = 1/(1 + np.exp(-x)) 
R=[]
for num in x:
    if(num>0):
        R.append(num)
    else:
        R.append(0)
R=np.array(R)
T=np.tanh(x)
plt.subplot(3,1,1)
plt.plot(x, S) 
plt.xlabel("x") 
plt.ylabel("Sigmoid(X)") 

plt.subplot(3,1,2)
plt.plot(x, R) 
plt.xlabel("x") 
plt.ylabel("ReLU(X)") 

plt.subplot(3,1,3)
plt.plot(x, T) 
plt.xlabel("x") 
plt.ylabel("Tanh(X)") 
plt.show() 