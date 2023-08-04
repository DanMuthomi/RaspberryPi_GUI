import tkinter as tk
import home

def root_frame(parent_frame, prev_callback):
    frame = tk.Frame(parent_frame, bg='Royal blue')

    label_prompt = tk.Label(frame, text="", font=('Bold', 20), bg='royal blue', fg='white')
    label_prompt.pack(pady=20)

    def logout():
        label_prompt.config(text="Logout button clicked")
        frame.destroy()  # Destroy the current frame

        # Call the previous callback function to transition back to the home page
        prev_callback()

    blank_btn = tk.Button(frame, text='Blank Button', font=('Bold', 20), bd=0, command=lambda: None)
    blank_btn.pack(pady=20)

    logout_btn = tk.Button(frame, text='Logout', font=('Bold', 20), bd=0, command=logout)
    logout_btn.pack(pady=20)

    return frame
