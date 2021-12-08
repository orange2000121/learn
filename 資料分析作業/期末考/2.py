# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:10:00 2021

@author: danny
"""

import tkinter as tk

window = tk.Tk()
canvas=tk.Canvas(window,width=1000,height=1000)#設置繪畫版
canvas.pack()#放上去
for i in range(1,11):
    a=i*10#以十為間隔
    b=i*10+100
    canvas.create_oval(a,100,b,200)#畫圈
window.mainloop()