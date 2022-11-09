# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:18:31 2022

@author: tossu
"""

import tkinter as tk

root = tk.Tk()

root.geometry("480x320")
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill = tk.BOTH, expand = True)

id = canvas.create_rectangle(100, 100, 300, 200, fill="black")

root.mainloop()
