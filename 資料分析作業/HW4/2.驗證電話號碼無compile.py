# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:38:25 2021

@author: danny
"""
import re
msgs=['Please call my secretary using 0930-919-919 or 0952-001-001',
     '請明天17:30和我一起參加明志科大教師節晚餐',
     '請明天17:30和一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我']#測試用句子
for msg in msgs:
    phone=re.search(r'\d{4}-\d{3}-\d{3}',msg)#收尋第一個出現府和的句字
    if phone:
        print('電話號碼是:',phone.group())
    else:
        print(msg,'字串不含電話號碼')