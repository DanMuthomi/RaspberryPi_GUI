import tkinter as tk

def scan_rfid():
    rfid = "RFID1234"  # Replace this with the actual RFID code obtained from scanning
    if rfid == "RFID1234":  # Replace "RFID1234" with the correct RFID value
        error_label.config(text="RFID card scan successful", fg="green")
    else:
        error_label.config(text="Error: Invalid RFID card", fg="red")

root = tk.Tk()
#root.attributes('-fullscreen', True)
root.title('RFID Scan Page')
root.tk_setPalette("black")

rfid_frame = tk.Frame(root, bg='black')
rfid_frame.pack()

scan_label = tk.Label(rfid_frame, text='Scan RFID card', font=('Bold', 30), fg='white', bg='black')
scan_label.pack(pady=50)

error_label = tk.Label(rfid_frame, text='', font=('Bold', 20), fg='red', bg='black')
error_label.pack(pady=20)

scan_btn = tk.Button(rfid_frame, text='Scan', font=('Bold', 20), bd=0, command=scan_rfid)
scan_btn.pack(pady=50)

rfid_frame.pack_propagate(False)
rfid_frame.configure(width=800, height=480)

root.mainloop()
