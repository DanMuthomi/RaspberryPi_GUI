from tkinter import *
from tkinter import ttk

root = Tk()

def myClick():
    myLabel = Label(root, text="button clicked!")
    myLabel.pack()
    
ttk.Button(root, text="Click here!", command=myClick)
ttk.pck()

root.mainloop()