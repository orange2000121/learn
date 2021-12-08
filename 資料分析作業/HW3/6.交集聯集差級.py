# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:42:36 2021

@author: danny
"""
a=[x for x in range(1, 100,2)]
b=[x for x in range(101,5)]
交集=set(a) & set(b)
ab差集=set(a)-set(b)
ba差集=set(b)-set(a)
ab對稱差集=set(a)^set(b)
ba對稱差集=set(b)^set(a)
print('交集',交集)
print('ab差集',ab差集)
print('ba差集',ba差集)
print('ab對稱差集',ab對稱差集)
print('ba對稱差集',ba對稱差集)
      