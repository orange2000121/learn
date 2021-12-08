# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:01:30 2020

@author: danny
"""
def display(nums):
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            print(nums[i][j],end=' ')
        print()
#設定m*n的陣列
print('設定陣列大小')
m=input('m行')
n=input('n列')
#輸入陣列數值
nums=[]
print('輸入陣列數值')
for i in range(int(n)):
    row=[]
    for j in range(int(m)):
        row.append(input('輸入數值:'))
    nums.append(row)
print('轉至前:')
display(nums)
change=[]
#行列交換
for i in range(int(m)):
    row=[]
    for j in range(int(n)):
        row.append(nums[j][i])
    change.append(row)
print('轉至後:')
display(change)