# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:35:02 2022

@author: tossu
"""

import tkinter as tk

root = tk.Tk()

root.geometry("640x480")
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill = tk.BOTH, expand = True)
    
def car(x, y, width, height, D, color, i, j, tag):
    id1 = canvas.create_rectangle(x+j, y+(height/3)+i, x+width+j, y+height-D+i, fill=color, outline=color, tag="tag{}".format(tag))
    id2 = canvas.create_rectangle(x+(width/4)+j, y+i, x+(width*3/4)+j, y+(height/3)+i, fill=color, outline=color, tag="tag{}".format(tag))
    id3 = canvas.create_oval(x+(width/6)+j, y+height-D+i, x+width/6+D+j, y+height+i, fill="black", tag="tag{}".format(tag))
    id4 = canvas.create_oval(x+(width*5/6)+j, y+height-D+i, x+(width*5/6)-D+j, y+height+i, fill="black", tag="tag{}".format(tag))
    

for i in range(10):
    for j in range(10):
        if i == 0 or i % 2 == 0: 
            if j == 0 or j % 2 == 0:
                car(10,24,26,22,6,"blue",i*40,j*40, i*10+j)
            else:
                car(10,24,26,22,6,"red",i*40,j*40, i*10+j)
        else:
            if j == 0 or j % 2 == 0:
                car(10,24,26,22,6,"red",i*40,j*40, i*10+j)
            else:
                car(10,24,26,22,6,"blue",i*40,j*40, i*10+j)
                
               
root.update()

while(True):
    delete_number = input("delete number? >>")    
    try:
        if delete_number == "quit":
            root.destroy()
            break
        if 0 <= int(delete_number) <= 99:
            print("a")
            canvas.delete("tag{}".format(delete_number))
            root.update()
        elif int(delete_number) < 0 or 99 < int(delete_number):
            print("error")
    except(Exception):
        print("error")

