import tkinter as tk

def logout():
    # Replace this function with the logout logic of your application
    #print("Logout button clicked")
    label_prompt.config(text="Logout button clicked")
    root.destroy()
    import home

root = tk.Tk()
#root.attributes('-fullscreen', True)
root.title('Logged in')
root.tk_setPalette("black")

additional_frame = tk.Frame(root, bg='black')
additional_frame.pack()

# Prompt label at the top
label_prompt = tk.Label(additional_frame, text="", font=('Bold', 20), bg='black', fg='white')
label_prompt.pack(pady=20)

# First button (Blank button)
blank_btn = tk.Button(additional_frame, text='Blank Button', font=('Bold', 20), bd=0, command=lambda: None)
blank_btn.pack(pady=20)

# Second button (Logout button)
logout_btn = tk.Button(additional_frame, text='Logout', font=('Bold', 20), bd=0, command=logout)
logout_btn.pack(pady=20)

additional_frame.pack_propagate(False)
additional_frame.configure(width=800, height=480)

root.mainloop()
