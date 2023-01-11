# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:36:43 2022

@author: tossu
"""

import tkinter as tk

def main():
    draw_cannon(300, 500)
    draw_cannon_ball(300,455)
    move_ball()
    root.mainloop()

def draw_cannon(x,y):
    canvas.create_rectangle(x-50,y,x+50,y+35,fill="green",outline="green")
    canvas.create_rectangle(x-15,y-30,x+15,y,fill="green",outline="green")
    
def draw_cannon_ball(x,y):
    canvas.create_oval(x-15, y-15, x+15, y+15, fill="black", tag="cannon_ball")  
    
def move_ball():
    if canvas.bbox("cannon_ball")[1] < 0:
        canvas.delete("cannon_ball")
    canvas.move("cannon_ball", 0, -10)
    root.after(100, move_ball)
    

if __name__=="__main__":
    root = tk.Tk()
    root.geometry("600x600")
    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill = tk.BOTH, expand = True)
    main()

