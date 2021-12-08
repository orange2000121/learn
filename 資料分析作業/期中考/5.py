# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 11:21:20 2021

@author: danny
"""
def hello(event):
    print(i)
import tkinter as tk
window=tk.Tk()
for i in range(9):
    tk.Label(window,text='hi',borderwidth=1,relief="sunken", width=10,height=10).bind('<Button-1>', hello)
window.mainloop()