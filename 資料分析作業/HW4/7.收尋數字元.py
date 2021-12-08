# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:35:55 2021

@author: danny
"""

import re
msg='1 cat,2 dogs,3 pigs,3 swans'#測試用句子
pattern='\d\ \w{3,5}'#建立pattern
print(re.findall(pattern,msg))#收尋所有