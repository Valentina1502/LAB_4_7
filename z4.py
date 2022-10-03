#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, IntVar, Radiobutton, Label


def name():
    label['text'] = 'Валентина'


def number():
    label['text'] = '8-999-743-23-25'


def adress():
    label['text'] = 'Ставрополь'


if __name__ == '__main__':
    root = Tk()
    root.title('ИВТ-б-о-20-1')
    var = IntVar()
    var.set(-1)
    Radiobutton(indicatoron=0, text="Имя", command=name, variable=var,
                value=0, width=20, height=2).pack()
    Radiobutton(indicatoron=0, text="Номер", command=number, variable=var,
                value=1, width=20, height=2).pack()
    Radiobutton(indicatoron=0, text="Адресс", command=adress, variable=var,
                value=2, width=20, height=2).pack()
    label = Label(width=40, height=25)
    label.pack()
    root.mainloop()
