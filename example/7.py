#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()

#f_top = Frame(root)
#f_bot = Frame(root)
f_top = LabelFrame(text="Верх")
f_bot = LabelFrame(text="Низ")

l1 = Label(f_top, width=7, height=4, bg='yellow', text="1")
l2 = Label(f_top, width=7, height=4, bg='orange', text="2")
l3 = Label(f_bot, width=7, height=4, bg='lightgreen', text="3")
l4 = Label(f_bot, width=7, height=4, bg='lightblue', text="4")

f_top.pack()
f_bot.pack(ipadx=10, ipady=10)



l1.pack(side=LEFT, padx=10, pady=10,)
l2.pack(side=LEFT, padx=10, pady=10,)
l3.pack(side=LEFT)
l4.pack(side=LEFT)
root.mainloop()