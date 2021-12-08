# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:17:27 2021

@author: danny
"""

import tkinter as tk

window= tk.Tk()
window.title("tk")
window.geometry("300x300")

n1 = tk.IntVar()
n2 = tk.IntVar()
n3 = tk.IntVar()
n4 = tk.IntVar()
n5 = tk.IntVar()

n4.set("/")

def add():                       #加
    n3.set(n1.get()+n2.get())
    n4.set("+")
def less():                      #減
    n3.set(n1.get()-n2.get())
    n4.set("-")
def multiply():                  #乘
    n3.set(n1.get()*n2.get())
    n4.set("*")
def division():                  #除
    n3.set(n1.get()/n2.get())
    n4.set("/")
def equal():                     #等於
    n5.set(n3.get())

lab1 = tk.Label(window ,text="/" ,width=5 ,textvariable=n4).place(x=110,y=50)    #標籤設定

btn1 = tk.Button(window ,text="+" ,width=2 ,command=add).place(x=118,y=75)       #按鍵設定
btn2 = tk.Button(window ,text="-" ,width=2 ,command=less).place(x=118,y=100)
btn3 = tk.Button(window ,text="*" ,width=2 ,command=multiply).place(x=118,y=125)
btn4 = tk.Button(window ,text="/" ,width=2 ,command=division).place(x=118,y=150)
btn5 = tk.Button(window ,text="=" ,width=2 ,command=equal).place(x=118,y=175)

e1 = tk.Entry(window ,textvariable=n1 ,width=8)      #文字方塊設定
e2 = tk.Entry(window ,textvariable=n2 ,width=8)
e3 = tk.Entry(window ,textvariable=n5 ,width=8)
e1.place(x=50,y=50)                               #文字方塊定位
e2.place(x=150,y=50)
e3.place(x=100,y=200)
window.mainloop()
