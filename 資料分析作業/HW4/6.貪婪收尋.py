# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:31:51 2021

@author: danny
"""

import re
msg='sonsonsonsonson'#測試用句子
pattern='(son){3,5}'#3~5個重複
print('最短:',re.search(pattern+'?',msg).group())#找重複出現最少
print('最長:',re.search(pattern,msg).group())#找重複最多