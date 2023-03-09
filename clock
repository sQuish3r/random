import tkinter as tk
import time

class Clock:
    def __init__(self, master):
        self.master = master
        self.master.title("Clock")
        self.master.geometry("200x100")
        self.time_label = tk.Label(self.master, text="", font=("Helvetica", 48))
        self.time_label.pack(expand=True)

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.master.after(1000, self.update_time)

root = tk.Tk()
clock = Clock(root)
clock.update_time()
root.mainloop()
