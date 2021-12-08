# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 11:10:15 2021

@author: danny
"""

import tkinter as tk
friends=['Peter','Kevin','Tracy','John','Tommy','Mike','Notron','Mary','Vicent']#好友列表
window=tk.Tk()
for i,name in enumerate(friends):
    tk.Label(window, text=name).grid(row=int(i/3),column=i%3)
window.mainloop()