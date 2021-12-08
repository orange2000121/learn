# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:23:25 2020

@author: danny
"""

import numpy as np
a=np.arange(1,13,1)
a=a.reshape(3,4)
print('before')
print(a)
a=a*3
print('after')
print(a)