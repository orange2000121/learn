# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:49:38 2021

@author: danny
"""
import re


for i in range(3):
    number=input('輸入電話號碼:')
    rule=re.compile(r'\d{3}-\d{4}-\d{4}')#建立正規表示式
    if rule.search(number):#判斷有沒有符和正則表示式
        print('是大陸號碼')
    else:
        print('不是大陸號碼')
    
        