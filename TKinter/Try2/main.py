import tkinter as tk
import home
import pinverify
import logged_in

class AppManager:
    def __init__(self):
        self.root = tk.Tk()
        #self.root.attributes('-fullscreen', True)
        self.root.title('Main Application')
        self.root.tk_setPalette("black")

        self.current_frame = None

        self.show_home()

    def show_home(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = home.root_frame(self.root, self.show_pinverify)
        self.current_frame.pack()

    def show_pinverify(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = pinverify.root_frame(self.root, self.show_logged_in)
        self.current_frame.pack()

    def show_logged_in(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = logged_in.root_frame(self.root, self.show_home)
        self.current_frame.pack()

if __name__ == "__main__":
    app_manager = AppManager()
    app_manager.root.mainloop()
