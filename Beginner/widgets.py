import re
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Zip Code Validator")
root.resizable(0, 0)
root.geometry("300x100")

errmsg = StringVar()
formatting = "Zip should ##### or #####-####"


def check_zip(newval, op):
    errmsg.set("")
    valid = re.match('^[0-9]{5}(\-[0-9]{4})?$', newval) is not None
    btn.state(['!disabled']) if valid else ['disabled']


check_zip_wrapper = (root.register(check_zip), '%P', '%V')

zip = StringVar()
f = ttk.Frame(root)
f.grid(column=0, row=0)
ttk.Label(f, text='Name:').grid(column=0, row=0, padx=5, pady=5)
ttk.Entry(f).grid(column=1, row=0, padx=5, pady=5)
ttk.Label(f, text='Zip:').grid(column=0, row=1, padx=5, pady=5)
e = ttk.Entry(f, textvariable=zip, validate='all',
              validatecommand=check_zip_wrapper)
e.grid(column=1, row=1, padx=5, pady=5)
btn = ttk.Button(f, text="Process")
btn.grid(column=2, row=1, padx=5, pady=5)
btn.state(['disabled'])
msg = ttk.Label(f, font='TkSmallCaptionFont',
                foreground='red', textvariable=errmsg)
msg.grid(column=1, row=2, padx=5, pady=5, sticky='w')


root.mainloop()
