import tkinter as tk
from PIL import Image, ImageTk

class SplashScreen:
    def __init__(self, root, next_callback, duration=2000):
        self.root = root
        self.next_callback = next_callback
        self.duration = duration

        self.splash = tk.Toplevel(root)
        self.splash.attributes('-fullscreen', True)
        self.splash.configure(bg='black')

        self.logo_image = self.resize_image("GELogo.png")
        self.logo_label = tk.Label(self.splash, image=self.logo_image, bg='black')
        self.logo_label.image = self.logo_image
        self.logo_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.splash.after(self.duration, self.close_splash)

    def resize_image(self, image_path):
        original_image = Image.open(image_path)
        original_width, original_height = original_image.size
        screen_width = self.splash.winfo_screenwidth()
        screen_height = self.splash.winfo_screenheight()

        # Calculate the new dimensions while maintaining the aspect ratio
        aspect_ratio = original_width / original_height
        if screen_width / screen_height > aspect_ratio:
            new_width = screen_height * aspect_ratio
            new_height = screen_height
        else:
            new_width = screen_width
            new_height = screen_width / aspect_ratio

        resized_image = original_image.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)

    def close_splash(self):
        self.splash.destroy()
        self.next_callback()
