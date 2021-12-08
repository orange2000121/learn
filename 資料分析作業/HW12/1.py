# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:50:07 2020

@author: danny
"""
import matplotlib.pyplot as plt


Benz= [3367,4120,5539,6020,6620]
BMW=  [4000,3590,4423,4900,4590]
Lexus=[5200,4930,5350,6200,6930]
year= [2018,2019,2020,2021,2022]
#建立圖表大小
plt.figure(figsize=(15,10),dpi=100,linewidth=2)
#設定資料,顏色，label
plt.plot(year,Benz,color='r',label='Benz')
plt.plot(year,BMW,color='b',label='BMW')
plt.plot(year,Lexus,color='g',label='Lexus')
#標題
plt.title('銷售圖表',x=0.5,y=1.03)
#刻度字體大小
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#標籤字體大小
plt.xlabel('Year',fontsize=30,labelpad=15)
plt.ylabel('銷售量',fontsize=30,labelpad=20)
#顯示出線條標記位置
plt.legend(loc='best',fontsize=20)
#繪圖
plt.show()
