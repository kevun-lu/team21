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
    height = 45
)
red_background.place(x = 245, y = 50)

# Create green background
green_background = Label(
    window,
    background = GREEN,
    width = 50,
    height = 45
)
green_background.place(x = 600, y = 50)

# Create red team header                        HEADERS
red_team_label = Label(
    window, 
    text = "RED TEAM", 
    background = WHITE, 
    foreground = RED, 
    font = FONT_SIZE,
    width = 20,
    height = 1
)
red_team_label.place(x = 315, y = 60)
# Create green team header
green_team_label = Label(
    window, 
    text = "GREEN TEAM", 
    background = WHITE, 
    foreground = GREEN, 
    font = FONT_SIZE,
    width = 20,
    height = 1
)
green_team_label.place(x = 660, y = 60)

# Create red ID input 1                         RED TEAM INPUTS
red_id_input1 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_id_input1.place(x = 250, y = 100)
# Create red codename input 1
red_codename_input1 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_codename_input1.place(x = 425, y = 100)
# Create red ID input 2
red_id_input2 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_id_input2.place(x = 250, y = 140)
# Create red codename input 2
red_codename_input2 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_codename_input2.place(x = 425, y = 140)
# Create red ID input 3
red_id_input3 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_id_input3.place(x = 250, y = 180)
# Create red codename input 3
red_codename_input3 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_codename_input3.place(x = 425, y = 180)
# Create red ID input 4
red_id_input4 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_id_input4.place(x = 250, y = 220)
# Create red codename input 4
red_codename_input4 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_codename_input4.place(x = 425, y = 220)
# Create red ID input 5
red_id_input5 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_id_input5.place(x = 250, y = 260)
# Create red codename input 5
red_codename_input5 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_codename_input5.place(x = 425, y = 260)
# Create red ID input 6
red_id_input6 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_id_input6.place(x = 250, y = 300)
# Create red codename input 6
red_codename_input6 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_codename_input6.place(x = 425, y = 300)
# Create red ID input 7
red_id_input7 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_id_input7.place(x = 250, y = 340)
# Create red codename input 7
red_codename_input7 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_codename_input7.place(x = 425, y = 340)
# Create red ID input 8
red_id_input8 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_id_input8.place(x = 250, y = 380)
# Create red codename input 8
red_codename_input8 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_codename_input8.place(x = 425, y = 380)
# Create red ID input 9
red_id_input9 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_id_input9.place(x = 250, y = 420)
# Create red codename input 9
red_codename_input9 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_codename_input9.place(x = 425, y = 420)
# Create red ID input 10
red_id_input10 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_id_input10.place(x = 250, y = 460)
# Create red codename input 10
red_codename_input10 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_codename_input10.place(x = 425, y = 460)
# Create red ID input 11
red_id_input11 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_id_input11.place(x = 250, y = 500)
# Create red codename input 11
red_codename_input11 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_codename_input11.place(x = 425, y = 500)
# Create red ID input 12
red_id_input12 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_id_input12.place(x = 250, y = 540)
# Create red codename input 12
red_codename_input12 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_codename_input12.place(x = 425, y = 540)
# Create red ID input 13
red_id_input13 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_id_input13.place(x = 250, y = 580)
# Create red codename input 13
red_codename_input13 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_codename_input13.place(x = 425, y = 580)
# Create red ID input 14
red_id_input14 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_id_input14.place(x = 250, y = 620)
# Create red codename input 14
red_codename_input14 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_codename_input14.place(x = 425, y = 620)
# Create red ID input 15
red_id_input15 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_id_input15.place(x = 250, y = 660)
# Create red codename input 15
red_codename_input15 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
red_codename_input15.place(x = 425, y = 660)

# Create green ID input 1                       GREEN TEAM INPUTS      
green_id_input1 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_id_input1.place(x = 605, y = 100)
# Create green codename input 1
green_codename_input1 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_codename_input1.place(x = 780, y = 100)
# Create green ID input 2
green_id_input2 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_id_input2.place(x = 605, y = 140)
# Create green codename input 2
green_codename_input2 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_codename_input2.place(x = 780, y = 140)
# Create green ID input 3    
green_id_input3 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_id_input3.place(x = 605, y = 180)
# Create green codename input 3
green_codename_input3 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_codename_input3.place(x = 780, y = 180)
# Create green ID input 4
green_id_input4 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_id_input4.place(x = 605, y = 220)
# Create green codename input 4
green_codename_input4 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_codename_input4.place(x = 780, y = 220)
# Create green ID input 5   
green_id_input5 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_id_input5.place(x = 605, y = 260)
# Create green codename input 5
green_codename_input5 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_codename_input5.place(x = 780, y = 260)
# Create green ID input 6
green_id_input6 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_id_input6.place(x = 605, y = 300)
# Create green codename input 6
green_codename_input6 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_codename_input6.place(x = 780, y = 300)
# Create green ID input 7    
green_id_input7 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_id_input7.place(x = 605, y = 340)
# Create green codename input 7
green_codename_input7 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_codename_input7.place(x = 780, y = 340)
# Create green ID input 8
green_id_input8 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_id_input8.place(x = 605, y = 380)
# Create green codename input 8
green_codename_input8 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_codename_input8.place(x = 780, y = 380)
# Create green ID input 9   
green_id_input9 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_id_input9.place(x = 605, y = 420)
# Create green codename input 9
green_codename_input9 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_codename_input9.place(x = 780, y = 420)
# Create green ID input 10
green_id_input10 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_id_input10.place(x = 605, y = 460)
# Create green codename input 10
green_codename_input10 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_codename_input10.place(x = 780, y = 460)
# Create green ID input 11    
green_id_input11 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_id_input11.place(x = 605, y = 500)
# Create green codename input 11
green_codename_input11 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_codename_input11.place(x = 780, y = 500)
# Create green ID input 12
green_id_input12 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_id_input12.place(x = 605, y = 540)
# Create green codename input 12
green_codename_input12 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_codename_input12.place(x = 780, y = 540)
# Create green ID input 13   
green_id_input13 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_id_input13.place(x = 605, y = 580)
# Create green codename input 13
green_codename_input13 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_codename_input13.place(x = 780, y = 580)
# Create green ID input 14
green_id_input14 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_id_input14.place(x = 605, y = 620)
# Create green codename input 14
green_codename_input14 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_codename_input14.place(x = 780, y = 620)
# Create green ID input 15    
green_id_input15 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_id_input15.place(x = 605, y = 660)
# Create green codename input 15
green_codename_input15 = Text(
    window,
    font = FONT_SIZE,
    width = ID_LABEL_WIDTH,
    height = ID_LABEL_HEIGHT
)
green_codename_input15.place(x = 780, y = 660)

