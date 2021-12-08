# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:04:49 2021

@author: danny
"""

import math
import matplotlib.pyplot as plt
# w1=0.5
# w2=0.5
# b=-0.5
#x1,x2,uot
datas=[[0.0,0.0,0.0],[1.0,0.0,1.0],[0.0,1.0,1.0],[1.0,1.0,1.0]]
historyw1=[]
historyw2=[]
def trainModel(datas,iniw1,iniw2,inib):
    # ---------------------------- 訓練五回，一回四筆資料，總共訓練二十次 --------------------------- #
    for i in range(5):
        for data in datas:
            x1=data[0]
            x2=data[1]
            out=(iniw1*x1)+(iniw2*x2)+inib#計算結果
            # ------------------------------ 判斷計算結果與目標結果是否相同 ----------------------------- #
            # --------------------------------- 不相同時調整權重 --------------------------------- #
            if(out>0 and data[2]<0.5):
                if(x1!=0):
                    iniw1+=(data[2]-out)/0.1#輸入不等於0時調整權重
                if(x2!=0):
                    iniw2+=(data[2]-out)/0.1
                inib=stable_sigmoid(inib+(data[2]-out)/0.001)
            elif(out<=0 and data[2]>0.5):#計算與目標結果不相同
                if(x1!=0):
                    iniw1+=(data[2]-out)/0.1
                if(x2!=0):
                    iniw2+=(data[2]-out)/0.1
                inib=stable_sigmoid(inib+(data[2]-out)/0.001)
            # --------------------------------- 顯示每次計算的變量 -------------------------------- #
            print('out=',out,',x1',x1,',x2',x2,',data[2]=',data[2],',i=',i)
            print('w1',iniw1,',w2',iniw2,',b',inib)
            # ---------------------------------- 紀錄全種變化 ---------------------------------- #
            historyw1.append(iniw1)
            historyw2.append(iniw2)
    return iniw1,iniw2,inib

def stable_sigmoid(x):
    if x >= 0:
        z = math.exp(-x)
        sig = 1 / (1 + z)
        return sig
    else:
        z = math.exp(x)
        sig = z / (1 + z)
        return sig
# ---------------------------------- 呼叫訓練模型 ---------------------------------- #
# ---------------------------- w1=-3，w2=-0.91，b=9 --------------------------#
w1,w2,b=trainModel(datas,-3.0,-0.91,9)
print('w1=',w1)
print('w2=',w2)
print('b=',b)
# ----------------------------------- 驗證結果 ----------------------------------- #
for data in datas:
    print()
    out=data[0]*w1+data[1]*w2+b
    if(out>0 and data[2]>0.5):
        print('data : ',data)
        print('out : ',out)
        print(True)
    elif(out<=0 and data[2]<=0.5):
        print('data : ',data)
        print('out : ',out)
        print(True)
    else:
        print('data : ',data)
        print('out : ',out)
        print(False)

plt.plot(range(1,len(historyw1)+1),historyw1)
plt.plot(range(1,len(historyw2)+1),historyw2)
plt.show()



























