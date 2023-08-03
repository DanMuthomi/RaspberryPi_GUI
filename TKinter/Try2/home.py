import tkinter as tk
from PIL import Image, ImageTk  # Import directly from Pillow

def resize_image(image_path, target_width, target_height):
    original_image = Image.open(image_path)
    original_width, original_height = original_image.size

    # Calculate the new dimensions while maintaining the aspect ratio
    aspect_ratio = original_width / original_height
    if target_width / target_height > aspect_ratio:
        new_width = int(target_height * aspect_ratio)
        new_height = target_height
    else:
        new_width = target_width
        new_height = int(target_width / aspect_ratio)

    resized_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)

def root_frame(parent, next_callback):
    frame = tk.Frame(parent, bg='black')

    # Load and resize the logo image
    logo_image = resize_image("GELogo.png", 800, 300)
    logo_label = tk.Label(frame, image=logo_image, bg='black')
    logo_label.image = logo_image  # Store a reference to the image to prevent garbage collection
    logo_label.pack()

    start_btn = tk.Button(frame, text='Click to Start', font=('Bold', 30), bd=0, command=next_callback)
    start_btn.pack(pady=20)  # Adjust the padding as needed

    frame.pack_propagate(False)
    frame.configure(width=800, height=480)

    return frame
