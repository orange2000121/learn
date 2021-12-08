# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:09:51 2020

@author: danny
"""
import matplotlib.pyplot as plt
import numpy as np
contry=['America','Australia','Japan','Europe','United Kingdom']
students=[10549,2105,1190,3346,980]
plt.figure(figsize=(6,9))    # 顯示圖框架大小

labels = contry    # 製作圓餅圖的類別標籤
separeted = (0, 0, 0.3, 0, 0)                  # 依據類別數量，分別設定要突出的區塊
size = students                       # 製作圓餅圖的數值來源

plt.pie(size,                           # 數值
        labels = labels,                # 標籤
        autopct = "%1.1f%%",            # 將數值百分比並留到小數點一位
        explode = separeted,            # 設定分隔的區塊位置
        pctdistance = 0.6,              # 數字距圓心的距離
        textprops = {"fontsize" : 12},  # 文字大小
        shadow=True)                    # 設定陰影

 
plt.axis('equal')                                          # 使圓餅圖比例相等
plt.legend(loc = "best")                                   # 設定圖例及其位置為最佳
