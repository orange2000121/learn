# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:59:38 2020

@author: danny
"""
import numpy as np
A=[4,3,7,6,0,2]
B=[4,1,5,2,0,9]

#add
C=np.zeros(len(A))
C[0]=A[0]
for i in range(1,len(A)):
    C[i]=A[i]+B[i]
print(C)

#sub
C=np.zeros(len(A))
C[0]=A[0]
for i in range(1,len(A)):
    C[i]=A[i]-B[i]
print(C)

#乘法
C=np.zeros(A[0]+B[0]+1)
C[0]=A[0]+B[0]
for a in range(1,len(A)):
    for b in range(1,len(B)):
        C[9-a-b]+=A[a]*B[b]
print(C)