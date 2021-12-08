# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:22:35 2021

@author: danny
"""

import re
msgs=['son','sonson','sonsonson','sonsonsonson','sonsonsonsonson','sonsonsonsonsonson']#測試用句子
pattern1='(son){2,}'
pattern2='(son){,5}'
print('以下用pattern1%s收尋'%(pattern1))
for msg in msgs:
    txt=re.search(pattern1,msg)#第一種方式搜尋
    if txt:
        print('收尋成功:',txt.group())
    else:
        print('收尋失敗')
print('以下用pattern2%s收尋'%(pattern2))
for msg in msgs:
    txt=re.search(pattern2,msg)#第二種方式收尋
    if txt:
        print('收尋成功:',txt.group())
    else:
        print('收尋失敗')   
        
