# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:27:27 2021

@author: danny
"""

money=int(input('消費金額:'));#輸入消費金額
if(money>100000):#如果大於100000
    print('折扣後消費金額:',money-money*0.15);#輸出15%off
elif(money>50000):#如果大於50000
    print('折扣後消費金額:',money-money*0.1);#輸出10%off
elif(money>10000):#如果大於10000
    print('折扣後消費金額:',money-money*0.05);#輸出5%off
else:
    print('消費金額:',money)