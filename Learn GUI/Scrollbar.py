from tkinter import *
from tkinter import ttk
from typing import filedialog

root = Tk()
l = Listbox(root, height=5)
l.grid(column=0, row=0, sticky=(N, W, E, S))
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=1, row=0, sticky=(N, S))

l['yscrollcommand'] = s.set
ttk.Sizegrip().grid(column=1, row=1, sticky=(S, E))

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

for i in range(1, 101):
    l.insert(END, 'Line %d of 100' % i)

for i in range(1, 101, 2):
    l.itemconfig(i, background="#f0f0ff")


root.mainloop()
