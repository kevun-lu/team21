import tkinter as tk
import threading
import time
from PIL import Image, ImageTk
from playsound import playsound

def countdown_start():
    def update_countdown():
        nonlocal countdown_value
        if(countdown_value == 15):
            threading.Thread(target=playsound, args=("Track01.mp3",), daemon=True).start()
        if countdown_value > 0:
            # Update label with the current countdown value
            label.config(text=str(countdown_value))
            countdown_value -= 1
        elif countdown_value == 0:
            # Change the text to "Go!" before closing
            time.sleep(1)
            label.config(text="Go!")
            countdown_value -= 1
        else:
            # Close the window after showing "Go!"
            root.destroy()
        root.after(1035, update_countdown)  # Schedule the function to be called after 1s

    root = tk.Tk()
    root.attributes("-fullscreen", True)

    # Initialize countdown value
    countdown_value = 30

    # Use a label to display countdown
    label = tk.Label(root, text="", font=("Helvetica", 90), fg='orange', bg='black')
    label.pack(expand=True, fill=tk.BOTH)

    # Start the countdown
    update_countdown()

    root.mainloop()
