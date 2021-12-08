# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:08:23 2021

@author: danny
"""

import re
msg='我喜歡看小龍女與楊過,不僅因為小龍女美麗,楊過在戲中所扮演的角色更是讓我喜歡'#測試用句子

while 1:
    find=input('收尋字串:')
    num=len(re.findall(find,msg))#計算所有收尋到的句子總數
    print('所收尋字串: ',find,end=' ')
    print('共出現%d次' %(num))
    if input('y繼續')!='y':
        break