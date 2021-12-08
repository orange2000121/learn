# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 09:54:31 2021

@author: danny
"""

week={'monday':'星期一','tuesday':'星期二','wensday':'星期三','thusday':'星期四',
      'friday':'星期五','staday':'星期六','sunday':'星期日'}#宣告每個星期中英對照
tra='1'
while tra!='0':
    tra=input('輸入星期英文:')
    if tra in week:#判斷輸入的英文有沒有在week裡面
        print(week[tra])
    else:#如果沒在week裡面輸出error
        print('error')
