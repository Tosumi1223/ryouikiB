# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:32:51 2022

@author: tossu
"""

import tkinter as tk

root = tk.Tk()

root.geometry("480x320")
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill = tk.BOTH, expand = True)

id1 = canvas.create_rectangle(100, 100, 250, 150, fill="black")
id2 = canvas.create_rectangle(150, 75, 200, 100, fill="black")
id3 = canvas.create_oval(120, 150, 150, 180, fill="black")
id4 = canvas.create_oval(200, 150, 230, 180, fill="black")
id5 = canvas.create_text(175, 200, text="Yuki Tosumi")

root.mainloop()