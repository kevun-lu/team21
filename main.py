from tkinter import *

from dotenv import load_dotenv
load_dotenv()

from splash_screen import splash_screen
from entryScreen import Entry_Screen
from countdown import countdown_start
from play_action_display import Play_Action_Display
from updKL import Udp

import os
from supabase import create_client, Client

#testing push

#test again

#initialize supabase
url = os.environ.get("supabase_url")
key = os.environ.get("supabase_key")
supabase = create_client(url,key)
udp = Udp()

splash_screen()
entry_screen = Entry_Screen(supabase, udp)
countdown_start()
play_action_display = Play_Action_Display(supabase, entry_screen.red_team_players, entry_screen.green_team_players)

# Starts up the udp server
# def startUDP():
#     command = ["python3", "UDP_Client.py"]
#     subprocess.run(command)

