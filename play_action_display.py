from tkinter import *
import tkinter as tk
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
        self.max_red_index = 0
        self.max_green_index = 0

    def start(self, red_players, green_players, udp):
        self.udp = udp
        self.red_team_players = red_players
        self.green_team_players = green_players
        for i in range(len(self.red_team_players)):
            self.red_team_players[i]["hit_enemy_base"] = False
        for i in range(len(self.green_team_players)):
            self.green_team_players[i]["hit_enemy_base"] = False
        self.udp.sendGameStartCode()
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
        self.timer_label.place(x=800,y=630)
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
        self.countdown_label.place(x=1000,y=630)

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
            self.red_player_label.place(x=50,y=120+i*30)
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
            self.red_player_score_label.place(x=250,y=120+i*30)
            self.red_scores_list.append(self.red_player_score_label)

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
            self.green_player_label.place(x=550,y=120+i*30)
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
            self.green_player_score_label.place(x=750,y=120+i*30)
            self.red_scores_list.append(self.red_player_score_label)

        self.game_action_text_label = Label(
                self.window,
                text="ADD HERE",
                background=BLUE,
                foreground=ORANGE,
                font=FONT_SIZE,
                width=20,
                height=5
        )
        self.game_action_text_label.place(x=50,y=340)

        def countdown(count):
            self.countdown_label["text"] = count
            if count > 0:
               self.window.after(1000, countdown, count - 1) 

        def receive_player_action(player, object):
            if player == object:
                hit_self(player)
            elif object == 53:
                hit_red_base(player)
            elif object == 43:
                hit_green_base(player)
            else:
                hit_player(player, object)

        def update_player_score(player, team, points):
            for i in range(len(self.red_team_players)):
                if(player == self.red_team_players[i]["id"]):
                    change = int(self.red_scores_list[i]["text"])
                    change += points
                    self.red_scores_list[i]["text"] = change
            if points > 0:
                placement = 1
            else:
                placement = 0
            swap_player_positions(player, team, placement)

        def update_team_score(team, points):
            if team == "red":
                self.red_team_score_label["text"] += points
            else:
                self.green_team_score_label["text"] += points

        def hit_red_base(player):
            for i in range(len(self.green_team_players)):
                if(player == self.green_team_players[i]["id"]):
                    if self.green_team_players[i]["hit_enemy_base"] == False:
                        update_player_score(player, "green", 100)
                        self.green_team_players[i]["hit_enemy_base"] = True
                        
        def hit_green_base(player):
            for i in range(len(self.red_team_players)):
                if(player == self.red_team_players[i]["id"]):
                    if self.red_team_players[i]["hit_enemy_base"] == False:
                        update_player_score(player, "red", 100)
                        self.red_team_players[i]["hit_enemy_base"] = True

        def hit_player(player, object):
            for i in range(len(self.red_team_players)):
                if(player == self.red_team_players[i]["id"]):
                    player_team = "red"
                else: 
                    player_team = "green"
            for i in range(len(self.red_team_players)):
                if(object == self.red_team_players[i]["id"]):
                    object_team = "red"
                else:
                    object_team = "green"
            if player_team != object_team:
                update_player_score(player, player_team, 10)
            else:
                update_player_score(player, player_team, -10)

        def hit_self(player):
            pass

        def swap_player_positions(player, team, placement):
            #if player gains points
            if(placement):
                #if player is on red team
                if(team == "red"):
                    for i in range(len(self.red_team_players)):
                        if(player == self.red_team_players[i]["id"]):
                            #if player is not in top position and has greater score than player above, swap positions
                            if(int(self.red_scores_list[i].cget("text")) != 120 & (int(self.red_scores_list[i].cget("text")) > int(self.red_scores_list[i - 1].cget("text")))):
                                #change positions in red team players
                                player_change = self.red_team_players[i]
                                self.red_team_players[i] = self.red_team_players[i - 1]
                                self.red_team_players[i - 1] = player_change
                                #change positions in red players labels list and change lable position
                                label_change = self.red_players_label_list[i]["text"]
                                label_change_position1 = self.red_players_label_list[i].place_info()
                                label_change_position2 = self.red_players_label_list[i - 1].place_info()
                                self.red_players_label_list[i].place(x=50,y=int(label_change_position2["y"]))
                                self.red_players_label_list[i - 1].place(x=50,y=int(label_change_position1["y"]))
                                self.red_players_label_list[i]["text"] = self.red_players_label_list[i - 1]["text"]
                                self.red_players_label_list[i - 1]["text"] = label_change
                                #change positions in red scores list and change label positions
                                score_change = self.red_scores_list[i]
                                score_change_position1 = self.red_scores_list[i].place_info()
                                score_change_position2 = self.red_scores_list[i - 1].place_info()
                                self.red_scores_list[i].place(x=250,y=int(score_change_position2["y"]))
                                self.red_scores_list[i - 1].place(x=250,y=int(score_change_position1["y"]))
                                self.red_scores_list[i] = self.red_scores_list[i - 1]
                                self.red_scores_list[i - 1] = score_change
                else:
                    for i in range(len(self.green_team_players)):
                        if(player == self.green_team_players[i]["id"]):
                            #if player is not in top position and has greater score than player above, swap positions
                            if(int(self.green_scores_list[i].cget("text")) != 120 & (int(self.green_scores_list[i].cget("text")) > int(self.green_scores_list[i - 1].cget("text")))):
                                #change positions in green team players
                                player_change = self.green_team_players[i]
                                self.green_team_players[i] = self.green_team_players[i - 1]
                                self.green_team_players[i - 1] = player_change
                                #change positions in green players labels list and change lable position
                                label_change = self.green_players_label_list[i]["text"]
                                label_change_position1 = self.green_players_label_list[i].place_info()
                                label_change_position2 = self.green_players_label_list[i - 1].place_info()
                                self.green_players_label_list[i].place(x=550,y=int(label_change_position2["y"]))
                                self.green_players_label_list[i - 1].place(x=550,y=int(label_change_position1["y"]))
                                self.green_players_label_list[i]["text"] = self.green_players_label_list[i - 1]["text"]
                                self.green_players_label_list[i - 1]["text"] = label_change
                                #change positions in green scores list and change label positions
                                score_change = self.green_scores_list[i]
                                score_change_position1 = self.green_scores_list[i].place_info()
                                score_change_position2 = self.green_scores_list[i - 1].place_info()
                                self.green_scores_list[i].place(x=750,y=int(score_change_position2["y"]))
                                self.green_scores_list[i - 1].place(x=750,y=int(score_change_position1["y"]))
                                self.green_scores_list[i] = self.green_scores_list[i - 1]
                                self.green_scores_list[i - 1] = score_change
            else:
                #if player is on red team
                if(team == "red"):
                    for i in range(len(self.red_team_players)):
                        if(player == self.red_team_players[i]["id"]):
                            #if player is not in top position and has greater score than player above, swap positions
                            if(int(self.red_scores_list[i].cget("text")) != 120 + self.max_red_index * 30 & (int(self.red_scores_list[i].cget("text")) < int(self.red_scores_list[i - 1].cget("text")))):
                                #change positions in red team players
                                player_change = self.red_team_players[i]
                                self.red_team_players[i] = self.red_team_players[i - 1]
                                self.red_team_players[i + 1] = player_change
                                #change positions in red players labels list and change lable position
                                label_change = self.red_players_label_list[i]["text"]
                                label_change_position1 = self.red_players_label_list[i].place_info()
                                label_change_position2 = self.red_players_label_list[i + 1].place_info()
                                self.red_players_label_list[i].place(x=50,y=int(label_change_position2["y"]))
                                self.red_players_label_list[i + 1].place(x=50,y=int(label_change_position1["y"]))
                                self.red_players_label_list[i]["text"] = self.red_players_label_list[i + 1]["text"]
                                self.red_players_label_list[i + 1]["text"] = label_change
                                #change positions in red scores list and change label positions
                                score_change = self.red_scores_list[i]
                                score_change_position1 = self.red_scores_list[i].place_info()
                                score_change_position2 = self.red_scores_list[i + 1].place_info()
                                self.red_scores_list[i].place(x=250,y=int(score_change_position2["y"]))
                                self.red_scores_list[i + 1].place(x=250,y=int(score_change_position1["y"]))
                                self.red_scores_list[i] = self.red_scores_list[i + 1]
                                self.red_scores_list[i + 1] = score_change
                else:
                    for i in range(len(self.green_team_players)):
                        if(player == self.green_team_players[i]["id"]):
                            #if player is not in top position and has greater score than player above, swap positions
                            if(int(self.green_scores_list[i].cget("text")) != 120 + self.max_green_index * 30 & (int(self.green_scores_list[i].cget("text")) < int(self.green_scores_list[i - 1].cget("text")))):
                                #change positions in green team players
                                player_change = self.green_team_players[i]
                                self.green_team_players[i] = self.green_team_players[i + 1]
                                self.green_team_players[i + 1] = player_change
                                #change positions in green players labels list and change lable position
                                label_change = self.green_players_label_list[i]["text"]
                                label_change_position1 = self.green_players_label_list[i].place_info()
                                label_change_position2 = self.green_players_label_list[i + 1].place_info()
                                self.green_players_label_list[i].place(x=550,y=int(label_change_position2["y"]))
                                self.green_players_label_list[i - 1].place(x=550,y=int(label_change_position1["y"]))
                                self.green_players_label_list[i]["text"] = self.green_players_label_list[i + 1]["text"]
                                self.green_players_label_list[i + 1]["text"] = label_change
                                #change positions in green scores list and change label positions
                                score_change = self.green_scores_list[i]
                                score_change_position1 = self.green_scores_list[i].place_info()
                                score_change_position2 = self.green_scores_list[i + 1].place_info()
                                self.green_scores_list[i].place(x=750,y=int(score_change_position2["y"]))
                                self.green_scores_list[i + 1].place(x=750,y=int(score_change_position1["y"]))
                                self.green_scores_list[i] = self.green_scores_list[i - 1]
                                self.green_scores_list[i + 1] = score_change



        countdown(360)
        
        update_player_score(2, "red", 10)

        update_player_score(1, "red", 20)

        update_player_score(2, "green", 10)
 
        update_player_score(1, "green", 20)

        thread = Thread(target = self.udp.receiveData())
        thread2 = Thread(target = self.window.mainloop())
        thread.start()
        thread2.start()
        thread.join()
        
