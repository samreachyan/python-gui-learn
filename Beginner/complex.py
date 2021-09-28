from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Complex")
root.geometry("300x300")

p = ttk.Panedwindow(root, orient=HORIZONTAL)
# two panes, each of which would get widgets gridded into it:
f1 = ttk.Labelframe(p, text='Pane1', width=100, height=100)
f2 = ttk.Labelframe(p, text='Pane2', width=100, height=100)
lab = ttk.Label(f1, text='Username')
lab.grid(row=0, column=0, padx=5, pady=5)
ent = ttk.Entry(f1, width=15)
ent.grid(row=0, column=1, padx=10, pady=5)
lab2 = ttk.Label(f1, text='Password')
lab2.grid(row=1, column=0)
ent2 = ttk.Entry(f1, width=15)
ent2.grid(row=1, column=1)
p.add(f1)
p.add(f2)
p.pack()


n = ttk.Notebook(root)
f1 = ttk.Frame(n)   # first page, which would get widgets gridded into it
f2 = ttk.Frame(n)   # second page
n.add(f1, text='One')
labb = ttk.Label(f1, text='Username')
labb.grid(row=0, column=0, padx=5, pady=5)
entb = ttk.Entry(f1, width=15)
entb.grid(row=0, column=1, padx=10, pady=5)
lab2 = ttk.Label(f1, text='Password')
lab2.grid(row=1, column=0)
ent2 = ttk.Entry(f1, width=15)
ent2.grid(row=1, column=1)
n.add(f2, text='Two')
mess = ttk.Label(f2, text='Message')
entbmsg = ttk.Entry(f2, width=15)
entbmsg.grid(row=0, column=0, padx=10, pady=5)
mess.grid(row=1, column=0)
n.pack()

root.mainloop()
