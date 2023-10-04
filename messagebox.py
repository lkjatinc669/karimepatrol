from tkinter import *
from tkinter import messagebox 

def showError():
    messagebox.showerror("Error", "All your Files are corrupted")

def showInformation():
    messagebox.showinfo("Information", "You are Safe")

def showWarning():
    messagebox.showwarning("Warning", "Are you Sure?")

def askOkCancel():
    if (messagebox.askokcancel("Really?", "Are you Ohk?")== True):
        print("You Clicked OK")
    else:
        print("You clicked Cancel")

root = Tk()
root.geometry("300x50")
root.title("MessageBoxes")

Button(root, text="ErrorBox", command=showError, width=20).grid(row=0, column=0)
Button(root, text="InformationBox", command=showInformation, width=20).grid(row=0, column=1)
Button(root, text="WarningBox", command=showWarning, width=20).grid(row=1, column=0)
Button(root, text="Ask Ok Cancel", command=askOkCancel, width=20).grid(row=1, column=1)


root.mainloop()