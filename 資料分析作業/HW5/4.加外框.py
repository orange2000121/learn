# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:42:40 2021

@author: danny
"""


from PIL import Image
pic=Image.open('photosticker.jpeg')
pic=pic.resize((350,500))
picobj=Image.new('RGB',(450,600),'Yellow')
picobj.paste(pic,(50,50))
picobj.save('myfig.jpg')