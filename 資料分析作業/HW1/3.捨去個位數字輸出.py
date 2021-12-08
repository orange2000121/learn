# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:01:44 2021

@author: danny
"""

num=int(input('輸入三位數:'));#輸入三位數
num-=num%10;#求除十的餘數減掉
print(num);#輸出答案