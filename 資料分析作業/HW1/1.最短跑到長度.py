# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 09:51:01 2021

@author: danny
"""

v=float(input('輸入初始速度:'));#輸入初始速度:
a=float(input('輸入初始加速度:'));#輸入初始加速度
length=(v*v)/2*a;#計算最短長度
print('最短跑到朝度:',length);#輸出計算結果
