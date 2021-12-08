# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:49:53 2021

@author: danny
"""

import json
allpeoplenumber=0
with open("populations.json","r") as f:
    datas = json.load(f)
for data in datas:
    # print(data)
    if(data['Year']=='2000'):
        if data['Country Name']!='World':
            print(data['Country Name'],':',data['Numbers'])
            allpeoplenumber+=float(data['Numbers'])
print('總人口:',allpeoplenumber)