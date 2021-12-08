# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:15:21 2021

@author: danny
"""

from PIL import Image
picobj=Image.new('RGB',(300,180),'LightGreen')#建立淡綠色矩形
picobj.save('out.jpg')
