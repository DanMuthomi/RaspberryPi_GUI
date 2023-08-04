#includes a logo image
import tkinter as tk

def root_frame(parent, next_callback):
    frame = tk.Frame(parent, bg='black')

    # Load the logo image
    logo_image = tk.PhotoImage(file="GELogo.png")
    logo_label = tk.Label(frame, image=logo_image, bg='black')
    logo_label.image = logo_image  # Store a reference to the image to prevent garbage collection
    logo_label.pack()

    start_btn = tk.Button(frame, text='Click to Start', font=('Bold', 30), bd=0, command=next_callback)
    start_btn.pack(pady=20)  # Adjust the padding as needed

    frame.pack_propagate(False)
    frame.configure(width=800, height=480)

    return frame