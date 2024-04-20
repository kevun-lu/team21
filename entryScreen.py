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
UDP_ID_WIDTH = 5
UDP_ID_HEIGHT = 1
BUTTON_WIDTH = 10
BUTTON_HEIGHT = 4




class Entry_Screen():
    def __init__(self, supabase, udp):
        self.red_team_players = []
        self.green_team_players = []
        self.supabase = supabase
        self.udp = udp
        self.current_red_index = 0
        self.current_green_index = 0

        self.make_boxes()

    def make_boxes(self):
        # Creates tk object for window
        self.window = Tk()
        self.window.title("Player Entry Screen")
        # Set window size
        self.window.geometry("1200x800")
        # Set window color
        self.window.configure(background=BLACK)

        # Create red background
        self.red_background = Label(
            self.window,
            background=RED,
            width=45,
            height=45
        )
        self.red_background.place(x=200, y=50)

        # Create green background
        self.green_background = Label(
            self.window,
            background=GREEN,
            width=45,
            height=45
        )
        self.green_background.place(x=610, y=50)

        # Create red team header
        self.red_team_label = Label(
            self.window,
            text="RED TEAM",
            background=WHITE,
            foreground=RED,
            font=FONT_SIZE,
            width=20,
            height=1
        )
        self.red_team_label.place(x=315, y=60)

        # Create green team header
        self.green_team_label = Label(
            self.window,
            text="GREEN TEAM",
            background=WHITE,
            foreground=GREEN,
            font=FONT_SIZE,
            width=20,
            height=1
        )
        self.green_team_label.place(x=715, y=60)

        # Create red ID inputs
        self.red_id_box_list = []
        self.red_codename_box_list = []
        self.red_equipment_id_list = []
        for i in range(1, 16):
            red_id_input = Text(
                self.window,
                font=FONT_SIZE,
                width=ID_LABEL_WIDTH,
                height=ID_LABEL_HEIGHT
            )
            red_id_input.place(x=210, y=100 + 40 * (i - 1))
            self.red_id_box_list.append(red_id_input)

            red_codename_input = Text(
                self.window,
                font=FONT_SIZE,
                width=ID_LABEL_WIDTH,
                height=ID_LABEL_HEIGHT
            )
            red_codename_input.place(x=380, y=100 + 40 * (i - 1))
            self.red_codename_box_list.append(red_codename_input)

            red_equipment_id_input = Text(
                self.window,
                font=FONT_SIZE,
                width=UDP_ID_WIDTH,
                height=UDP_ID_HEIGHT
            )
            red_equipment_id_input.place(x = 550, y=100 + 40 * (i - 1))
            self.red_equipment_id_list.append(red_equipment_id_input)

            self.red_team_players.append({"id": None, "codename": None, "equipment_id": None})

        # Create green ID inputs
        self.green_id_box_list = []
        self.green_codename_box_list = []
        self.green_equipment_id_list = []
        for i in range(1, 16):
            green_id_input = Text(
                self.window,
                font=FONT_SIZE,
                width=ID_LABEL_WIDTH,
                height=ID_LABEL_HEIGHT
            )
            green_id_input.place(x=620, y=100 + 40 * (i - 1))
            self.green_id_box_list.append(green_id_input)

            green_codename_input = Text(
                self.window,
                font=FONT_SIZE,
                width=ID_LABEL_WIDTH,
                height=ID_LABEL_HEIGHT
            )
            green_codename_input.place(x=790, y=100 + 40 * (i - 1))
            self.green_codename_box_list.append(green_codename_input)

            green_equipment_id_input = Text(
                self.window,
                font=FONT_SIZE,
                width=UDP_ID_WIDTH,
                height=UDP_ID_HEIGHT
            )
            green_equipment_id_input.place(x=960, y=100 + 40 * (i - 1))
            self.green_equipment_id_list.append(green_equipment_id_input)

            self.green_team_players.append({"id": None, "codename": None, "equipment_id": None})

        # Create start button
        self.start_button = Button(
            self.window,
            text="Start\n",
            background=WHITE,
            foreground=GREEN,
            font=FONT_SIZE,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            command=self.start
        )
        self.start_button.place(x=0, y=690)


        # Create clear all entries button
        self.clear_button = Button(
            self.window,
            text="Clear\nall entries",
            background=WHITE,
            foreground=GREEN,
            font=FONT_SIZE,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            command=self.clear_all_entries
        )
        self.clear_button.place(x=1080, y=690)  


        #Search ID on database for red team
        search_button = Button(self.window, text="Search", command=self.search_id_red)
        search_button.place(x=275, y=700)
        #Update codename for red team
        update_button = Button(self.window, text="Update", command=self.update_codename_red)
        update_button.place(x=440, y =700)
        #Read equipment id for red team
        read_button = Button(self.window, text="OK", command=self.read_equipment_id_red)
        read_button.place(x=550, y =700)
        #Search ID on database for green team
        search_button = Button(self.window, text="Search", command=self.search_id_green)
        search_button.place(x=685, y=700)
        #Update codename for green team
        update_button = Button(self.window, text="Update", command=self.update_codename_green)
        update_button.place(x=850, y =700)
        #Read equipment id for green team
        read_button = Button(self.window, text="OK", command=self.read_equipment_id_green)
        read_button.place(x=960, y =700)


        # Shows window
        self.window.mainloop()


        # Create clear all entries button functionality
    def clear_all_entries(self):
        for i in range(len(self.red_id_box_list)):
            self.red_id_box_list[i].delete("1.0", END)
        for i in range(len(self.green_id_box_list)):
            self.green_id_box_list[i].delete("1.0", END)
        for i in range(len(self.red_codename_box_list)):
            self.red_codename_box_list[i].delete("1.0", END)
        for i in range(len(self.green_codename_box_list)):
            self.green_codename_box_list[i].delete("1.0", END)
        for i in range(len(self.red_equipment_id_list)):
            self.red_equipment_id_list[i].delete("1.0", END)
        for i in range(len(self.green_equipment_id_list)):
            self.green_equipment_id_list[i].delete("1.0", END)
        for i in range(len(self.red_team_players)):
            self.red_team_players[i] = {"id": None, "codename": None, "equipment_id": None}
            self.green_team_players[i] = {"id": None, "codename": None, "equipment_id": None}
        self.current_red_index = 0
        self.current_green_index = 0

        
    # Create start button functionality
    def start(self):
        self.window.destroy()

    def search_id_red(self):
        print("Search")
        color = 1 #red=1 green=2
        for i in range(len(self.red_id_box_list)):
            id = self.red_id_box_list[i].get("1.0", "end").strip()
            if id != '':
                id = int(id)
                self.red_team_players[i] = {"id": id, "codename": None, "equipment_id": None}
                data, count = self.supabase.table('players').select('*').eq('id', id).execute()

        
                if(data[1] != []):
                    print(data[1][0]["codename"])
                    self.red_team_players[i]["codename"] = data[1][0]["codename"]
                else:
                    print("you need to add a codename")
                    self.red_team_players[i]["codename"] = "need new codename"

        self.display_codename(color)
    
    #Green team  
    def search_id_green(self):
        print("Search_green")
        color = 2 #red=1 green=2
        for i in range(len(self.green_id_box_list)):
            id = self.green_id_box_list[i].get("1.0", "end").strip()
            if id != '':
                id = int(id)
                self.green_team_players[i] = {"id": id, "codename": None, "equipment_id": None}
                data, count = self.supabase.table('players').select('*').eq('id', id).execute()
                if(data[1] != []):
                    print(data[1][0]["codename"])
                    self.green_team_players[i]["codename"] = data[1][0]["codename"]
                else:
                    print("you need to add a codename")
                    self.green_team_players[i]["codename"] = "need new codename"

        self.display_codename(color)

    def display_codename(self, color):
        if color == 1:
            #red
            for i in range(len(self.red_team_players)):
                if self.red_team_players[i]["id"]:
                    self.red_codename_box_list[i].delete("1.0", END)
                    self.red_codename_box_list[i].insert("1.0",self.red_team_players[i]["codename"])
        else:
            #green
            for i in range(len(self.green_team_players)):
                if self.green_team_players[i]["id"]:
                    self.green_codename_box_list[i].delete("1.0", END)
                    self.green_codename_box_list[i].insert("1.0",self.green_team_players[i]["codename"])
            

    def update_codename_red(self):
        print("Update")
        for i in range(len(self.red_codename_box_list)):
            if self.red_team_players[i]["codename"] == "need new codename":
                codename = self.red_codename_box_list[i].get("1.0", "end").strip()
                self.red_team_players[i]["codename"] = codename

                self.supabase.table('players').insert({"id": self.red_team_players[i]["id"], "codename": codename}).execute()

        
    
    def update_codename_green(self):
        print("Update")
        for i in range(len(self.green_codename_box_list)):
            if self.green_team_players[i]["codename"] == "need new codename":
                codename = self.green_codename_box_list[i].get("1.0", "end").strip()
                self.green_team_players[i]["codename"] = codename

                self.supabase.table('players').insert({"id": self.green_team_players[i]["id"], "codename": codename}).execute()
        
        

    def read_equipment_id_red(self):
        for i in range(len(self.red_codename_box_list)):
            if self.red_team_players[i]["id"]:
                equipment_id = self.red_equipment_id_list[i].get("1.0", "end").strip()
                self.red_team_players[i]["equipment_id"] = equipment_id
                self.udp.sendEquipmentId(equipment_id)

    

    def read_equipment_id_green(self):
        for i in range(len(self.green_codename_box_list)):
            if self.green_team_players[i]["id"]:
                equipment_id = self.green_equipment_id_list[i].get("1.0", "end").strip()
                self.green_team_players[i]["equipment_id"] = equipment_id
                self.udp.sendEquipmentId(equipment_id)
