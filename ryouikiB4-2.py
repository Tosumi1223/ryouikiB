# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:43:33 2022

@author: tossu
"""

import tkinter as tk

def main():
    draw_cannon(300, 500)
    root.bind("<KeyPress>",key_press)   
    root.mainloop()
    
def key_press(event):
    global i
    if event.keysym=="space":
        draw_cannon_ball(300, 455)
        move_ball("cannon_ball{}".format(i))
        i = i + 1

def draw_cannon(x,y):
    canvas.create_rectangle(x-50,y,x+50,y+35,fill="green",outline="green")
    canvas.create_rectangle(x-15,y-30,x+15,y,fill= "green",outline="green")
    
def draw_cannon_ball(x,y):
    global cannon_balls
    global i
    canvas.create_oval(x-15, y-15, x+15, y+15, fill="black", tag="cannon_ball_{}".format(i))
    print(canvas.gettags("cannon_ball_{}".format(i)))

    
def move_ball(tag):
    print(type(tag))
    while canvas.bbox(tag)[1] < 0:
        canvas.move(tag, 0, -10)
    canvas.delete(tag)

    

if __name__=="__main__":
    root = tk.Tk()
    root.geometry("600x600")
    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill = tk.BOTH, expand = True)
    cannon_balls = []
    i = 0
    main()
