# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:39:34 2021

@author: danny
"""
# numlist=[1,1,1,2,3,4,9,5,7,3,6]
def average(numlist):
    count=0
    for num in numlist:
        count+=num
    return count/len(numlist)
def Mode(numlist):
    temp={}
    for num in numlist:
        if num not in temp:
            temp[str(num)]=1
        else:
            temp[str(num)]+=1
    max=0
    for i in temp:
        if temp[i]>max:
            max=temp[i]
            maxnum=i
    return int(maxnum)
def median(numlist):
    for i in range(len(numlist)):#氣泡排序法
        for j in range(i+1,len(numlist)):
            if(numlist[i]>numlist[j]):
                temp=numlist[i]
                numlist[i]=numlist[j]
                numlist[j]=temp
    if len(numlist)%2:
        return numlist[int(len(numlist)/2)+1]
    else:
        return (numlist[int(len(numlist)/2)]+numlist[int(len(numlist)/2)+1])/2
numlist=[]
for i in range(10):
    numlist.append(int(input('輸入整數:')))
print('numlist=',numlist)
print('平均數')
print(average(numlist))
print('中位數:')
print(median(numlist))
print('眾數:')
print(Mode(numlist))