from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Test 2")
root.geometry("320x240")

entry = ttk.Entry(root, show = "*")
entry.place(x=80, y=40)
entry.insert(0, "enter anything")

label = ttk.Label(root)
label.place(x=80, y=120)

def get_values():
    v = entry.get()
    label.config(text=v)

btn =ttk.Button(root, text="Process widget", command=get_values)
btn.place(x=80, y=80)

btn2 = ttk.Button(root, text="Quit", command=root.destroy)
btn2.place(x=80, y=160)
root.mainloop()
