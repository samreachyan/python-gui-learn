from time import clock_getres, strftime
from tkinter import *

# Window Config for clock
window = Tk()
window.title("Digital Clock")
window.geometry("200x80")
window.resizable(0, 0)
window.configure(background='black')

# Label Config for clock
clock_label = Label(window, font=('times', 30, 'bold'),
                    bg='black', fg='white', relief='flat')
clock_label.place(x=20, y=20)


def update_clock():
    # Update the clock label
    clock_label.configure(text=strftime('%H:%M:%S'))
    # Call the update_clock function again in 1000ms
    clock_label.after(80, update_clock)


update_clock()
window.mainloop()
