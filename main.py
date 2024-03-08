from tkinter import *

from dotenv import load_dotenv
load_dotenv()

from splash_screen import splash_screen
from entryScreen import player_entry_screen

import os
from supabase import create_client, Client

#testing push

#initialize supabase
url = os.environ.get("supabase_url")
key = os.environ.get("supabase_key")
supabase = create_client(url,key)

splash_screen()
player_entry_screen(supabase)


# Starts up the udp server
# def startUDP():
#     command = ["python3", "UDP_Client.py"]
#     subprocess.run(command)

