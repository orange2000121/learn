# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 09:29:03 2021

@author: danny
"""

num=[]
for i in range(3):
    num.append(int(input('輸入正數'))) 
for i in range(len(num)):#氣泡排序法
    for j in range(i+1,len(num)):
        if(num[i]>num[j]):
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
print('由大至小')
for i in range(len(num)-1,-1,-1):
    print(num[i])
print('由小至大')
for i in num:
    print(i)