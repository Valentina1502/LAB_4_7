#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()

r_var = BooleanVar()
r_var.set(0)
r1 = Radiobutton(text='First',
                 variable=r_var, value=0)
r2 = Radiobutton(text='Second',
                 variable=r_var, value=1)
r1.pack(anchor=E)
r2.pack(anchor=E)
root.mainloop()
