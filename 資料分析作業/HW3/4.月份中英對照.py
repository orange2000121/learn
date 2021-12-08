# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:09:33 2021

@author: danny
"""
month={'一月':'January',
        '二月':'February',
        '三月':'March',
        '四月':'April',
        '五月':'May',
        '六月':'June',
        '七月':'July',
        '八月':'August',
        '九月':'September',
        '十月':'October',
        '十一月':'November',
        '十二月':'December'}
tra='1'
while tra!='0':
    tra=input('輸入月份中文:')
    if tra in month:#判斷輸入的英文有沒有在month裡面
        print(month[tra])
    else:#如果沒在month裡面輸出error
        print('error')
