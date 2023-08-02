import tkinter as tk

stored_digits=""

root = tk.Tk()
root.geometry('300x400')
root.title('Keypad')
root.tk_setPalette("black")

def insert_num(number):
    key_entry.insert(tk.INSERT, number)
    store_num(number)
    
def delete_num():
    index = int(key_entry.index(tk.INSERT)) - 1
    if index != -1:
        key_entry.delete(index)
    print(index)
    global stored_digits
    stored_digits = stored_digits[:index] + stored_digits[index+1:]
    #index counts digits entered hencecan determine length for pin
    
def store_num(number):
    global stored_digits
    stored_digits += str(number)

def submit():
    print("Stored digits:" ,stored_digits)

key_frame = tk.Frame(root, bg='black')
key_frame.pack()

key_input = tk.Frame(key_frame)

key_entry = tk.Entry(key_input, font=('Bold', 25), bd=0, justify=tk.CENTER) #include: show='*' to hide characters being typed
key_entry.place(x=40, y=20, width=210)

key_input.pack(pady=10)
key_input.pack_propagate(False)
key_input.configure(width=290, height=80)

key_pad=tk.Frame(key_frame)

one_btn = tk.Button(key_pad, text='1', font=('Bold', 20), bd=0, command=lambda: insert_num(1))
one_btn.place(x=0, y=5, width=70)

two_btn = tk.Button(key_pad, text='2', font=('Bold', 20), bd=0, command=lambda: insert_num(2))
two_btn.place(x=70, y=5, width=70)

three_btn = tk.Button(key_pad, text='3', font=('Bold', 20), bd=0, command=lambda: insert_num(3))
three_btn.place(x=140, y=5, width=70)

four_btn = tk.Button(key_pad, text='4', font=('Bold', 20), bd=0, command=lambda: insert_num(4))
four_btn.place(x=0, y=70, width=70)

five_btn = tk.Button(key_pad, text='5', font=('Bold', 20), bd=0, command=lambda: insert_num(5))
five_btn.place(x=70, y=70, width=70)

six_btn = tk.Button(key_pad, text='6', font=('Bold', 20), bd=0, command=lambda: insert_num(6))
six_btn.place(x=140, y=70, width=70)

seven_btn = tk.Button(key_pad, text='7', font=('Bold', 20), bd=0, command=lambda: insert_num(7))
seven_btn.place(x=0, y=140, width=70)

eight_btn = tk.Button(key_pad, text='8', font=('Bold', 20), bd=0, command=lambda: insert_num(8))
eight_btn.place(x=70, y=140, width=70)

nine_btn = tk.Button(key_pad, text='9', font=('Bold', 20), bd=0, command=lambda: insert_num(9))
nine_btn.place(x=140, y=140, width=70)

del_btn = tk.Button(key_pad, text='del', font=('Bold', 20), bd=0, command=delete_num)
del_btn.place(x=0, y=210, width=70)

zero_btn = tk.Button(key_pad, text='0', font=('Bold', 20), bd=0, command=lambda: insert_num(0))
zero_btn.place(x=70, y=210, width=70)

enter_btn = tk.Button(key_pad, text='enter', font=('Bold', 20), bd=0, command=submit)
enter_btn.place(x=140, y=210, width=70)

key_pad.place(x=45, y=100, width=210, height=280)

key_frame.pack_propagate(False)
key_frame.configure(width=300, height=400)

root.mainloop()