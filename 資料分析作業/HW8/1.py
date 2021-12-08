import tkinter as tk

windows = tk.Tk()
canvas = tk.Canvas(windows ,width=400 ,height=250)      #建立畫布
canvas.pack()

for x in range(0,100,5):                        #建立一個間隔為5的迴圈畫出20個長方形
    canvas.create_line(10+x ,10+x ,395-x ,10+x ,395-x ,245-x ,10+x ,245-x ,10+x ,10+x ,fill="SlateBlue")
windows.mainloop