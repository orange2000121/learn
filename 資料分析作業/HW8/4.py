# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:25:46 2021

@author: danny
"""

import tkinter as tk

global x           #設定全域變數
global y
x = 10             #設定初值
y = 10

def lineprint(event):            #判斷按鍵並執行畫線動作
    global x
    global y
    if event.keysym == 'Left':
        canvas.create_line(x ,y ,x-5 ,y ,fill="Crimson")
        x = x-5
        y = y
    if event.keysym == 'Right':
        canvas.create_line(x ,y ,x+5 ,y ,fill="Crimson")
        x = x+5
        y = y
    if event.keysym == 'Up':
        canvas.create_line(x ,y ,x ,y-5 ,fill="Crimson")
        x = x
        y = y-5
    if event.keysym == 'Down':
        canvas.create_line(x ,y ,x ,y+5 ,fill="Crimson")
        x = x
        y = y+5

window = tk.Tk()
canvas = tk.Canvas(window ,width=400 ,height=250)      #建立畫布
canvas.pack()

canvas.bind_all('<KeyPress-Left>' ,lineprint)       #訊息綁定
canvas.bind_all('<KeyPress-Right>',lineprint)
canvas.bind_all('<KeyPress-Up>' ,lineprint)
canvas.bind_all('<KeyPress-Down>' ,lineprint)
