import tkinter as tk

def start():
    root.destroy()
    import pinverify

root = tk.Tk()
#root.attributes('-fullscreen', True)
root.title('Home Page')
root.tk_setPalette("black")

home_frame = tk.Frame(root, bg='black')
home_frame.pack()

start_btn = tk.Button(home_frame, text='Click to Start', font=('Bold', 30), bd=0, command=start)
start_btn.pack(pady=100)

home_frame.pack_propagate(False)
home_frame.configure(width=800, height=480)

root.mainloop()
