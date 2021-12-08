# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:23:03 2020

@author: danny
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-6,6,0.1)
x_label=np.arange(-6,7,1)
f1=3*np.sin(x)
f2=np.sin(x)
f3=0.2*np.sin(x)
#建立圖表大小
plt.figure(figsize=(15,10),dpi=100,linewidth=2)
#設定資料,顏色，label
plt.plot(x,f1,color='r',label='f1')
plt.plot(x,f2,color='b',label='f2')
plt.plot(x,f3,color='g',label='f3')
#標題
plt.title('銷售圖表',x=0.5,y=1.03)
#刻度字體大小
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#標籤字體大小
plt.xlabel('',fontsize=30,labelpad=15)
plt.ylabel('銷售量',fontsize=30,labelpad=20)
#顯示出線條標記位置
plt.legend(loc='best',fontsize=20)
#繪圖
plt.show()