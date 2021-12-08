# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 11:02:22 2021

@author: danny
"""

import tkinter as tk
window=tk.Tk()
tk.Label(window, text="台塑企業").pack()#以pack打包
tk.Label(window, text="台積電").pack()
tk.Label(window, text="聯發科").pack()
tk.Label(window, text="華碩電腦").pack()
tk.Label(window, text="宏碁電腦").pack()
window.mainloop()