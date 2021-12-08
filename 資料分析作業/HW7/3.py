# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:12:55 2021

@author: danny
"""

import tkinter as tk

window= tk.Tk()
window.title("tk")
window.geometry("200x200")

C = tk.IntVar()#攝氏
F = tk.IntVar()#華氏

def tranfer():
    F.set(C.get()*9/5+32)#轉換公式

lab1 = tk.Label(window ,text="攝氏:").place(x=50,y=25)    #標籤設定
lab2 = tk.Label(window ,text="華氏:").place(x=50,y=75)#標籤設定
lab3 = tk.Label(window ,textvariable=F).place(x=120,y=75)#標籤設定

btn = tk.Button(window ,text="轉換" ,command=tranfer).place(x=50,y=125)#一顆按鈕

e1 = tk.Entry(window ,textvariable=C)              #文字方塊設定
e1.place(x=50,y=50)             #文字方塊定位

window.mainloop()