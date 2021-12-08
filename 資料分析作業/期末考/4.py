# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:43:14 2021

@author: danny
"""

import tkinter as tk

def show():
    selection=''
    for i in checkbox:#確認是不是有勾選
        if checkbox[i].get()==True:
            selection+=breakfast[i]+'\t'
    tk.messagebox.showinfo(title='你最喜歡的早餐',message=selection)
            

window = tk.Tk()
window.title('早餐')#設定標題
window.geometry('400x300')#window大小
breakfast={0:'三名自',1:'潛水艇',2:'燒餅',3:'飯糰',4:'羅波高'}#早餐列表
var = tk.IntVar()
var.set(0)#初始值
tk.Label(window,text='選取你喜歡的早餐')#標題
checkbox={}#記住勾選的
for i in range(len(breakfast)):#勾選框
    checkbox[i]=tk.BooleanVar()
    tk.Checkbutton(window,text=breakfast[i],variable=checkbox[i]).pack()
tk.Button(window,text='確定',command=show).pack()#按鈕
window.mainloop()