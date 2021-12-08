# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:23:26 2020

@author: danny
"""

class Shape:
    def __init__(self,name,len):
        self.name=name
        self.len=len
    def length(self):
        return self.round
class Tri(Shape):
    def display(self):
        self.round=0
        print(self.name,end=' ')
        for i in self.len:
            self.round+=i
        print('周常為:',self.round)
class Rec(Shape):
    def display(self):
        self.round=0
        print(self.name,end=' ')
        self.round=(self.len[0]+self.len[1])*2
        print('周常為:',self.round)
class Cir(Shape):
    def display(self):
        self.round=0
        print(self.name,end=' ')
        self.round=3.14*self.len*self.len
        print('周常為:',self.round)

s1=Tri('三角形',[10,5,4])
s1.display()
print(s1.length())

s2=Rec('長方形',[10,5])
s2.display()
print(s2.length())

s3=Cir('circle',5)
s3.display()
print(s3.length())