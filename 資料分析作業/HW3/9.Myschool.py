# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:03:02 2021

@author: danny
"""

class Myschool:
    def __init__(self,title):
        self.title=title
    def departments(self):
        return['電機','資工','化工']
school=Myschool('東海大學')
print(school.departments())
            
        