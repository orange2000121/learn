# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:55:24 2020

@author: danny
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
nums=np.zeros(11)
for i in range(1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    nums[dice1+dice2-2]+=1

plt.bar(range(2,13),
        nums,
        width=0.5, 
        bottom=None, 
        align='center', 
        color=['lightsteelblue', 
               'cornflowerblue', 
               'royalblue', 
               'midnightblue', 
               'navy', 
               'darkblue', 
               'mediumblue'])
plt.xticks(rotation='vertical')
plt.show()