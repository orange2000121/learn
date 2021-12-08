# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:08:25 2021

@author: danny
"""

class Myschool:
    def __init__(self,title):
        self.title=title
    def departments(self):
        self.subject=['電機','資工','化工']
        return self.subject
    def add(self,addsuject):
        self.subject.append(addsuject)
        return self.subject
    def omit(self,omitsubject):
        self.subject.remove(omitsubject)
        return self.subject
school=Myschool('東海大學')
print(school.departments())
print('新增工工',school.add('工工'))
print('刪除電機',school.omit('電機'))