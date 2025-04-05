import tkinter as tk
import time
import threading
import platform
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Optional sound
def play_sound():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 500)  # Beep at 1000 Hz for 0.5 sec
    else:
        pygame.mixer.music.load('alarm.mp3')
        pygame.mixer.music.play()

# Countdown logic
def start_timer():
    try:
        t = int(entry.get())
    except ValueError:
        label.config(text="Enter a valid number!")
        return

    def countdown():
        nonlocal t
        while t > 0:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            label.config(text=timeformat)
            window.update()
            time.sleep(1)
            t -= 1

        label.config(text="Time's up!")
        play_sound()

    threading.Thread(target=countdown).start()  # Run countdown in a separate thread

# GUI setup
window = tk.Tk()
window.title("Countdown Timer")
window.geometry("300x150")

label = tk.Label(window, text="Enter time in seconds", font=("Arial", 18))
label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14), justify='center')
entry.pack(pady=5)

start_btn = tk.Button(window, text="Start Timer", command=start_timer, font=("Arial", 14))
start_btn.pack(pady=10)

window.mainloop()
