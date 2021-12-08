# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:31:34 2021

@author: danny
"""

from tkinter import *
from random import*
import time

def resetAll():
        global tk
        tk.destroy()
        tk = Tk()
        game()
        
def game():
    canvas = Canvas(tk ,width=400 ,height=250)      #建立畫布
    canvas.pack()
    id1 = canvas.create_oval(10,50,60,100 ,fill='yellow' ,outline='black')           #建立黃球
    id2 = canvas.create_oval(10,150,60,200 ,fill='LightSteelBlue' ,outline='black')  #建立藍球
    canvas.create_text(17 ,40 ,text="ball 1")
    canvas.create_text(17 ,140 ,text="ball 2")
    
    n1 = IntVar()

    canvas.create_text(82 ,240 ,text="輸入哪一個球獲勝:")           #使用者輸入猜測結果處
    e1 = Entry(tk ,width=5 ,textvariable=n1).place(x=140 ,y=230)
    btn = Button(tk ,text="重置" ,command=resetAll).place(x=180 ,y=228)
    
    for x in range(0 ,100):                                         #球的移動
            if randint(1,100) > 60:
                canvas.move(id1,5,0)
            else:
                canvas.move(id2,5,0)
            tk.update()
            time.sleep(0.05)
        
    ballPos1 = canvas.coords(id1)                                  #獲得球最終的座標
    ballPos2 = canvas.coords(id2)
    
    if ballPos1[2] > ballPos2[2]:                                  #由球座標判斷誰先到終點
         if n1.get() == 1:
            label = Label(tk ,width=15 ,text="你贏了").place(x=250 ,y=230)
         else:
            label = Label(tk ,width=15 ,text="抱歉你輸了,球1獲勝").place(x=250 ,y=230)

    else:
         if n1.get() == 2:
             label = Label(tk ,width=15 ,text="你贏了").place(x=250 ,y=230)
         else:
             label = Label(tk ,width=15 ,text="抱歉你輸了,球2獲勝").place(x=250 ,y=230)
        

global tk
tk = Tk()
game()




