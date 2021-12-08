# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:20:14 2021

@author: danny
"""

import tkinter as tk
window = tk.Tk()
canvas = tk.Canvas(window ,width=400 ,height=250)      #建立畫布
canvas.pack()

for y in range(0,201,10):                        #建立一個間隔為10的迴圈畫出橫線
    for x in range(0,201,10):                    #建立一個間隔為10的迴圈畫出直線  
        canvas.create_line(10 ,10+y ,210 ,10+y ,fill="SlateBlue")
        canvas.create_line(10+x ,10 ,10+x ,210 ,fill="SlateBlue")

