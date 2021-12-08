# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:41:22 2021

@author: danny
"""

import re
msgs=['0932895453','093289ss53']#測試用句子
pattern='\d{10}'#必須府和10個都是數字
for msg in msgs:
    txt=re.search(pattern,msg)
    if txt:
        print('收尋成功:',txt.group())
    else:
        print(msg,'非全部是數字')