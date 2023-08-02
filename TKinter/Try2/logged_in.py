import tkinter as tk

def root_frame(parent, prev_callback):
    def logout():
        # Replace this function with the logout logic of your application
        label_prompt.config(text="Logout button clicked")
        parent.destroy()
        prev_callback()  # Transition back to the previous window

    frame = tk.Frame(parent, bg='black')

    label_prompt = tk.Label(frame, text="", font=('Bold', 20), bg='black', fg='white')
    label_prompt.pack(pady=20)

    # First button (Blank button)
    blank_btn = tk.Button(frame, text='Blank Button', font=('Bold', 20), bd=0, command=lambda: None)
    blank_btn.pack(pady=20)

    # Second button (Logout button)
    logout_btn = tk.Button(frame, text='Logout', font=('Bold', 20), bd=0, command=logout)
    logout_btn.pack(pady=20)

    frame.pack_propagate(False)
    frame.configure(width=800, height=480)
    
    return frame
