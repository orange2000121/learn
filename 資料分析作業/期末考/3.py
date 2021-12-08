# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:24:20 2021

@author: danny
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,100)#-10到10  100份
y1=x
y2=x**2#平方
y3=x**3#次方
y4=x**4#4次方
plt.subplot(2,2,1)#第一個圖
plt.plot(x,y1)
plt.subplot(2,2,2)#第二個圖
plt.plot(x,y2)
plt.subplot(2,2,3)#第三個圖
plt.plot(x,y3)
plt.subplot(2,2,4)#第四個圖
plt.plot(x,y4)
plt.show()