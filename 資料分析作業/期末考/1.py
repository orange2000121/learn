# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:38:15 2021

@author: danny
"""

import tkinter as tk


def changeword():
    lbl_1 = tk.Label(window, text='Hello Word')#叫出lable
    lbl_1.pack()#置中
window =tk.Tk()
window.title('tk')#設定title
window.geometry('400x300')#window大小
but = tk.Button(window, text='顯示訊息',command=changeword)#顯示按鈕
but.pack()#置中
window.mainloop()