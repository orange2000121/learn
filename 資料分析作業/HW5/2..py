# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:21:24 2021

@author: danny
"""

from PIL import Image,ImageColor
picobj=Image.open('out.jpg')
for x in range(50,151):#x範圍
    for y in range(10,50):#y範圍
        picobj.putpixel((x,y),ImageColor.getcolor('Blue','RGBA'))#填顏色
for x in range(50,151):#x範圍
    for y in range(50,100):#y範圍
        picobj.putpixel((x,y),ImageColor.getcolor('Red','RGBA'))#填顏色
picobj.save('out1.jpg')#存檔