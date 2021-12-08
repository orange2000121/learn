# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:34:44 2021

@author: danny
"""

import tkinter as tk
from tkinter import messagebox

windows=tk.Tk()
def mymes():
    messagebox.askokcancel('我的對話方塊','Hello word!') # 標題,內容
windows.title('作業七')#window title
windows.geometry('300x160')#width and heiigh
tk.Button(windows,text='顯示訊息',command=mymes).pack()# 一顆按鈕
windows.mainloop()
