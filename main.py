from tkinter import *

from dotenv import load_dotenv
load_dotenv()

from splash_screen import splash_screen
from entryScreen import Entry_Screen
from countdown import countdown_start
from play_action_display import Play_Action_Display
from upd import Udp
from trafficgenerator import tg

import os
from supabase import create_client, Client

#testing push

#test again

#initialize supabase
url = os.environ.get("supabase_url")
key = os.environ.get("supabase_key")
supabase = create_client(url,key)
play_action_display = Play_Action_Display()
udp = Udp(play_action_display)

splash_screen()
entry_screen = Entry_Screen(supabase, udp)
countdown_start()
play_action_display.start(entry_screen.red_team_players, entry_screen.green_team_players, udp)


# Starts up the udp server
# def startUDP():
#     command = ["python3", "UDP_Client.py"]
#     subprocess.run(command)