# Create start button functionality             BUTTONS
def start():
    print("Function not implemented yet")
# Create start button
start_button = Button(
    window,
    text = "Start\n",
    background = WHITE,
    foreground = GREEN,
    font = FONT_SIZE,
    width = BUTTON_WIDTH,
    height = BUTTON_HEIGHT,
    command = start
)
start_button.place(x = 0, y = 690)
# Create clear all entries button functionality
def clear_all_entries():
    red_id_input1.delete("1.0", "end")
    red_codename_input1.delete("1.0", "end")
    red_id_input2.delete("1.0", "end")
    red_codename_input2.delete("1.0", "end")
    red_id_input3.delete("1.0", "end")
    red_codename_input3.delete("1.0", "end")
    red_id_input4.delete("1.0", "end")
    red_codename_input4.delete("1.0", "end")
    red_id_input5.delete("1.0", "end")
    red_codename_input5.delete("1.0", "end")
    red_id_input6.delete("1.0", "end")
    red_codename_input6.delete("1.0", "end")
    red_id_input7.delete("1.0", "end")
    red_codename_input7.delete("1.0", "end")
    red_id_input8.delete("1.0", "end")
    red_codename_input8.delete("1.0", "end")
    red_id_input9.delete("1.0", "end")
    red_codename_input9.delete("1.0", "end")
    red_id_input10.delete("1.0", "end")
    red_codename_input10.delete("1.0", "end")
    red_id_input11.delete("1.0", "end")
    red_codename_input11.delete("1.0", "end")
    red_id_input12.delete("1.0", "end")
    red_codename_input12.delete("1.0", "end")
    red_id_input13.delete("1.0", "end")
    red_codename_input13.delete("1.0", "end")
    red_id_input14.delete("1.0", "end")
    red_codename_input14.delete("1.0", "end")
    red_id_input15.delete("1.0", "end")
    red_codename_input15.delete("1.0", "end")
    green_id_input1.delete("1.0", "end")
    green_codename_input1.delete("1.0", "end")
    green_id_input2.delete("1.0", "end")
    green_codename_input2.delete("1.0", "end")
    green_id_input3.delete("1.0", "end")
    green_codename_input3.delete("1.0", "end")
    green_id_input4.delete("1.0", "end")
    green_codename_input4.delete("1.0", "end")
    green_id_input5.delete("1.0", "end")
    green_codename_input5.delete("1.0", "end")
    green_id_input6.delete("1.0", "end")
    green_codename_input6.delete("1.0", "end")
    green_id_input7.delete("1.0", "end")
    green_codename_input7.delete("1.0", "end")
    green_id_input8.delete("1.0", "end")
    green_codename_input8.delete("1.0", "end")
    green_id_input9.delete("1.0", "end")
    green_codename_input9.delete("1.0", "end")
    green_id_input10.delete("1.0", "end")
    green_codename_input10.delete("1.0", "end")
    green_id_input11.delete("1.0", "end")
    green_codename_input11.delete("1.0", "end")
    green_id_input12.delete("1.0", "end")
    green_codename_input12.delete("1.0", "end")
    green_id_input13.delete("1.0", "end")
    green_codename_input13.delete("1.0", "end")
    green_id_input14.delete("1.0", "end")
    green_codename_input14.delete("1.0", "end")
    green_id_input15.delete("1.0", "end")
    green_codename_input15.delete("1.0", "end")
# Create clear all entries button
clear_button = Button(
    window,
    text = "Clear\nall entries",
    background = WHITE,
    foreground = GREEN,
    font = FONT_SIZE,
    width = BUTTON_WIDTH,
    height = BUTTON_HEIGHT,
    command = clear_all_entries
)
clear_button.place(x = 1080, y = 690)

# Shows window
window.mainloop()
