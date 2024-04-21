from tkinter import *
import tkinter as tk

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
    def __init__(self, supabase, red_players, green_players):
        self.red_team_players = red_players
        self.green_team_players = green_players
        self.supabase = supabase
        self.current_red_index = 0
        self.current_green_index = 0
        self.red_players_label_list = []
        self.green_players_label_list = []
        self.red_scores_list = []
        self.green_scores_list = []

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

        def update_player_score(player, points):
            placement = 1
            swap_player_positions(player, placement)
            print()

        def update_team_score(team, points):
            if team == "red":
                self.red_team_score_label["text"] += points
            else:
                self.green_team_score_label["text"] += points

        def hit_base(player):
            points = 0
            for i in range(len(self.red_team_players)):
                if(player == self.red_team_players[i]["id"]):
                    update_player_score(points)
                    update_team_score(points)
        
        def hit_player(player):
            points = 0
            for i in range(len(self.red_team_players)):
                if(player == self.red_team_players[i]["id"]):
                    update_player_score(points)
                    update_team_score(points)

        def swap_player_positions(player, placement):
            #if player gains points
            if(placement):
                #if player is on red team
                for i in range(len(self.red_team_players)):
                    if(player == self.red_team_players[i]["id"]):
                        #if player is not in top position and has greater score than player above, swap positions
                        if(self.red_scores_list[i].cget("text") != 120 & self.red_scores_list[i].cget("text") > self.red_scores_list[i + 1].cget("text")):
                            #change positions in red team players
                            player_change = self.red_team_players[i]
                            self.red_team_players[i] = self.red_team_players[i + 1]
                            self.red_team_players[i + 1] = player_change
                            #change positions in red scores list and change label positions
                            score_change = self.red_scores_list[i]
                            score_change_position1 = self.red_player_score_label[i].place_info()
                            score_change_position1 = self.red_player_score_label[i].place_info()



        countdown(360)

        # Shows window
        self.window.mainloop()
