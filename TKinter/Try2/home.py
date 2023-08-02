import tkinter as tk

def root_frame(parent, next_callback):
    frame = tk.Frame(parent, bg='black')

    start_btn = tk.Button(frame, text='Click to Start', font=('Bold', 30), bd=0, command=next_callback)
    start_btn.pack(pady=100)

    frame.pack_propagate(False)
    frame.configure(width=800, height=480)

    return frame
