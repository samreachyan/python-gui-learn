from tkinter import *
from tkinter import ttk


def setColor(newcolor):
    global color
    color = newcolor


def xy(event):
    global x, y
    x, y = event.x, event.y


def addLine(event):
    global x, y
    canvas.create_line((x, y, event.x, event.y), fill=color)
    x, y = event.x, event.y


root = Tk()
root.title('Pillo')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

canvas = Canvas(root)
id = canvas.create_rectangle(10, 10, 30, 30, fill='red')
canvas.tag_bind(id, "<Button-1>", lambda x: setColor('red'))
canvas.grid(row=0, column=0, sticky='nsew')
canvas.bind('<Button-1>', xy)
canvas.bind('<B1-Motion>', addLine)

root.mainloop()
