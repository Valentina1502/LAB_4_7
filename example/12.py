#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

def smile():
    label = Label(text=":)", bg="yellow")
    text1.window_create(INSERT, window=label)

root = Tk()

text = Text(width=50, height=10)
text.pack()
text.insert(1.0, "Hello world!\nline two")
text.tag_add('title', 1.0, '1.end')
text.tag_config('title', justify=CENTER,
                font=("Verdana", 24, 'bold'))

text1 = Text(width=50, height=10)
text1.pack()
button = Button(text=":)", command=smile)
button.pack()

root.mainloop()


