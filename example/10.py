#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
root = Tk()

text = Text(width=25, height=5)
text.pack(side=LEFT)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scroll.set)

root.mainloop()
