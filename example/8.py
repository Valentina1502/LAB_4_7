#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()
l1 = Label(text="This is a label",
        width=30, height=10,
        bg="lightgreen")
#l1.pack(expand=0, fill=BOTH)
l1.pack(expand=1, anchor=SW)
root.mainloop()

