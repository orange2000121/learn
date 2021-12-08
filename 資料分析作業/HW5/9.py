# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:43:14 2021

@author: danny
"""

from PIL import Image,ImageDraw,ImageFont
pic=Image.open('myfig.jpg')
width,height=pic.size
picobj=Image.new('RGB',(width,height+200),'Yellow')
picobj.paste(pic)
drawpic=ImageDraw.Draw(picobj)
fontinfo=ImageFont.truetype('C:/Windows/Fonts/msjhbd.ttc',36)
drawpic.text(xy=(170,650),text='許子霆',fill='Blue',font=fontinfo)
picobj.save('myfig2.jpg')