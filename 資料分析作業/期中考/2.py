# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 10:33:29 2021

@author: danny
"""

import re
number=input('輸入電話號碼:')
rule=re.compile(r'\d{4}-\d{3}-\d{3}')#建立正規表示式
if rule.search(number):#判斷有沒有符和正則表示式
       print('是台灣號碼')
else:
    print('不是台灣號碼')