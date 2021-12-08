# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:04:07 2021

@author: danny
"""

from PIL import Image
pic=Image.open('photosticker.jpeg')
pic=pic.resize((50,50))
picobj=Image.new('RGB',(420,220),'Yellow')
for i in range(4):
    for j in range(8):
        x=j*50+10
        y=i*50+10
        picobj.paste(pic,(x,y))
picobj.save('myfig1.jpg')
