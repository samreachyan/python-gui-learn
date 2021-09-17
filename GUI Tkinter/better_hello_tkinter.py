"""A better Hello world for tkinter"""

import tkinter as tk
from tkinter import ttk


class MyApplication(tk.Tk):
    """Hello world main application"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hello World")
        # self.geometry("600x400")
        # self.resizable(False, False)

        self.hello_frame = HelloView(self)
        self.hello_frame.pack(fill='both', expand=True)
        self.columnconfigure(0, weight=1)


class HelloView(tk.Frame):
    """A freindly little module"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.name = tk.StringVar()
        self.hello_string = tk.StringVar(value="Hello World")

        self.name_label = ttk.Label(self, text="Name:")
        self.name_entry = ttk.Entry(self, textvariable=self.name)

        self.hello_button = ttk.Button(
            self, text="Submit", command=self.message)

        self.hello_label = ttk.Label(
            self, textvariable=self.hello_string, font=("Helvetica", 54), wraplength=500)

        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.hello_button.grid(row=0, column=2)
        self.hello_label.grid(row=1, column=0, columnspan=3)
        self.columnconfigure(0, weight=1)

    def swaphi(self):
        """A method to swap the text"""

        if self.hi.get() == "Hi":
            self.hi.set("Hello")
        else:
            self.hi.set("Hi")

    def message(self):
        """A method to say hello"""

        if self.name.get().strip():
            self.hello_string.set("Hello {}".format(self.name.get()))
        else:
            self.hello_string.set("Hello World")


if __name__ == "__main__":
    MyApplication().mainloop()
