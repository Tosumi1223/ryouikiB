# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:22:41 2022

@author: tossu
"""

import tkinter as tk

root = tk.Tk()

root.geometry("480x320")
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill = tk.BOTH, expand = True)

def car(x, y, width, height, D, color):
    id1 = canvas.create_rectangle(x, y+(height/3), x+width, y+height-D, fill=color, outline=color)
    id2 = canvas.create_rectangle(x+width/4, y, x+(width*3/4), y+height/3, fill=color, outline=color)
    id3 = canvas.create_oval(x+width/6, y+height-D, x+width/6+D, y+height, fill="black")
    id4 = canvas.create_oval(x+width*5/6, y+height-D, x+(width*5/6)-D, y+height, fill="black")
    
car(100, 75, 150, 105, 30, "red")
car(300, 200, 75, 50, 15, "blue")

root.mainloop()