# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:54:17 2021

@author: danny
"""

Math =['Peter', 'Norton', 'Kevin', 'Mary', 'John', 'Ford', 'Nelson', 'Damon', 'Ivan', 'Tom']
Computer = ['Curry', 'James', 'Mary', 'Turisa', 'Tracy', 'Judy', 'Lee', 'Jarmul', 'Damon', 'Ivan']
Physics =['Eric', 'Lee', 'Kevin', 'Mary', 'Christy', 'Josh', 'Nelson', 'Kazil', 'Linda', 'Tom']
print('同時參加 Math 與 Computer:',set(Math)&set(Computer))
print('同時參加 Math 與 Physics:',set(Math)&set(Physics))
print('同時參加 Physics 與 Computer:',set(Computer)&set(Physics))