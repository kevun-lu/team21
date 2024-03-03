from tkinter import *
import tkinter as tk

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



def player_entry_screen(supabase):
    # Creates tk object for window
    window = Tk()
    window.title("Player Entry Screen")
    # Set window size
    window.geometry("1200x800")
    # Set window color
    window.configure(background=BLACK)

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
    red_id_box_list = []
    red_codename_box_list = []
    for i in range(1, 16):
        red_id_input = Text(
            window,
            font=FONT_SIZE,
            width=ID_LABEL_WIDTH,
            height=ID_LABEL_HEIGHT
        )
        red_id_input.place(x=250, y=100 + 40 * (i - 1))
        red_id_box_list.append(red_id_input)

        red_codename_input = Text(
            window,
            font=FONT_SIZE,
            width=ID_LABEL_WIDTH,
            height=ID_LABEL_HEIGHT
        )
        red_codename_input.place(x=425, y=100 + 40 * (i - 1))
        red_codename_box_list.append(red_codename_input)

    # Create green ID inputs
    green_id_box_list = []
    green_codename_box_list = []
    for i in range(1, 16):
        green_id_input = Text(
            window,
            font=FONT_SIZE,
            width=ID_LABEL_WIDTH,
            height=ID_LABEL_HEIGHT
        )
        green_id_input.place(x=605, y=100 + 40 * (i - 1))
        green_id_box_list.append(green_id_input)

        green_codename_input = Text(
            window,
            font=FONT_SIZE,
            width=ID_LABEL_WIDTH,
            height=ID_LABEL_HEIGHT
        )
        green_codename_input.place(x=780, y=100 + 40 * (i - 1))
        green_codename_box_list.append(green_codename_input)


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
                red_id_box_list, red_codename_box_list, green_id_box_list, green_codename_box_list):
            red_data = red_id_input.get("1.0", "end").strip()
            red_codename = red_codename_input.get("1.0", "end").strip()
            green_data = green_id_input.get("1.0", "end").strip()
            green_codename = green_codename_input.get("1.0", "end").strip()
            red_id_input.delete("1.0", "end")
            red_codename_input.delete("1.0", "end")
            green_id_input.delete("1.0", "end")
            green_codename_input.delete("1.0", "end")
            print("Red ID:", red_data)
            print("Red Codename:", red_codename)
            print("Green ID:", green_data)
            print("Green Codename:", green_codename)
    #list of ID not box
    red_id_list = []
    green_id_list = []
    red_codename_list = []
    green_codename_list = []

    def search_id_red():
        print("Search")
        color = 1 #red=1 green=2
        for red_id_input, red_codename_input, green_id_input, green_codename_input in zip(red_id_box_list, red_codename_box_list, green_id_box_list, green_codename_box_list):
            red_data = red_id_input.get("1.0", "end").strip()
            red_id_list.append(red_data)
            # red_codename = red_codename_input.get("1.0", "end").strip()
            # # red_codename_list.append(red_codename)
            # green_data = green_id_input.get("1.0", "end").strip()
            # green_id_list.append(green_data)
            # green_codename = green_codename_input.get("1.0", "end").strip()
            # green_codename_list.append(green_codename)
            #Red
        for red_id in red_id_list:
            if red_id != "":
                data, count = supabase.table('players').select('*').eq('id', int(red_id)).execute()
                if(data[1] != []):
                    print('print data[1][0]["code_name"] to codename box')
                    print(red_id)
                    print(data[1][0]["code_name"])
                    red_codename_list.append(data[1][0]["code_name"])
                else:
                    print("you need to add a codename")
                    red_codename_list.append("need new code_name")
            # #Green
            # for green_id in green_id_list:
            #     if green_id != "":
            #         data, count = supabase.table('players').select('*').eq('id', int(green_id)).execute()
            #         if(data[1] != []):
            #             print('print data[1][0]["code_name"] to codename box')
            #             print(green_id)
            #             print(data[1][0]["code_name"])
            #             green_codename_list.append(data[1][0]["code_name"])
            #         else:
            #             print("you need to add a codename")
            #             green_codename_list.append("need new code_name")     
        display_codename(color)
    #Green team  
    def search_id_green():
        print("Search_green")
        color = 2 #red=1 green=2

        for red_id_input, red_codename_input, green_id_input, green_codename_input in zip(red_id_box_list, red_codename_box_list, green_id_box_list, green_codename_box_list):
            red_data = red_id_input.get("1.0", "end").strip()
            green_data = green_id_input.get("1.0", "end").strip()
            green_id_list.append(green_data)
            #Green
        for green_id in green_id_list:
            if green_id != "":
                data, count = supabase.table('players').select('*').eq('id', int(green_id)).execute()
                if(data[1] != []):
                    print('print data[1][0]["code_name"] to codename box')
                    print(green_id)
                    print(data[1][0]["code_name"])
                    green_codename_list.append(data[1][0]["code_name"])
                else:
                    print("you need to add a codename")
                    green_codename_list.append("need new code_name")    
        display_codename(color)

    def display_codename(color):
        if color == 1:
            #red
            for i in range(len(red_codename_list)):
                red_codename_box_list[i].insert("1.0",red_codename_list[i])
        else:
            #green
            for i in range(len(green_codename_list)):
                green_codename_box_list[i].insert("1.0",green_codename_list[i])
        

    def update_codename_red():
        print("Update")
        color = 1
        red_codename_list.clear()
        for red_id_input, red_codename_input, green_id_input, green_codename_input in zip(red_id_box_list, red_codename_box_list, green_id_box_list, green_codename_box_list):
            red_codename = red_codename_input.get("1.0", "end").strip()
            red_codename_list.append(red_codename)
        for i in range(len(red_id_list)):
            if red_id_list[i] != "":
                data, count = supabase.table('players').select('*').eq('id', int(red_id_list[i])).execute()
                if(data[1] != []):
                    pass
                else:
                    supabase.table('players').insert({"id": red_id_list[i], "code_name": red_codename_list[i]}).execute()
    
    def update_codename_green():
        print("Update")
        color = 1
        green_codename_list.clear()
        for red_id_input, red_codename_input, green_id_input, green_codename_input in zip(red_id_box_list, red_codename_box_list, green_id_box_list, green_codename_box_list):
            green_codename = green_codename_input.get("1.0", "end").strip()
            green_codename_list.append(green_codename)
        for i in range(len(green_id_list)):
            if green_id_list[i] != "":
                data, count = supabase.table('players').select('*').eq('id', int(green_id_list[i])).execute()
                if(data[1] != []):
                    pass
                else:
                    supabase.table('players').insert({"id": green_id_list[i], "code_name": green_codename_list[i]}).execute()



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

    #Search ID on database for red team
    search_button = Button(window, text="Search", command=search_id_red)
    search_button.place(x=300, y=700)
    #Update codename for red team
    update_button = Button(window, text="Update", command=update_codename_red)
    update_button.place(x=450, y =700)
    #Search ID on database for green team
    search_button = Button(window, text="Search", command=search_id_green)
    search_button.place(x=650, y=700)
    #Update codename for green team
    update_button = Button(window, text="Update", command=update_codename_green)
    update_button.place(x=800, y =700)


    # Shows window
    window.mainloop()
