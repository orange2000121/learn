# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 10:48:47 2021

@author: danny
"""

class CRect:
    def __init__(self,width,height,length):
        self.width=width
        self.height=height
        self.length=length
    def computeArea(self):
        self.area=self.width*self.height#計算面積
    def computeVolume(self):
        self.volume=self.width*self.height*self.length#計算體積
    def show(self):
        self.computeVolume()
        self.computeArea()
        print('面積:',self.area)
        print('體積:',self.volume)
rec1=CRect(10,20,30)
rec2=CRect(40,20,60)
rec3=CRect(50,70,100)
rec1.show()
rec2.show()
rec3.show()