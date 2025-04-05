import tkinter as tk
from tkinter import ttk
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("300x200")
        
        # Create and configure the main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Time input
        ttk.Label(main_frame, text="Enter time in seconds:").grid(row=0, column=0, pady=5)
        self.time_entry = ttk.Entry(main_frame)
        self.time_entry.grid(row=1, column=0, pady=5)
        
        # Timer display
        self.timer_label = ttk.Label(main_frame, text="00:00", font=("Arial", 24))
        self.timer_label.grid(row=2, column=0, pady=10)
        
        # Start button
        self.start_button = ttk.Button(main_frame, text="Start Timer", command=self.start_timer)
        self.start_button.grid(row=3, column=0, pady=5)
        
        self.running = False
        self.remaining_time = 0

    def countdown(self):
        if self.remaining_time > 0 and self.running:
            mins, secs = divmod(self.remaining_time, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.timer_label.config(text=timer)
            self.remaining_time -= 1
            self.root.after(1000, self.countdown)
        elif self.remaining_time == 0:
            self.timer_label.config(text="Time's up!")
            self.running = False
            self.start_button.config(state=tk.NORMAL)

    def start_timer(self):
        if not self.running:
            try:
                self.remaining_time = int(self.time_entry.get())
                if self.remaining_time > 0:
                    self.running = True
                    self.start_button.config(state=tk.DISABLED)
                    self.countdown()
            except ValueError:
                self.timer_label.config(text="Invalid input!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()