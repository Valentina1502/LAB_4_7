#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()

text = Text(width=25, height=5, bg="darkgreen",
            fg='white', wrap=WORD)

text.pack()
root.mainloop()
