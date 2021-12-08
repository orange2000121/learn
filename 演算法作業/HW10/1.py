# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 17:10:28 2020

@author: danny
"""

arr=[6, 7,1,5, 9,3, 8,4]
def merge(X, Y):
    " merge two sorted lists "
    p1 = p2 = 0
    out = []
    while p1 < len(X) and p2 < len(Y):
        if X[p1] < Y[p2]:
            out.append(X[p1])
            p1 += 1
        else:
            out.append(Y[p2])
            p2 += 1
    out += X[p1:] + Y[p2:]
    return out

def mergeSort(A):
    if len(A) <= 1:
        return A
    if len(A) == 2:
        return sorted(A)

    mid = int(len(A)/2)
    return merge(mergeSort(A[:mid]), mergeSort(A[mid:]))
arr=mergeSort(arr)
print(arr)
def binary_search(arr,num):
    if len(arr):
        mid=int(len(arr)/2)
        if num>arr[mid]:
            binary_search(arr[mid+1:],num)
        elif num<arr[mid]:
            binary_search(arr[:mid],num)
        else:
            print(num,'存在')
            return
    else:
        print(num,'不存在')
binary_search(arr,2)
binary_search(arr,8)