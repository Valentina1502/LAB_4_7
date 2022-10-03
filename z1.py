#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import *


def addition(event):
    try:
        s1 = float(e1.get())
        s2 = float(e2.get())
        l1['text'] = s1+s2
    except ValueError:
        l1['text'] = 'Ошибка'


def substraction(event):
    try:
        s1 = float(e1.get())
        s2 = float(e2.get())
        l1['text'] = s1-s2
    except ValueError:
        l1['text'] = 'Ошибка'


def multiply(event):
    try:
        s1 = float(e1.get())
        s2 = float(e2.get())
        l1['text'] = s1*s2
    except ValueError:
        l1['text'] = 'Ошибка'


def devide(event):
    try:
        s1 = float(e1.get())
        s2 = float(e2.get())
        l1['text'] = s1/s2
    except ValueError:
        l1['text'] = 'Ошибка'
    except ZeroDivisionError:
        l1['text'] = 'Деление на 0!'


if __name__ == '__main__':
    root = Tk()
    e1 = Entry(width=20)
    e2 = Entry(width=20)
    b1 = Button(text='+', width=15)
    b2 = Button(text='-', width=15)
    b3 = Button(text='*', width=15)
    b4 = Button(text='/', width=15)
    l1 = Label(font=(
            "Comic Sans MS",
            16,
            "bold"
        )
    )
    b1.bind('<Button-1>', addition)
    b2.bind('<Button-1>', substraction)
    b3.bind('<Button-1>', multiply)
    b4.bind('<Button-1>', devide)
    l1.config(bd=10)
    e1.pack()
    e2.pack()
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()
    l1.pack()
    root.mainloop()
