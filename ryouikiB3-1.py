# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 12:47:36 2022

@author: tossu
"""

import tkinter as tk

root = tk.Tk()

root.geometry("600x600")
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill = tk.BOTH, expand = True)

def car(x, y, width, height, D, color, tag):
    id1 = canvas.create_rectangle(x, y+(height/3), x+width, y+height-D, fill=color, outline=color, tag=tag)
    id2 = canvas.create_rectangle(x+width/4, y, x+(width*3/4), y+height/3, fill=color, outline=color, tag=tag)
    id3 = canvas.create_oval(x+width/6, y+height-D, x+width/6+D, y+height, fill="black", tag=tag)
    id4 = canvas.create_oval(x+width*5/6, y+height-D, x+(width*5/6)-D, y+height, fill="black", tag=tag)
  
def move_car():
    global d
    if d == 1:
        canvas.move("car1", 10, 0)
        bbox = canvas.bbox("car1")
        pos_x = (bbox[0]+bbox[2])/2
        root.after(100, move_car)
    elif d == -1:
        canvas.move("car1", -10, 0)
        bbox = canvas.bbox("car1")
        pos_x = (bbox[0]+bbox[2])/2
        root.after(100, move_car)
    if bbox[2]>600:
        d = -1
    if bbox[0]<0:
        d = 1

d = 1
car(30, 30, 75, 50, 15, "red", "car1")

root.after(10, move_car)

root.mainloop()