from tkinter import *

root = Tk()

def on_entry_change(*args):
    name = nameEntry.get()
    number = numbervar.get()
    btn.config(text="Hello, "+name+" "+str(number))

Label(root, text="Enter a name: ").grid(row=0, column=0)
nameentryvar = StringVar()
nameentryvar.trace("w", on_entry_change)
nameEntry = Entry(root, textvariable=nameentryvar)
nameEntry.grid(row=1, column=0)

Label(root, text="Choose a Number: ").grid(row=0, column=1)

options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numbervar = IntVar()
numbervar.set(0)
numbervar.trace("w", on_entry_change)

numberEntry = OptionMenu(root, numbervar, *options)
numberEntry.grid(row=1, column=1)

btn = Button(root, text="Hello", width=30)
btn.grid(row=1, column=3)


root.mainloop()