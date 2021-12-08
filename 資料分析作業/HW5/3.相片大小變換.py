# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:28:29 2021

@author: danny
"""

from PIL import Image
photosticker=Image.open('photosticker.jpeg')
width,height=photosticker.size
newpic=photosticker.resize((int(width*1.2),height))#調整寬高
newpic.save('3-1.jpg')#存檔

newpic=photosticker.resize((int(width*1.5),height))#調整寬高
newpic.save('3-2.jpg')#存檔

newpic=photosticker.resize((int(width*0.5),height))#調整寬高
newpic.save('3-3.jpg')#存檔

newpic=photosticker.resize((int(width*0.8),height))#調整寬高
newpic.save('3-4.jpg')#存檔

newpic=photosticker.resize((width,int(height*1.2)))#調整寬高
newpic.save('3-5.jpg')#存檔

newpic=photosticker.resize((width,int(height*1.5)))#調整寬高
newpic.save('3-6.jpg')#存檔

newpic=photosticker.resize((width,int(height*0.5)))#調整寬高
newpic.save('3-7.jpg')#存檔

newpic=photosticker.resize((width,int(height*0.8)))#調整寬高
newpic.save('3-8.jpg')#存檔