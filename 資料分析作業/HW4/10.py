# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:29:08 2021

@author: danny
"""

import re
msg= '''txt@deepstone.com.tw kkk@gmail.com abc@me.com mymail@qq.com abc@abc@abc'''
pattern='\w+@\w+\.\w+\.?\w?'#括號可有殼無，-可有可無，第一串數字需要為二，最後需要有7~8字
print(re.findall(pattern,msg))