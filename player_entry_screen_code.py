# Player Entry Screen Code
# Author : Kevin Van
# Purpose : Creates player entry screen that
# allows user to input id number and codename

# Imports tkinter module for Python GUI
from tkinter import *

# Default colors and sizes
BLACK = "#000000"
GREEN = "#005500"
RED = "#550000"
WHITE = "#FFFFFF"
FONT_SIZE = "20"
ID_LABEL_WIDTH = 15
ID_LABEL_HEIGHT = 1
BUTTON_WIDTH = 10
BUTTON_HEIGHT = 4

# Creates tk object for window
window = Tk()
window.title("Player Entry Screen")
# Set window size
window.geometry("1200x800")
# Set window color
window.configure(background = BLACK)

# Create red background                         BACKGROUNDS
red_background = Label(
    window,
    background = RED,
    width = 50,
    height = 40
).place(x = 245, y = 50)
# Create green background
green_background = Label(
    window,
    background = GREEN,
    width = 50,
    height = 40
).place(x = 600, y = 50)

# Create red team header                        HEADERS
red_team_label = Label(
    window, 
    text = "RED TEAM", 
    background = WHITE, 
    foreground = RED, 
    font = FONT_SIZE,
    width = 20,
    height = 1
).place(x = 315, y = 60)
# Create green team header
green_team_label = Label(
    window, 
    text = "GREEN TEAM", 
    background = WHITE, 
    foreground = GREEN, 
    font = FONT_SIZE,
    width = 20,
    height = 1
).place(x = 660, y = 60)

# Create red ID input 1                         RED TEAM INPUTS
red_id_input1 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
).place(x = 250, y = 100)
# Create red codename input 1
red_codename_input1 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
).place(x = 425, y = 100)
# Create red ID input 2
red_id_input2 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
).place(x = 250, y = 140)
# Create red codename input 2
red_codename_input2 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
).place(x = 425, y = 140)

# Create green ID input 1                       GREEN TEAM INPUTS      
green_id_input1 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
).place(x = 605, y = 100)
# Create green codename input 1
green_codename_input1 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
).place(x = 780, y = 100)
# Create green ID input 2
green_id_input2 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
).place(x = 605, y = 140)
# Create green codename input 2
green_codename_input2 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
).place(x = 780, y = 140)

# Create start button                           BUTTONS
start_button = Button(
    window,
    text = "Start\n(F5)",
    background = WHITE,
    foreground = GREEN,
    font = FONT_SIZE,
    width = BUTTON_WIDTH,
    height = BUTTON_HEIGHT
).place(x = 0, y = 690)
# Create clear all entries button
clear_button = Button(
    window,
    text = "Clear\nall entries\n(F12)",
    background = WHITE,
    foreground = GREEN,
    font = FONT_SIZE,
    width = BUTTON_WIDTH,
    height = BUTTON_HEIGHT
).place(x = 1080, y = 690)

# Shows window
window.mainloop()
