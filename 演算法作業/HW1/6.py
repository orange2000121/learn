# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:36:56 2020

@author: danny
"""

import exlotto as lot#載入自建函數

def bubble(nums):#氣泡排序
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if(nums[i]>nums[j]):
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
    return nums

nums=lot.lotto(48,5)
nums=bubble(nums)
print(nums)
