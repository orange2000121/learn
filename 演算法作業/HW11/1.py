# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 14:20:02 2021

@author: danny
"""

def knapsack(W,wt,val):
    n=len(val)
    table=[[0 for x in range(W+1)] for x in range(n+1)]
    for r in range(n+1):
        for c in range(W+1):
            if r==0 or c==0:
                table[r][c]=0
            elif wt[r-1]<=c:
                table[r][c]=max(val[r-1]+table[r-1][c-wt[r-1]],table[r-1][c])
            else:
                table[r][c]=table[r-1][c]
    return table[n][W]

weight=[5,3,2,2,3,1]
value=[800,200,600,700,400,100]
bag_weight=5
print('最高價值:',knapsack(bag_weight,weight,value))
