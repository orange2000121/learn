# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:05:05 2021

@author: danny
"""

from PIL import Image,ImageFilter
pic=Image.open('THU.jfif')
newpic=pic.filter(ImageFilter.BLUR)
newpic.save('7-1.jpg')
newpic=pic.filter(ImageFilter.EMBOSS)
newpic.save('7-2.jpg')
newpic=pic.filter(ImageFilter.CONTOUR)
newpic.save('7-3.jpg')
newpic=pic.filter(ImageFilter.FIND_EDGES)
newpic.save('7-4.jpg')
newpic=pic.filter(ImageFilter.DETAIL)
newpic.save('7-5.jpg')
newpic=pic.filter(ImageFilter.SMOOTH)
newpic.save('7-6.jpg')
newpic=pic.filter(ImageFilter.EDGE_ENHANCE)
newpic.save('7-7.jpg')
newpic=pic.filter(ImageFilter.SMOOTH_MORE)
newpic.save('7-8.jpg')
newpic=pic.filter(ImageFilter.EDGE_ENHANCE_MORE)
newpic.save('7-9.jpg')
newpic=pic.filter(ImageFilter.SHARPEN)
newpic.save('7-10.jpg')
