# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:22:28 2021

@author: danny
"""

import tkinter as tk
import time

window = tk.Tk()
canvas = tk.Canvas(window ,width=400 ,height=250)      #建立畫布
canvas.pack()

canvas.create_text(50 ,125 ,text="東海大學" ,fill="Crimson")       #建立文字

for x in range (0 ,40):                #讓字體移動
    canvas.move(1 ,5 ,0)
    window.update()
    time.sleep(0.05)
