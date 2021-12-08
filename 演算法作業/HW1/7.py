# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:48:42 2020

@author: danny
"""

class Shape:
    def __init__(self,name,len):
        self.name=name
        self.len=len
    def length(self):
        return 
class Tri(Shape):
    def display(self):
        round=0
        print(self.name,end=' ')
        for i in self.len:
            round+=i
        print('周常為:',round)

s1=Tri('三角形',[10,5,4])
s1.display()