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



def player_entry_screen():
    # Creates tk object for window
    window = Tk()
    window.title("Player Entry Screen")
    # Set window size
    window.geometry("1200x800")
    # Set window color
    window.configure(background=BLACK)

    # Create Buttons
    button = Button(window, text="Add", command=search_id)
    button.pack()

    # Create red background
    red_background = Label(
        window,
        background=RED,
        width=50,
        height=45
    )
    red_background.place(x=245, y=50)

    # Create green background
    green_background = Label(
        window,
        background=GREEN,
        width=50,
        height=45
    )
    green_background.place(x=600, y=50)

    # Create red team header
    red_team_label = Label(
        window,
        text="RED TEAM",
        background=WHITE,
        foreground=RED,
        font=FONT_SIZE,
        width=20,
        height=1
    )
    red_team_label.place(x=315, y=60)

    # Create green team header
    green_team_label = Label(
        window,
        text="GREEN TEAM",
        background=WHITE,
        foreground=GREEN,
        font=FONT_SIZE,
        width=20,
        height=1
    )
    green_team_label.place(x=660, y=60)

    # Create red ID inputs
    red_id_inputs = []
    red_codename_inputs = []
    for i in range(1, 16):
        red_id_input = Text(
            window,
            font=FONT_SIZE,
            width=ID_LABEL_WIDTH,
            height=ID_LABEL_HEIGHT
        )
        red_id_input.place(x=250, y=100 + 40 * (i - 1))
        red_id_inputs.append(red_id_input)

        red_codename_input = Text(
            window,
            font=FONT_SIZE,
            width=ID_LABEL_WIDTH,
            height=ID_LABEL_HEIGHT
        )
        red_codename_input.place(x=425, y=100 + 40 * (i - 1))
        red_codename_inputs.append(red_codename_input)

    # Create green ID inputs
    green_id_inputs = []
    green_codename_inputs = []
    for i in range(1, 16):
        green_id_input = Text(
            window,
            font=FONT_SIZE,
            width=ID_LABEL_WIDTH,
            height=ID_LABEL_HEIGHT
        )
        green_id_input.place(x=605, y=100 + 40 * (i - 1))
        green_id_inputs.append(green_id_input)

        green_codename_input = Text(
            window,
            font=FONT_SIZE,
            width=ID_LABEL_WIDTH,
            height=ID_LABEL_HEIGHT
        )
        green_codename_input.place(x=780, y=100 + 40 * (i - 1))
        green_codename_inputs.append(green_codename_input)


    # Create start button functionality
    def start():
        print("Function not implemented yet")


    # Create start button
    start_button = Button(
        window,
        text="Start\n",
        background=WHITE,
        foreground=GREEN,
        font=FONT_SIZE,
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        command=start
    )
    start_button.place(x=0, y=690)


    # Create clear all entries button functionality
    def clear_all_entries():
        for red_id_input, red_codename_input, green_id_input, green_codename_input in zip(
                red_id_inputs, red_codename_inputs, green_id_inputs, green_codename_inputs):
            red_data = red_id_input.get("1.0", "end").strip()
            red_codename = red_codename_input.get("1.0", "end").strip()
            green_data = green_id_input.get("1.0", "end").strip()
            green_codename = green_codename_input.get("1.0", "end").strip()
            print("Red ID:", red_data)
            print("Red Codename:", red_codename)
            print("Green ID:", green_data)
            print("Green Codename:", green_codename)


    # Create clear all entries button
    clear_button = Button(
        window,
        text="Clear\nall entries",
        background=WHITE,
        foreground=GREEN,
        font=FONT_SIZE,
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        command=clear_all_entries
    )
    clear_button.place(x=1080, y=690)

    # Shows window
    window.mainloop()

def search_id():
    print("Search")


player_entry_screen()
