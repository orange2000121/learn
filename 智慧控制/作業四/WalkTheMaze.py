import numpy as np
from random import randrange
from matplotlib import pyplot as plt
maze = np.array(
    [
        [-1, -1, -1, -1, -1, -1],
        [-1, 0, 0, 100, 0, -1],
        [-1, -1, 0, -1, 0, -1],
        [-1, 0, 0, 0, 0, -1],
        [-1, 0, -1, -1, 0, -1],
        [-1, 0, -1, 0, 0, -1],
        [-1, 0, -1, 0, -1, -1],
        [-1, 0, 0, 0, 0, -1],
        [-1, -1, -1, -1, -1, -1],
    ]
)  # 地圖設定
Q = np.zeros((maze.shape[0], maze.shape[1], 4))  # Q值設定
epoc = 100  # 訓練回数
step = 1000  # 步數
beta = 0.9  # 學習率
gamma = 0.9  # 獎勵因子
stepHistory = []  # 步數記錄
start = np.array([7, 1])  # 起始點
for round in range(epoc):
    lastStatus = start  # 上一狀態
    countStep = 0
    for i in range(step):
        directionArray = np.where(Q[lastStatus[0], lastStatus[1], :] == np.max(Q[lastStatus[0], lastStatus[1], :]))  # 取得最大Q值的方向
        direction = directionArray[0][randrange(0, len(directionArray[0]))]  # 隨機選擇方向
        # print("第", round + 1, "輪，第", i + 1, "步，方向 : ", direction)
        # 執行方向
        if direction == 0:
            currentStatus = np.array([lastStatus[0] - 1, lastStatus[1]])
        elif direction == 1:
            currentStatus = np.array([lastStatus[0] + 1, lastStatus[1]])
        elif direction == 2:
            currentStatus = np.array([lastStatus[0], lastStatus[1] - 1])
        elif direction == 3:
            currentStatus = np.array([lastStatus[0], lastStatus[1] + 1])
        # 更新Q值
        lestQ = Q[lastStatus[0], lastStatus[1], direction]
        currentMaze = maze[currentStatus[0], currentStatus[1]]
        currentQ = Q[currentStatus[0], currentStatus[1], np.argmax(Q[currentStatus[0], currentStatus[1], :])]
        Q[lastStatus[0], lastStatus[1], direction] = lestQ + beta * (currentMaze + gamma * currentQ - lestQ)
        countStep += 1
        if currentMaze == -1:
            continue
        elif currentMaze == 100:
            print("Success")
            break
        lastStatus = currentStatus
    print("總步數 : ", countStep)
    stepHistory.append(countStep)
plt.plot(stepHistory)
plt.show()
print(Q)
