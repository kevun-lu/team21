from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
import time
from threading import Thread

# Default colors and sizes
BLACK = "#000000"
BLUE = "#ADD8E6"
GREEN = "#00AA00"
ORANGE = "#AA5500"
RED = "#AA0000"
WHITE = "#FFFFFF"
YELLOW = "#EEEED0"
FONT_SIZE = "35"
FONT_SIZE2 = "helvetica 16 bold"
ID_LABEL_WIDTH = 15
ID_LABEL_HEIGHT = 1
BUTTON_WIDTH = 10
BUTTON_HEIGHT = 4

class Play_Action_Display():
    def __init__(self):
        self.current_red_index = 0
        self.current_green_index = 0
        self.red_players_label_list = []
        self.green_players_label_list = []
        self.red_scores_list = []
        self.green_scores_list = []
        self.red_b_list = []
        self.green_b_list = []
        self.max_red_index = 0
        self.max_green_index = 0
        self.flash = 0
        self.run = 0

    def start(self, red_players, green_players, udp):
        self.udp = udp
        self.red_team_players = red_players
        self.green_team_players = green_players
        for i in range(len(self.red_team_players)):
            self.red_team_players[i]["hit_enemy_base"] = False
        for i in range(len(self.green_team_players)):
            self.green_team_players[i]["hit_enemy_base"] = False
        self.make_boxes()

    def make_boxes(self):
        # Creates tk object for window
        self.window = Tk()
        self.window.title("Play Action Display")
        # Set window size
        self.window.geometry("1200x800")
        # Set window color
        self.window.configure(background=BLACK)

        # Create top half display background
        self.display_top_background = Label(
            self.window,
            background=WHITE,
            font=FONT_SIZE,
            width=100,
            height=25
        )
        self.display_top_background.place(x=45, y=60)
        # Create bottom half display background
        self.display_bot_background = Label(
            self.window,
            background=BLUE,
            font=FONT_SIZE,
            width=100,
            height=14
        )
        self.display_bot_background.place(x=45, y=340)
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
        self.red_team_label.place(x=50, y=90)
        self.red_team_score_label = Label(
            self.window,
            text="0",
            background=WHITE,
            foreground=RED,
            font=FONT_SIZE,
            width=20,
            height=1
        )
        self.red_team_score_label.place(x=250,y=90)
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
        self.green_team_label.place(x=550, y=90)
        self.green_team_score_label = Label(
            self.window,
            text="0",
            background=WHITE,
            foreground=GREEN,
            font=FONT_SIZE,
            width=20,
            height=1
        )
        self.green_team_score_label.place(x=750,y=90)
        # Create current scores label
        self.scores_label = Label(
            text="CURRENT SCORE",
            foreground=ORANGE,
            background=YELLOW,
            font=FONT_SIZE2,
            width=30,
            height=2
        )
        self.scores_label.place(x=800,y=30)
        self.game_action_text_label = scrolledtext.ScrolledText(
                self.window,
                background=BLUE,
                foreground=ORANGE,
                font=FONT_SIZE,
                width=98,
                height=14
        )
        self.game_action_text_label.place(x=45,y=340)
        # Create current scores label
        self.action_label = Label(
            self.window,
            text="CURRENT GAME ACTION",
            foreground=ORANGE,
            background=YELLOW,
            font=FONT_SIZE2,
            width=30,
            height=2
        )
        self.action_label.place(x=800,y=320)

        # Create countdown timer
        self.timer_label = Label(
            self.window,
            text="TIME LEFT:",
            foreground=ORANGE,
            background=YELLOW,
            font=FONT_SIZE2,
            width=20,
            height=2
        )
        self.timer_label.place(x=800,y=550)
        # Create countdown timer
        self.countdown_label = Label(
            self.window,
            text="360",
            foreground=ORANGE,
            background=YELLOW,
            font=FONT_SIZE2,
            width=15,
            height=2
        )
        self.countdown_label.place(x=1000,y=550)

        for i in range(len(self.red_team_players)):
            if self.red_team_players[i]["codename"] == None:
                break
            self.max_red_index += 1
            self.red_player_label = Label(
                self.window,
                text=self.red_team_players[i]["codename"],
                background=WHITE,
                foreground=RED,
                font=FONT_SIZE,
                width=20,
                height=1
            )
            if(i < 5):
                self.red_player_label.place(x=50,y=120+i*30)
            else:
                self.red_player_label.place(x=-100,y=-100)
            self.red_players_label_list.append(self.red_player_label)
            self.red_player_score_label = Label(
                self.window,
                text="0",
                background=WHITE,
                foreground=RED,
                font=FONT_SIZE,
                width=20,
                height=1
            )
            if(i < 5):
                self.red_player_score_label.place(x=250,y=120+i*30)
            else:
                self.red_player_score_label.place(x=-100,y=-100)
            self.red_scores_list.append(self.red_player_score_label)
            self.red_b_label = Label(
                self.window,
                text="",
                background=WHITE,
                foreground=RED,
                font="symbol 16 italic",
                width=1,
                height=1
            )
            if(i < 5):
                self.red_b_label.place(x=560,y=116+i*30)
            else:
                self.red_b_label.place(x=-100,y=-100)
            self.red_b_list.append(self.red_b_label)

        for i in range(len(self.green_team_players)):
            if self.green_team_players[i]["codename"] == None:
                break
            self.max_green_index += 1
            self.green_player_label = Label(
                self.window,
                text=self.green_team_players[i]["codename"],
                background=WHITE,
                foreground=GREEN,
                font=FONT_SIZE,
                width=20,
                height=1
            )
            if(i < 5):
                self.green_player_label.place(x=550,y=120+i*30)
            else:
                self.green_player_label.place(x=-100,y=-100)
            self.green_players_label_list.append(self.green_player_label)
            self.green_player_score_label = Label(
                self.window,
                text="0",
                background=WHITE,
                foreground=GREEN,
                font=FONT_SIZE,
                width=20,
                height=1
            )
            if(i < 5):
                self.green_player_score_label.place(x=750,y=120+i*30)
            else:
                self.green_player_score_label.place(x=-100,y=-100)
            self.green_scores_list.append(self.green_player_score_label)
            self.green_b_label = Label(
                self.window,
                text="",
                background=WHITE,
                foreground=GREEN,
                font="symbol 16 italic",
                width=1,
                height=1
            )
            if(i < 5):
                self.green_b_label.place(x=560,y=116+i*30)
            else:
                self.green_b_label.place(x=-100,y=-100)
            self.green_b_list.append(self.green_b_label)

        self.countdown(360)

        self.window.mainloop()

    def countdown(self, count):
        self.countdown_label["text"] = count
        if count > 0:
            self.window.after(1000, self.countdown, count - 1)
        else:
            self.game_over_label =  Label(
                self.window,
                text="GAME OVER",
                background=BLACK,
                foreground=ORANGE,
                font=FONT_SIZE,
                width=40,
                height=10
            )
            self.game_over_label.place(x="300",y="200")
            self.run = 1
            time.sleep(3)
            self.udp.sendGameEndCode()

    def receive_player_action(self, player, object):
        if self.run == 0:
            if player == object:
                self.hit_self(player)
            elif object == 53:
                self.hit_red_base(player)
            elif object == 43:
                self.hit_green_base(player)
            else:
                self.hit_player(player, object)

    def update_player_score(self, player, team, points):
        if(team == "red"):
            for i in range(self.max_red_index):
                if(player == int(self.red_team_players[i]["equipment_id"])):
                    change = int(self.red_scores_list[i]["text"])
                    change += points
                    self.red_scores_list[i]["text"] = change
        else:
            for i in range(self.max_green_index):
                if(player == int(self.green_team_players[i]["equipment_id"])):
                    change = int(self.green_scores_list[i]["text"])
                    change += points
                    self.green_scores_list[i]["text"] = change
        self.update_team_score(team, points)
        self.swap_player_positions(team)

    def update_team_score(self, team, points):
        if team == "red":
            change = int(self.red_team_score_label["text"])
            change += points
            self.red_team_score_label["text"] = change
        else:
            change = int(self.green_team_score_label["text"])
            change += points
            self.green_team_score_label["text"] = change

    def hit_red_base(self, player):
        for i in range(self.max_green_index):
            if(player == int(self.green_team_players[i]["equipment_id"])):
                codename = self.green_team_players[i]["codename"]
                for j in range(len(self.green_b_list)):
                    self.green_b_list[j]["text"] = ""
                self.green_b_list[i]["text"] = "B"
                self.update_player_score(player, "green", 100)
                self.update_game_action(codename, "base", "RED")
                break
        
    def hit_green_base(self, player):
        for i in range(self.max_red_index):
            if(player == int(self.red_team_players[i]["equipment_id"])):
                codename = self.red_team_players[i]["codename"]
                for j in range(len(self.red_b_list)):
                    self.red_b_list[j]["text"] = ""
                self.red_b_list[i]["text"] = "B"
                self.update_player_score(player, "red", 100)
                self.update_game_action(codename, "base", "GREEN")
                break
        
    def hit_player(self, player, object):
        codename1 = ""
        codename2 = ""
        player_team = ""
        object_team = ""
        player_found = 0
        for i in range(self.max_red_index):
            if(player == int(self.red_team_players[i]["equipment_id"])):
                player_team = "red"
                codename1 = self.red_team_players[i]["codename"]
                player_found = 1
                break
        if player_found == 0:
            for i in range(self.max_green_index):
                if(player == int(self.green_team_players[i]["equipment_id"])): 
                    player_team = "green"
                    codename1 = self.green_team_players[i]["codename"]
                    player_found = 1
                    break
        player_found = 0
        for i in range(self.max_red_index):
            if(object == int(self.red_team_players[i]["equipment_id"])):
                object_team = "red"
                codename2 = self.red_team_players[i]["codename"]
                player_found = 1
                break
        if player_found == 0:
            for i in range(self.max_green_index):
                if(object == int(self.green_team_players[i]["equipment_id"])):
                    object_team = "green"
                    codename2 = self.green_team_players[i]["codename"]
                    player_found = 1
                    break
        if player_found == 1:
            if player_team != object_team:
                self.update_player_score(player, player_team, 10)
            else:
                self.update_player_score(player, player_team, -10)
            self.update_game_action(codename1, codename2, "")

    def hit_self(self, player):
        pass

    def update_game_action(self, player, object, team):
        update = ""
        if(object == "base"):
            update = str(player) + " has hit " + str(team) + "'s base\n"
        else:
            update = str(player) + " has hit " + str(object) + "\n"
        if int(self.red_team_score_label.cget("text")) > int(self.green_team_score_label.cget("text")):
            self.green_team_label["foreground"] = GREEN
            self.green_team_score_label["foreground"] = GREEN
            if self.flash == 0:
                self.red_team_label["foreground"] = BLUE
                self.red_team_score_label["foreground"] = BLUE
                self.flash = 1
            else:
                self.red_team_label["foreground"] = RED
                self.red_team_score_label["foreground"] = RED
                self.flash = 0
        else:
            self.red_team_label["foreground"] = RED
            self.red_team_score_label["foreground"] = RED
            if self.flash == 0:
                self.green_team_label["foreground"] = BLUE
                self.green_team_score_label["foreground"] = BLUE
                self.flash = 1
            else:
                self.green_team_label["foreground"] = GREEN
                self.green_team_score_label["foreground"] = GREEN
                self.flash = 0
        self.game_action_text_label.insert(INSERT, update)
        self.game_action_text_label.update()
        self.game_action_text_label.yview(END)

    def swap_player_positions(self, team):
        #if player gains points
        if(team == "red"):
            for i in range(self.max_red_index):
                best_score = int(self.red_scores_list[i]["text"])
                for j in range(i+1,self.max_red_index,1):
                    current_score = int(self.red_scores_list[j]["text"])
                    if current_score > best_score:
                        best_score = current_score
                        #change b positions
                        b_change = self.red_b_list[j]
                        b_change_position1 = self.red_b_list[j].place_info()
                        b_change_position2 = self.red_b_list[i].place_info()
                        self.red_b_list[j].place(x=60,y=int(b_change_position2["y"]))
                        self.red_b_list[i].place(x=60,y=int(b_change_position1["y"]))
                        self.red_b_list[j] = self.red_b_list[i]
                        self.red_b_list[i] = b_change
                        #change positions in red team players
                        player_change = self.red_team_players[j]
                        self.red_team_players[j] = self.red_team_players[i]
                        self.red_team_players[i] = player_change
                        #change positions in red players labels list and change lable position
                        label_change = self.red_players_label_list[j]
                        label_change_position1 = self.red_players_label_list[j].place_info()
                        label_change_position2 = self.red_players_label_list[i].place_info()
                        self.red_players_label_list[j].place(x=50,y=int(label_change_position2["y"]))
                        self.red_players_label_list[i].place(x=50,y=int(label_change_position1["y"]))
                        self.red_players_label_list[j] = self.red_players_label_list[i]
                        self.red_players_label_list[i] = label_change
                        #change positions in red scores list and change label positions
                        score_change = self.red_scores_list[j]
                        score_change_position1 = self.red_scores_list[j].place_info()
                        score_change_position2 = self.red_scores_list[i].place_info()
                        self.red_scores_list[j].place(x=250,y=int(score_change_position2["y"]))
                        self.red_scores_list[i].place(x=250,y=int(score_change_position1["y"]))
                        self.red_scores_list[j] = self.red_scores_list[i]
                        self.red_scores_list[i] = score_change    
        elif team == "green":
            for i in range(self.max_green_index):
                best_score = int(self.green_scores_list[i]["text"])
                for j in range(i+1,self.max_green_index,1):
                    current_score = int(self.green_scores_list[j]["text"])
                    if current_score > best_score:
                        best_score = current_score
                        #change b positions
                        b_change = self.green_b_list[j]
                        b_change_position1 = self.green_b_list[j].place_info()
                        b_change_position2 = self.green_b_list[i].place_info()
                        self.green_b_list[j].place(x=560,y=int(b_change_position2["y"]))
                        self.green_b_list[i].place(x=560,y=int(b_change_position1["y"]))
                        self.green_b_list[j] = self.green_b_list[i]
                        self.green_b_list[i] = b_change
                        #change positions in green team players
                        player_change = self.green_team_players[j]
                        self.green_team_players[j] = self.green_team_players[i]
                        self.green_team_players[i] = player_change
                        #change positions in green players labels list and change lable position
                        label_change = self.green_players_label_list[j]
                        label_change_position1 = self.green_players_label_list[j].place_info()
                        label_change_position2 = self.green_players_label_list[i].place_info()
                        self.green_players_label_list[j].place(x=550,y=int(label_change_position2["y"]))
                        self.green_players_label_list[i].place(x=550,y=int(label_change_position1["y"]))
                        self.green_players_label_list[j] = self.green_players_label_list[i]
                        self.green_players_label_list[i] = label_change
                        #change positions in green scores list and change label positions
                        score_change = self.green_scores_list[j]
                        score_change_position1 = self.green_scores_list[j].place_info()
                        score_change_position2 = self.green_scores_list[i].place_info()
                        self.green_scores_list[j].place(x=750,y=int(score_change_position2["y"]))
                        self.green_scores_list[i].place(x=750,y=int(score_change_position1["y"]))
                        self.green_scores_list[j] = self.green_scores_list[i]
                        self.green_scores_list[i] = score_change
