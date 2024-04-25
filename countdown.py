import tkinter as tk
import time
import random
import pygame

pygame.mixer.init()
num = random.randrange(4)
match num:
    case 0:
        pygame.mixer.music.load("Track01.mp3")
    case 1:
        pygame.mixer.music.load("Track02.mp3")
    case 2:
        pygame.mixer.music.load("Track03.mp3")
    case 3:
        pygame.mixer.music.load("Track04.mp3")
    case default:
        pygame.mixer.music.load("Track05.mp3")

def countdown_start():
    def update_countdown():
        nonlocal countdown_value
        if(countdown_value == 15):
            pygame.mixer.music.play()

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
