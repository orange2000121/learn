# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:41:01 2020

@author: danny
"""
import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5, 6, 7, 8]
data2 = [1, 4, 9, 16, 25, 36, 49, 64]
data3 = [1, 3, 6, 10, 15, 21, 28, 36]
data4 = [1, 7, 15, 26, 40, 57, 77, 100]

fig,axes=plt.subplots(2,2)
axes[0][0].plot(data1)
axes[0][1].plot(data2)
axes[1][0].plot(data3)
axes[1][1].plot(data4)
fig.show