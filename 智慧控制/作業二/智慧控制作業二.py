# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 18:21:29 2021

@author: danny
"""
import math
import random
import matplotlib.pyplot as plt

# ----------------------------------- 訓練資料 ----------------------------------- #
input = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1,0, 1], [1, 1, 0], [1, 1, 1]]
target = [0, 0, 0, 1, 0, 1, 1, 1]
# --------------------------------- 設定Node數量 --------------------------------- #
Ninp = 3  # 輸入層數量
Nhid = 30  # 隱藏層數量
Nout = 1  # 輸出層數量
# ----------------------------------- 權重初始化 ---------------------------------- #
W_xh = []
W_hy = []
for i in range(Ninp):
    W_xh.append([])
    for h in range(Nhid):
        W_xh[i].append(random.uniform(-1, 1))
for h in range(Nhid):
    W_hy.append([])
    for j in range(Nout):
        W_hy[h].append(random.uniform(-1, 1))
# ---------------------------------- 偏權值初始化 ---------------------------------- #
theta_h = []
theta_y = []
for h in range(Nhid):
    theta_h.append(random.uniform(-1, 1))
for o in range(Nout):
    theta_y.append(random.uniform(-1, 1))
# ----------------------------------- 計算輸出值 ---------------------------------- #


def output(casenum=0):
    H = []  # 隱藏層輸出
    net_h = []
    for h in range(Nhid):
        temp = 0
        for i in range(Ninp):
            temp += W_xh[i][h] * input[casenum][i]
        net_h.append(temp + theta_h[h])
    for h in range(Nhid):
        H.append(1 / (1 + math.exp(-net_h[h])))
    Y = []  # 輸出層輸出
    for o in range(Nout):
        net_y = []
        for o in range(Nout):
            temp = 0
            for h in range(Nhid):
                temp += W_hy[h][o] * H[h]
            net_y.append(temp + theta_y[o])
    for o in range(Nout):
        Y.append(1 / (1 + math.exp(-net_y[o])))
    return H, Y


# ----------------------------------- 計算差距量 ---------------------------------- #


def error(casenum=0):
    H, Y = output(casenum)
    # 計算輸出層差距量
    delta_y = []
    for o in range(Nout):
        delta_y.append((target[casenum] - Y[o]) * Y[o] * (1 - Y[o]))
    # 計算隱藏層差距量
    delta_h = []
    for h in range(Nhid):
        temp = 0
        for o in range(Nout):
            temp += delta_y[o] * W_hy[h][o]
        delta_h.append(temp * H[h] * (1 - H[h]))
    return delta_h, delta_y, H, Y


# ---------------------------- 計算各層的加權值修正量及偏權值修正量 ---------------------------- #


def weight_update(casenum=0):
    learning_rate = 0.3
    delta_h, delta_y, H, Y = error(casenum)
    # print("weight_update : ", delta_h)
    # 隱藏層到輸出層的權重更新
    for h in range(Nhid):
        for o in range(Nout):
            W_hy[h][o] += learning_rate * delta_y[o] * H[h]
    # 隱藏層到輸出層的偏權值更新
    for o in range(Nout):
        theta_y[o] += -learning_rate * delta_y[o]
    # 輸入層到隱藏層的權重更新
    for i in range(Ninp):
        for h in range(Nhid):
            W_xh[i][h] += learning_rate * delta_h[h] * input[casenum][i]
    # 輸入層到隱藏層的偏權值更新
    for h in range(Nhid):
        theta_h[h] += -learning_rate * delta_h[h]


# ----------------------------------- 訓練 ---------------------------------- #
historyW_xh = []
historyW_hy = []
for i in range(500):
    for casenum in range(len(input)):
        weight_update(casenum)
        #儲存權重值歷史
        historyW_xh.append([])
        for i in range(len(W_xh)):
            for j in range(len(W_xh[0])):
                historyW_xh[len(historyW_xh)-1].append(W_xh[i][j])
        historyW_hy.append([])
        for i in range(len(W_hy)):
            for j in range(len(W_hy[0])):
                historyW_hy[len(historyW_hy)-1].append(W_hy[i][j])
# ----------------------------------- 測試 ---------------------------------- #
for i in range(len(input)):
    H, Y = output(i)
    if Y[0] > 0.5 and target[i] == 1 or Y[0] < 0.5 and target[i] == 0:
        print("輸入值:", input[i], "輸出值:", Y[0], "目標:", target[i], "TRUE")
    else:
        print("輸入值:", input[i], "輸出值:", Y[0], "目標:", target[i], "FALSE")

# 權重變化折線圖
for i in range(len(historyW_xh[0])):
    temp = []
    for j in range(len(historyW_xh)):
        temp.append(historyW_xh[j][i])
    plt.plot(range(1, len(historyW_xh) + 1), temp)
for i in range(len(historyW_hy[0])):
    temp = []
    for j in range(len(historyW_hy)):
        temp.append(historyW_hy[j][i])
    plt.plot(range(1, len(historyW_hy) + 1), temp)
plt.show()
