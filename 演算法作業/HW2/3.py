# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:20:52 2020

@author: danny
"""
def setarray():
    print('1.設定陣列大小')
    m=input('m行')
    n=input('n列')
    #輸入陣列數值
    nums=[]
    print('1.輸入陣列數值')
    for i in range(int(n)):
        row=[]
        for j in range(int(m)):
            row.append(int(input('輸入數值:')))
        nums.append(row)
    return nums
def display(nums):
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            print(nums[i][j],end=' ')
        print()
#相加
def add(nums1,nums2):
    nums_add=[]
    for i in range(len(nums1)):
        row=[]
        for j in range(len(nums1[0])): 
            row.append(nums1[i][j]+nums2[i][j])
        nums_add.append(row)
    return nums_add
#內積
def dot(nums1,nums2):
    nums_dot=[]
    for i in range(len(nums1)):
        row=[]
        for j in range(len(nums1[0])): 
            row.append(nums1[i][j]*nums2[i][j])
        nums_dot.append(row)
    return nums_dot
#外積
def cross(nums1,nums2):
    nums_cross=[]
    for i in range(len(nums1)):
        row=[]
        for j in range(len(nums1[0])): 
            temp=0
            for k in range(len(nums1)):
                temp+=nums1[k][j]*nums2[i][k]
            row.append(temp)
        nums_cross.append(row)
    return nums_cross
'''
nums1=setarray()
nums2=setarray()
'''
nums1=[[1,2],[1,2]]
nums2=[[1,2],[1,2]]
print('nums1:')
display(nums1)
print('nums2:')
display(nums2)
nums=add(nums1,nums2)
print('add:')
display(nums)
nums=dot(nums1,nums2)
print('dot')
display(nums)
nums=cross(nums1,nums2)
print('cross')
display(nums)

