# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:06:02 2021

@author: danny
"""
import tkinter as tk

window= tk.Tk()
window.title("tk")
window.geometry("200x200")

weight =  tk.IntVar()#體重
heigh =  tk.IntVar()#身高
bmi =  tk.IntVar()#bmi

def BMI():
    bmi.set(heigh.get()/(weight.get()*weight.get()/10000))#bmi計算公式

lab1 = tk.Label(window ,text="請輸入身高(公分):").place(x=50,y=25)    #標籤設定
lab2 =  tk.Label(window ,text="請輸入體重(公斤):").place(x=50,y=75)

btn =  tk.Button(window ,text="計算BMI" ,command=BMI).place(x=50,y=125)#創建一顆按鈕

e1 =  tk.Entry(window ,textvariable=weight)              #文字方塊設定
e2 =  tk.Entry(window ,textvariable=heigh)
e3 = tk.Entry(window ,textvariable=bmi)
e1.place(x=50,y=50)             #文字方塊定位
e2.place(x=50,y=100)
e3.place(x=50,y=150)
window.mainloop()