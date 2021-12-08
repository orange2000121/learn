# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 10:45:42 2021

@author: danny
"""

from PIL import Image,ImageDraw
newimage=Image.new('RGB',(300,300),'Red')
drawobj=ImageDraw.Draw(newimage)
for x in range(100,200,3):
    for y in range(100,200,3):
        drawobj.point([(x,y)],fill='Black')
        
drawobj.line([(0,0),(299,0),(299,299),(0,299),(0,0)],fill='Black')#
for x in range(150,300,10):
    drawobj.line([(x,0),(300,x-150)],fill='Blue')#左上外框
for x in range(150,-1,-10):
    drawobj.line([(x,0),(0,150-x)],fill='Blue')#右上外框
for y in range(150,300,10):
    drawobj.line([(0,y),(y-150,300)],fill='Blue')#左下外框
for y in range(300,149,-10):
    drawobj.line([(y,300),(300,450-y)],fill='Blue')#右下外框
newimage.save('3.jpg')